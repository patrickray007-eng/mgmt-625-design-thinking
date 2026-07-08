#!/usr/bin/env python3
"""
Royalty Reconciliation Tool
===========================

Reads your distributor payout statements (DistroKid and generic CSV/TSV formats),
applies your distribution-cost model and your contributor splits register, and
tells you exactly:

  * How much GROSS royalty income came in (by song, store, country, period)
  * How much went to DISTRIBUTION (fees + any % cut) and what % of gross that is
  * How much each CONTRIBUTOR is owed, and whether they've been paid
  * How much you NET keep, and your effective take-home %
  * AUDIT FLAGS: songs earning money with no splits defined, contributors owed
    but unpaid, negative/refund lines, and suspicious per-stream rates

It uses ONLY the Python standard library, so it runs anywhere Python 3.8+ is
installed — no `pip install` required.

--------------------------------------------------------------------------------
QUICK START
--------------------------------------------------------------------------------

1. Export your earnings statement(s) from DistroKid:
   Dashboard -> "Bank" (or "Get Paid") -> download the CSV/TSV.
   Drop the file(s) into:   reconciliation/statements/

2. Fill in your fees in:    reconciliation/config.json
   and your splits in:      templates/Splits-Register.csv
   (copy it to reconciliation/Splits-Register.csv or point --splits at it)

3. Run:
       python3 reconcile.py

4. Read the report written to:  reconciliation/output/reconciliation-report.md
   and the per-contributor payout in: reconciliation/output/contributor-payouts.csv

Run `python3 reconcile.py --help` for all options.

--------------------------------------------------------------------------------
IMPORTANT CONCEPTUAL NOTE
--------------------------------------------------------------------------------
A distributor statement (DistroKid, etc.) reports RECORDING / MASTER-side
streaming income only. It does NOT include your PUBLISHING income — that is:
performance royalties (BMI/ASCAP), mechanical royalties (The MLC), or
neighboring-rights royalties (SoundExchange). Those are collected separately and
should be reconciled on their own statements. See ../01-Royalty-Streams-Explained.md
and ../02-Live-Performance-Royalties.md. This tool reconciles the distributor
(master-side) money and applies your splits to it.
"""

import argparse
import csv
import io
import json
import os
import sys
from collections import defaultdict

# ------------------------------------------------------------------------------
# Column detection — different distributors label columns differently. We map a
# set of known aliases to canonical fields so the same code handles DistroKid,
# TuneCore, CD Baby, and hand-rolled CSVs.
# ------------------------------------------------------------------------------
COLUMN_ALIASES = {
    "earnings": [
        "earnings (usd)", "earnings", "net earnings", "amount", "royalty",
        "royalties", "payout", "net", "total", "revenue", "earnings usd",
    ],
    "title": ["title", "song", "song title", "track", "track title", "release"],
    "store": ["store", "retailer", "platform", "dsp", "service", "source"],
    "artist": ["artist", "artist name"],
    "isrc": ["isrc"],
    "quantity": ["quantity", "streams", "units", "plays", "qty"],
    "country": ["country of sale", "country", "territory"],
    "period": ["sale month", "reporting date", "period", "month", "date"],
}


def _norm(s):
    return (s or "").strip().lower().replace("﻿", "")


def detect_columns(header):
    """Return {canonical_field: actual_header} best-effort mapping."""
    norm_map = {_norm(h): h for h in header}
    resolved = {}
    for field, aliases in COLUMN_ALIASES.items():
        for alias in aliases:
            if alias in norm_map:
                resolved[field] = norm_map[alias]
                break
    return resolved


def sniff_delimiter(sample):
    """DistroKid ships TSV; many others ship CSV. Sniff which."""
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;|")
        return dialect.delimiter
    except csv.Error:
        # Fall back: whichever separator appears more in the first line.
        first = sample.splitlines()[0] if sample else ""
        return "\t" if first.count("\t") > first.count(",") else ","


def parse_money(raw):
    """Parse '$1,234.56', '(3.20)' (negative), '1.2E-3', '' -> float."""
    if raw is None:
        return 0.0
    s = str(raw).strip()
    if not s:
        return 0.0
    negative = s.startswith("(") and s.endswith(")")
    s = s.strip("()")
    s = s.replace("$", "").replace(",", "").replace("USD", "").strip()
    if s in ("", "-", "--"):
        return 0.0
    try:
        val = float(s)
    except ValueError:
        return 0.0
    return -val if negative else val


def load_statements(statements_dir):
    """Load every .csv/.tsv/.txt in the directory into normalized line dicts."""
    lines = []
    files_read = []
    if not os.path.isdir(statements_dir):
        return lines, files_read
    for name in sorted(os.listdir(statements_dir)):
        if not name.lower().endswith((".csv", ".tsv", ".txt")):
            continue
        path = os.path.join(statements_dir, name)
        with open(path, "r", encoding="utf-8-sig", newline="") as fh:
            content = fh.read()
        if not content.strip():
            continue
        delim = sniff_delimiter(content[:4096])
        reader = csv.reader(io.StringIO(content), delimiter=delim)
        rows = list(reader)
        if not rows:
            continue
        header = rows[0]
        cols = detect_columns(header)
        if "earnings" not in cols:
            print(f"  ! Skipping {name}: could not find an earnings/amount column.")
            print(f"    Detected header: {header}")
            continue
        idx = {f: header.index(h) for f, h in cols.items()}
        n = 0
        for row in rows[1:]:
            if not any(cell.strip() for cell in row):
                continue

            def get(field, default=""):
                i = idx.get(field)
                return row[i] if i is not None and i < len(row) else default

            lines.append({
                "file": name,
                "earnings": parse_money(get("earnings")),
                "title": get("title").strip() or "(untitled)",
                "store": get("store").strip() or "(unknown store)",
                "artist": get("artist").strip(),
                "isrc": get("isrc").strip().upper(),
                "quantity": parse_money(get("quantity")),
                "country": get("country").strip(),
                "period": get("period").strip(),
            })
            n += 1
        files_read.append((name, n, delim))
    return lines, files_read


def load_splits(splits_path):
    """
    Load the splits register. Expected columns (case-insensitive; extras OK):
        song_title, isrc, contributor, role, split_percent, paid_status
    `split_percent` is that contributor's % of the NET (post-distribution)
    royalties for that song. Rows with the same song accumulate. The remainder
    up to 100% is YOUR share.
    Match priority: ISRC (exact) first, then normalized song title.
    """
    by_isrc = defaultdict(list)
    by_title = defaultdict(list)
    rows = []
    if not splits_path or not os.path.isfile(splits_path):
        return by_isrc, by_title, rows
    with open(splits_path, "r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        norm_field = {_norm(f): f for f in (reader.fieldnames or [])}

        def field(*names):
            for nm in names:
                if nm in norm_field:
                    return norm_field[nm]
            return None

        f_title = field("song_title", "title", "song")
        f_isrc = field("isrc")
        f_contrib = field("contributor", "name", "payee")
        f_role = field("role")
        f_split = field("split_percent", "split", "percent", "share")
        f_paid = field("paid_status", "paid", "status")
        if not (f_contrib and f_split):
            print(f"  ! Splits file {splits_path} missing contributor/split_percent "
                  f"columns; ignoring splits.")
            return by_isrc, by_title, rows
        for r in reader:
            contributor = (r.get(f_contrib) or "").strip()
            if not contributor:
                continue
            pct = parse_money(r.get(f_split))
            entry = {
                "contributor": contributor,
                "role": (r.get(f_role) or "").strip() if f_role else "",
                "split_percent": pct,
                "paid_status": (r.get(f_paid) or "").strip().lower() if f_paid else "",
                "song_title": (r.get(f_title) or "").strip() if f_title else "",
                "isrc": (r.get(f_isrc) or "").strip().upper() if f_isrc else "",
            }
            rows.append(entry)
            if entry["isrc"]:
                by_isrc[entry["isrc"]].append(entry)
            if entry["song_title"]:
                by_title[_norm(entry["song_title"])].append(entry)
    return by_isrc, by_title, rows


def splits_for_song(title, isrc, by_isrc, by_title):
    if isrc and isrc in by_isrc:
        return by_isrc[isrc]
    if title and _norm(title) in by_title:
        return by_title[_norm(title)]
    return None


def money(x):
    return f"${x:,.2f}"


def pct(x):
    return f"{x * 100:.1f}%"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Reconcile music royalty statements.")
    ap.add_argument("--statements", default=os.path.join(here, "statements"),
                    help="Directory of statement CSV/TSV files.")
    ap.add_argument("--config", default=os.path.join(here, "config.json"),
                    help="Path to config.json (fees & distribution model).")
    ap.add_argument("--splits", default=None,
                    help="Path to splits register CSV. Defaults to "
                         "reconciliation/Splits-Register.csv then "
                         "templates/Splits-Register.csv.")
    ap.add_argument("--outdir", default=os.path.join(here, "output"),
                    help="Directory for the report and payout CSV.")
    args = ap.parse_args()

    # ---- config ----
    config = {}
    if os.path.isfile(args.config):
        with open(args.config, "r", encoding="utf-8") as fh:
            config = json.load(fh)
    else:
        print(f"  ! No config at {args.config}; using zero fees. "
              f"Copy config.example.json to config.json and edit it.")
    # Names that mean "me, the owner" — these rows are YOUR share, not an
    # external payout. Configurable via "owner_aliases" in config.json.
    owner_aliases = {a.strip().lower() for a in
                     config.get("owner_aliases", []) if a.strip()}
    owner_aliases.update({"you", "me", "self", "myself", "owner"})
    owner_aliases.add(str(config.get("artist_name", "You")).strip().lower())
    dist = config.get("distribution", {})
    dk_fee = float(dist.get("distrokid_annual_fee", 0) or 0)
    dk_pct = float(dist.get("distrokid_percent_cut", 0) or 0) / 100.0
    other_name = dist.get("other_distributor_name", "Other distributor")
    other_pct = float(dist.get("other_distributor_percent_cut", 0) or 0) / 100.0
    other_flat = float(dist.get("other_distributor_flat_fees", 0) or 0)
    period_label = config.get("period_label", "all statements")
    artist_you = config.get("artist_name", "You")

    # ---- splits path resolution ----
    splits_path = args.splits
    if not splits_path:
        candidates = [
            os.path.join(here, "Splits-Register.csv"),
            os.path.join(here, "..", "templates", "Splits-Register.csv"),
        ]
        for c in candidates:
            if os.path.isfile(c):
                splits_path = c
                break

    # ---- load ----
    print("Loading statements from:", args.statements)
    lines, files_read = load_statements(args.statements)
    if not files_read:
        print("\nNo statement files found. Put your DistroKid CSV/TSV export(s) in:")
        print("   ", args.statements)
        print("A sample file is in reconciliation/sample-data/ you can copy in to test.")
        sys.exit(1)
    for name, n, delim in files_read:
        d = "TSV" if delim == "\t" else "CSV"
        print(f"  - {name}: {n} lines ({d})")

    by_isrc, by_title, split_rows = load_splits(splits_path)
    if splits_path:
        print("Splits register:", splits_path, f"({len(split_rows)} split rows)")
    else:
        print("No splits register found — every earning song will be flagged.")

    # ---- aggregate gross ----
    gross_total = sum(l["earnings"] for l in lines)
    by_song = defaultdict(lambda: {"earnings": 0.0, "quantity": 0.0,
                                   "isrc": "", "title": ""})
    by_store = defaultdict(float)
    by_country = defaultdict(float)
    by_period = defaultdict(float)
    negatives = []
    for l in lines:
        key = l["isrc"] or _norm(l["title"])
        s = by_song[key]
        s["earnings"] += l["earnings"]
        s["quantity"] += l["quantity"]
        s["isrc"] = s["isrc"] or l["isrc"]
        s["title"] = s["title"] or l["title"]
        by_store[l["store"]] += l["earnings"]
        if l["country"]:
            by_country[l["country"]] += l["earnings"]
        if l["period"]:
            by_period[l["period"]] += l["earnings"]
        if l["earnings"] < 0:
            negatives.append(l)

    # ---- distribution cost ----
    # DistroKid keeps 100% of royalties by default, so its "cost" is the flat
    # annual fee. A %-cut distributor (or Smith Music, if it takes a cut) is
    # applied against gross. This is a MODEL — adjust config to match reality.
    dist_pct_cost = gross_total * dk_pct + gross_total * other_pct
    dist_flat_cost = dk_fee + other_flat
    dist_total_cost = dist_pct_cost + dist_flat_cost
    net_after_dist = gross_total - dist_total_cost

    # ---- apply splits on NET-after-distribution ----
    contributor_owed = defaultdict(float)
    contributor_meta = {}
    songs_no_splits = []
    songs_over_100 = []
    your_share_total = 0.0
    per_song_rows = []
    for key, s in by_song.items():
        earn = s["earnings"]
        net_song = earn - (dist_pct_cost + 0)  # % cut is proportional; flat fee handled globally
        # Distribute the flat fee proportionally to each song by its gross share
        if gross_total > 0:
            net_song = earn * (1 - dk_pct - other_pct) - dist_flat_cost * (earn / gross_total)
        else:
            net_song = 0.0
        rows = splits_for_song(s["title"], s["isrc"], by_isrc, by_title)
        total_pct = 0.0            # every row, incl. your own explicit rows
        owner_explicit_pct = 0.0   # rows that name you (the owner)
        external_pct = 0.0         # rows that name someone else
        song_contrib_detail = []
        if rows:
            for r in rows:
                total_pct += r["split_percent"]
                if r["contributor"].strip().lower() in owner_aliases:
                    owner_explicit_pct += r["split_percent"]
                    continue  # your own share — not an external payout
                external_pct += r["split_percent"]
                share = r["split_percent"] / 100.0
                owed = net_song * share
                contributor_owed[r["contributor"]] += owed
                contributor_meta.setdefault(r["contributor"], set()).add(r["role"] or "contributor")
                song_contrib_detail.append((r["contributor"], r["split_percent"], owed))
            if total_pct > 100.0001:
                songs_over_100.append((s["title"], total_pct))
        else:
            if earn > 0:
                songs_no_splits.append((s["title"], s["isrc"], earn))
        # Your share = your explicit rows + any unallocated remainder up to 100%.
        remainder_pct = max(0.0, 100.0 - total_pct)
        your_pct = (owner_explicit_pct + remainder_pct) / 100.0
        your_song_share = net_song * your_pct
        your_share_total += your_song_share
        per_song_rows.append({
            "title": s["title"], "isrc": s["isrc"], "gross": earn,
            "net": net_song, "contrib_pct": external_pct,
            "your_share": your_song_share, "detail": song_contrib_detail,
        })

    contributor_total = sum(contributor_owed.values())

    # ---- write outputs ----
    os.makedirs(args.outdir, exist_ok=True)
    report_path = os.path.join(args.outdir, "reconciliation-report.md")
    payout_path = os.path.join(args.outdir, "contributor-payouts.csv")

    def share_of_gross(x):
        return pct(x / gross_total) if gross_total else "n/a"

    per_song_rows.sort(key=lambda r: r["gross"], reverse=True)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Royalty Reconciliation Report\n\n")
        f.write(f"**Period:** {period_label}  \n")
        f.write(f"**Statements processed:** {len(files_read)} file(s), "
                f"{len(lines)} line items  \n")
        f.write(f"**Generated by:** reconcile.py (distributor / master-side income only)\n\n")

        f.write("## 1. The bottom line — where every dollar went\n\n")
        f.write("| Bucket | Amount | % of gross |\n|---|--:|--:|\n")
        f.write(f"| **Gross royalties collected** | {money(gross_total)} | 100.0% |\n")
        f.write(f"| Distribution — % cut | {money(dist_pct_cost)} | {share_of_gross(dist_pct_cost)} |\n")
        f.write(f"| Distribution — flat fees | {money(dist_flat_cost)} | {share_of_gross(dist_flat_cost)} |\n")
        f.write(f"| **Distribution — total** | {money(dist_total_cost)} | {share_of_gross(dist_total_cost)} |\n")
        f.write(f"| Paid to contributors | {money(contributor_total)} | {share_of_gross(contributor_total)} |\n")
        f.write(f"| **Your net take-home** | {money(your_share_total)} | {share_of_gross(your_share_total)} |\n\n")
        check = dist_total_cost + contributor_total + your_share_total
        f.write(f"*Reconciliation check:* {money(check)} vs gross {money(gross_total)} "
                f"(difference {money(gross_total - check)} — should be ~$0).\n\n")

        f.write("## 2. Distribution efficiency\n\n")
        if gross_total > 0:
            take_home_pct = your_share_total / gross_total
            f.write(f"- You keep **{pct(take_home_pct)}** of every gross dollar after "
                    f"distribution and contributor splits.\n")
            f.write(f"- Distribution costs you **{share_of_gross(dist_total_cost)}** of gross.\n")
            if dk_fee and gross_total:
                breakeven = "already past break-even" if gross_total > dk_fee else \
                    f"NOT yet at break-even — you paid {money(dk_fee)} in fees to collect {money(gross_total)}"
                f.write(f"- DistroKid flat fee vs. gross: {breakeven}.\n")
        f.write("\n")

        f.write("## 3. Earnings by store / platform\n\n")
        f.write("| Store | Earnings | % |\n|---|--:|--:|\n")
        for store, amt in sorted(by_store.items(), key=lambda kv: kv[1], reverse=True):
            f.write(f"| {store} | {money(amt)} | {share_of_gross(amt)} |\n")
        f.write("\n")

        if by_country:
            f.write("## 4. Earnings by country (top 15)\n\n")
            f.write("| Country | Earnings |\n|---|--:|\n")
            for c, amt in sorted(by_country.items(), key=lambda kv: kv[1], reverse=True)[:15]:
                f.write(f"| {c} | {money(amt)} |\n")
            f.write("\n")

        f.write("## 5. Earnings & splits by song\n\n")
        f.write("| Song | ISRC | Gross | Net after dist. | Contributors % | Your share |\n")
        f.write("|---|---|--:|--:|--:|--:|\n")
        for r in per_song_rows:
            f.write(f"| {r['title']} | {r['isrc'] or '—'} | {money(r['gross'])} | "
                    f"{money(r['net'])} | {r['contrib_pct']:.0f}% | {money(r['your_share'])} |\n")
        f.write("\n")

        f.write("## 6. Contributor payouts owed\n\n")
        if contributor_owed:
            f.write("| Contributor | Role(s) | Owed for this period |\n|---|---|--:|\n")
            for name, owed in sorted(contributor_owed.items(), key=lambda kv: kv[1], reverse=True):
                roles = ", ".join(sorted(contributor_meta.get(name, {"contributor"})))
                f.write(f"| {name} | {roles} | {money(owed)} |\n")
            f.write(f"\nSee `contributor-payouts.csv` for the itemized, per-song breakdown.\n\n")
        else:
            f.write("_No contributor splits matched any earning songs. Either you are the "
                    "sole owner, or your splits register needs song titles/ISRCs that match "
                    "your statements (see audit flags below)._\n\n")

        f.write("## 7. ⚠️ Audit flags\n\n")
        flagged = False
        if songs_no_splits:
            flagged = True
            f.write(f"**{len(songs_no_splits)} earning song(s) have NO entry in your splits "
                    f"register.** If any of these have co-writers, producers, or featured "
                    f"artists, someone may be owed money and not getting it — or you may be "
                    f"over-paying. Add them to the register:\n\n")
            for title, isrc, earn in sorted(songs_no_splits, key=lambda t: t[2], reverse=True)[:50]:
                f.write(f"- {title} ({isrc or 'no ISRC'}) — earned {money(earn)}\n")
            f.write("\n")
        if songs_over_100:
            flagged = True
            f.write("**Songs where contributor splits exceed 100%** (you'd pay out more than "
                    "you earn — a data error):\n\n")
            for title, p in songs_over_100:
                f.write(f"- {title}: splits total {p:.0f}%\n")
            f.write("\n")
        unpaid = [(r["contributor"], r) for r in split_rows
                  if r["paid_status"] in ("", "unpaid", "owed", "no", "pending")]
        if unpaid:
            flagged = True
            names = sorted({c for c, _ in unpaid})
            f.write(f"**Contributors with unpaid/blank payment status** in the register: "
                    f"{', '.join(names)}. Confirm whether they've actually been paid and "
                    f"update the `paid_status` column.\n\n")
        if negatives:
            flagged = True
            neg_total = sum(l["earnings"] for l in negatives)
            f.write(f"**{len(negatives)} negative/refund line(s)** totaling {money(neg_total)} "
                    f"— normal (chargebacks/corrections) but verify they're legitimate.\n\n")
        # Suspicious per-stream rate check
        low_rate_songs = []
        for r in per_song_rows:
            key = r["isrc"] or _norm(r["title"])
            q = by_song[key]["quantity"]
            if q > 1000 and r["gross"] > 0:
                rate = r["gross"] / q
                if rate < 0.0005:  # < $0.0005/stream is unusually low
                    low_rate_songs.append((r["title"], rate, q))
        if low_rate_songs:
            flagged = True
            f.write("**Unusually low per-stream payout** (< $0.0005/stream) — worth checking "
                    "the statement isn't mixing units, or a store is underpaying:\n\n")
            for title, rate, q in low_rate_songs:
                f.write(f"- {title}: ${rate:.5f}/stream over {q:,.0f} units\n")
            f.write("\n")
        if not flagged:
            f.write("No audit flags. Splits, payments, and rates all look consistent. ✅\n\n")

        f.write("## 8. What this report does NOT include\n\n")
        f.write("This reconciles **distributor / master-side streaming income only**. It does "
                "NOT include your publishing income, which is collected separately and is often "
                "where the biggest uncollected money sits:\n\n")
        f.write("- **Performance royalties** (BMI/ASCAP) — incl. live. See "
                "`../02-Live-Performance-Royalties.md`.\n")
        f.write("- **Mechanical royalties** (The MLC, free) — US streaming mechanicals.\n")
        f.write("- **Neighboring-rights / digital performance** (SoundExchange, free) — master side.\n")
        f.write("- **Sync** licensing income.\n\n")
        f.write("Reconcile those against their own statements; see "
                "`../01-Royalty-Streams-Explained.md` for who collects each and how to sign up.\n")

    # ---- contributor payout CSV (itemized) ----
    with open(payout_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["contributor", "song_title", "isrc", "split_percent",
                    "song_net_after_dist", "owed_this_period"])
        for r in per_song_rows:
            for name, spct, owed in r["detail"]:
                w.writerow([name, r["title"], r["isrc"], f"{spct:.2f}",
                            f"{r['net']:.2f}", f"{owed:.2f}"])

    # ---- console summary ----
    print("\n" + "=" * 64)
    print("RECONCILIATION SUMMARY —", period_label)
    print("=" * 64)
    print(f"  Gross royalties collected : {money(gross_total)}")
    print(f"  Distribution total cost   : {money(dist_total_cost)}  ({share_of_gross(dist_total_cost)} of gross)")
    print(f"  Paid to contributors      : {money(contributor_total)}  ({share_of_gross(contributor_total)} of gross)")
    print(f"  YOUR net take-home        : {money(your_share_total)}  ({share_of_gross(your_share_total)} of gross)")
    print("-" * 64)
    if songs_no_splits:
        print(f"  ⚠  {len(songs_no_splits)} earning song(s) missing from splits register")
    if unpaid:
        print(f"  ⚠  contributors with unpaid/blank status present")
    print(f"\n  Full report : {report_path}")
    print(f"  Payout CSV  : {payout_path}\n")


if __name__ == "__main__":
    main()

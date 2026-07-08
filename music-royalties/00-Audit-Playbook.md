# The Royalty Audit Playbook

A repeatable, do-this-in-order audit. Run **Phase 0–4 fully once** (a weekend's
work spread over a couple of sittings), then run the **Quarterly Loop** every 3
months. Each step says *why it matters* and *what "done" looks like* so you can
check it off.

Time budget: Phase 0–4 ≈ 3–5 hours the first time. Quarterly Loop ≈ 30–45 min.

---

## Phase 0 — Take inventory (know what you own)

**Goal:** a complete list of every song, who's on it, and where it lives.

- [ ] **List every release.** Pull your DistroKid catalog (and any releases via
  Smith Music Group). For each: title, ISRC, UPC, release date, and every person
  who contributed (co-writers, featured artists, producers, session players).
- [ ] **Note who owns the master vs. who wrote the song** for each track. These
  are different rights with different payers (see `01-Royalty-Streams-Explained.md`).
- [ ] **Confirm your identifiers.** You need your **BMI IPI/CAE number** (find it
  in your BMI account). You'll reuse it at The MLC and SoundExchange.

✅ **Done when:** you have a row for every song in `templates/Splits-Register.csv`,
even if some split %s are still "TBD".

---

## Phase 1 — Audit that YOU are getting paid (the income side)

**Goal:** verify the money that should be arriving actually is, and measure the cut.

- [ ] **Export DistroKid earnings.** Bank → *"See Excruciating Detail"* →
  **Download**. Drop the file into `reconciliation/statements/`. (If you have
  multiple years/exports, drop them all in — the tool merges them.)
- [ ] **Export any Smith Music Group statements** you have. If they distribute or
  administer any of your catalog, get their payout reports too. (Use
  `templates/Smith-Music-Questions.md` to request them and understand the terms.)
- [ ] **Run the reconciliation tool** (`python3 reconciliation/reconcile.py`).
  Read `reconciliation/output/reconciliation-report.md`.
- [ ] **Sanity-check the store totals.** Do Spotify/Apple numbers look plausible
  vs. your streaming dashboards? A store that's in your streaming stats but
  missing from earnings = a delivery or accounting problem to chase.
- [ ] **Check per-stream rates.** The tool flags songs paying < $0.0005/stream.
  Normal blended rates are roughly **$0.003–$0.005/stream** on Spotify; an
  order-of-magnitude miss means mismatched units or an underpaying channel.
- [ ] **Reconcile withdrawals.** Add up what actually hit your bank account vs.
  what the statements say you earned, minus withdrawal fees. Gaps = unwithdrawn
  balance or fee leakage.

✅ **Done when:** the report's "where every dollar went" table reconciles to ~$0,
and you can state your **effective take-home %** in one sentence.

---

## Phase 2 — Audit that CONTRIBUTORS are getting paid (the payout side)

**Goal:** no collaborator is silently owed money, and no one is being overpaid.

- [ ] **Finalize the splits register.** Fill every `split_percent` in
  `templates/Splits-Register.csv`. If a song has collaborators but no agreed
  split, that's your top-priority gap — the tool flags these as *"NO entry in
  your splits register."*
- [ ] **Match splits to signed agreements.** For each non-solo song, is there a
  **signed split sheet**? If not, create one now with
  `templates/Split-Sheet-Template.md` — memories fade and disputes are expensive.
- [ ] **Distinguish the two kinds of splits.** *Master/recording splits* govern
  the streaming money DistroKid pays. *Songwriting/composition splits* govern
  the publishing money (BMI/MLC). They're often the same people at different
  percentages. Record both (the register has room for notes).
- [ ] **Run the tool and read Section 6 (payouts owed) + Section 7 (flags).**
  Update `paid_status` for anyone already paid; log actual payments in
  `templates/Contributor-Payments-Log.csv`.
- [ ] **Decide your pay mechanism.** For DistroKid-distributed songs, the cleanest
  fix is **DistroKid Splits** — it auto-pays each collaborator their % directly,
  takes **0%**, and removes you as the manual middleman. ($10/yr per collaborator
  who doesn't have their own DistroKid account.) See `01-Royalty-Streams-Explained.md`.

✅ **Done when:** every earning song has defined splits, every non-solo song has a
signed split sheet, and no contributor has an unexplained unpaid balance.

---

## Phase 3 — Plug the leaks (collect money you're currently missing)

**Goal:** turn on every free collection channel and catch back-payments.

Work the full **`templates/Registration-Checklist.md`**. The high-leverage items:

- [ ] **The MLC (free).** Register as a **Self-Administered Songwriter**, add your
  IPI, register your catalog. Run the **Missing Member / unclaimed royalties
  lookup** — there's a large historical "black box" of unmatched mechanicals.
  *(If Smith Music or another admin already registers you at the MLC, do NOT
  double-register — confirm first to avoid conflicts.)*
- [ ] **SoundExchange (free).** Register as **both** performer and sound-recording
  owner (you self-release). Collects SiriusXM/Pandora/webcaster money on your
  *recordings* that nobody else pays you. Check their unclaimed/back-catalog list.
- [ ] **BMI works registration.** Confirm **every** song is registered at BMI with
  correct writer/publisher splits. Unregistered songs earn nothing at the PRO.
- [ ] **BMI Live.** Submit your recent shows (see `02-Live-Performance-Royalties.md`).
  Deadline is short — treat it as **6 months** from the show date.
- [ ] **Foreign royalties.** Decide whether to sign a publishing admin (Songtrust,
  Sentric, etc.) to sweep international performance + mechanical money. Weigh the
  15–20% cut against how much foreign streaming you actually have. *(Watch for
  overlap with Smith Music Group's publishing admin — don't pay two admins for
  the same rights.)*

✅ **Done when:** the Registration Checklist shows every free channel "Active" and
you've made a deliberate yes/no call on a paid publishing admin.

---

## Phase 4 — Maximize the percentage you keep

**Goal:** structurally increase take-home, not just plug leaks.

- [ ] **Right-size your DistroKid plan.** You pay a flat fee regardless of earnings,
  so the fee is a *fixed cost* — the more you earn, the smaller its %. But don't
  overpay for tiers you don't use (Ultimate is for managing many artists). Match
  the plan to the features you actually need.
- [ ] **Audit every % add-on.** DistroKid keeps **20%** of YouTube Content ID and
  **20%** of its Publishing Admin. Those can be worth it (money you'd otherwise
  miss) — but confirm each one is *net positive*, i.e., it's collecting money you
  couldn't collect for free yourself.
- [ ] **Avoid double-dipping intermediaries.** The classic indie leak is paying
  *two* services to collect the *same* right (e.g., DistroKid Publishing **and**
  Songtrust **and** Smith Music all claiming publishing admin). Pick one per right.
- [ ] **Cut withdrawal fee leakage.** Withdraw in larger, less frequent batches;
  prefer ACH ($1.07) over wire ($16+). Small frequent withdrawals bleed fees.
- [ ] **Register directly where it's free.** Every right you can collect yourself
  (MLC, SoundExchange, BMI) at **0%** is money you shouldn't hand a 15–20% admin
  for — reserve admins for what you genuinely can't reach (mainly foreign).
- [ ] **Grow the pie, not just the slice.** The biggest lever is usually more
  qualifying performances and placements: more BMI Live submissions, pitching for
  sync, and playlist/streaming growth. Take-home % optimization caps out; catalog
  and performance growth doesn't.

✅ **Done when:** you've made an explicit keep/cut decision on every fee and add-on,
and there's no right being administered by more than one intermediary.

---

## The Quarterly Loop (repeat every 3 months)

1. Export the latest DistroKid (and Smith Music) statements → `reconciliation/statements/`.
2. Run `reconcile.py`; skim the report and **audit flags**.
3. Pay out anything owed to contributors; update the payments log.
4. **Submit the quarter's live shows to BMI Live** (don't let the 6-month window lapse).
5. Skim The MLC + SoundExchange for newly matched/unclaimed money.
6. Note quarter-over-quarter: is your take-home % holding, and which stores/songs moved?

> **Tip:** put a recurring calendar reminder on the 15th of Jan/Apr/Jul/Oct. The
> ASCAP OnStage deadline grid (Jun 30 / Sep 30 / Dec 31 / Mar 31) is a good mental
> anchor even as a BMI writer — submit live claims before those dates and you'll
> never miss a window.

---

## Red flags that mean "dig deeper"

- A store appears in your streaming analytics but **not** in your earnings export.
- Your **effective take-home %** dropped between periods with no plan/add-on change.
- A collaborator's **owed balance keeps growing** and never moves to "paid."
- The **same right** (e.g., publishing) shows up under **two** intermediaries.
- Per-stream rate on a song is an **order of magnitude** off your others.
- You're paying an **annual fee larger than that catalog's annual earnings** (a
  release that no longer earns its keep — consider consolidating or "Leave a Legacy").

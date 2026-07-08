# Reconciliation Tool

`reconcile.py` reads your distributor payout statements plus your splits register
and produces a full breakdown of **where every royalty dollar went** — distribution
%, contributor %, your take-home % — with audit flags. Pure Python 3.8+, **no
`pip install` needed**.

## Files

```
reconciliation/
├── reconcile.py            # the tool
├── config.json             # YOUR fees & distribution model (edit this)
├── config.example.json     # annotated reference copy
├── statements/             # <- drop your DistroKid / Smith Music exports here
├── sample-data/            # a fake DistroKid export so you can test it first
└── output/                 # generated report + payout CSV land here
```

## Setup (once)

1. **Copy the sample to test:**
   ```
   cp sample-data/distrokid-sample.tsv statements/    # optional, to see it work
   python3 reconcile.py --statements sample-data --splits ../templates/Splits-Register.csv
   ```
   Open `output/reconciliation-report.md`.

2. **Edit `config.json`** with the fees you actually pay (see comments in
   `config.example.json`). Set `other_distributor_percent_cut` only once you've
   confirmed Smith Music Group's actual cut (see `../templates/Smith-Music-Questions.md`).

3. **Fill in `../templates/Splits-Register.csv`** with your real songs and splits.

## Run (each quarter)

```
# 1. Export DistroKid: Bank -> "See Excruciating Detail" -> Download
# 2. Put the file(s) in statements/
# 3. Run:
python3 reconcile.py
```

By default it reads `statements/`, `config.json`, and the splits register (it looks
for `Splits-Register.csv` in this folder, then in `../templates/`). Override any
path:

```
python3 reconcile.py \
  --statements /path/to/exports \
  --config config.json \
  --splits ../templates/Splits-Register.csv \
  --outdir output
```

## What it outputs

- **`output/reconciliation-report.md`** — the readable audit: bottom-line dollar
  flow, distribution efficiency, earnings by store/country/song, contributor
  payouts owed, and **audit flags** (songs missing from your splits register,
  unpaid contributors, splits over 100%, refunds, suspicious per-stream rates).
- **`output/contributor-payouts.csv`** — itemized, per-song, what each collaborator
  is owed for the period. Feed this into your payments workflow.

## How it decides who gets what

1. Sums **gross** royalties across all statement lines.
2. Subtracts **distribution cost** — DistroKid's flat annual fee (its royalty cut is
   0%) plus any %-cut distributor you configure (e.g. Smith Music). This yields
   **net**.
3. Applies your **splits register** per song. Rows that name **you** (aliases: your
   configured `artist_name`, plus "You/Me/Self/Owner") are counted as *your* share.
   Rows naming anyone else are **contributor payouts**. Any % not allocated in the
   register defaults to **you**.
4. Whatever remains after distribution and contributor payouts is **your take-home**.

The three buckets always sum back to gross (there's a reconciliation check line in
the report that should read ~$0).

## Statement formats supported

- **DistroKid** TSV/CSV exports (auto-detected).
- Generic CSV/TSV from other distributors — it maps common column names
  (earnings/amount, title/song, store/platform, isrc, quantity/streams, country,
  period) automatically. If it can't find an earnings column, it prints the header
  it saw so you can rename a column and re-run.
- Drop in **multiple files** (multiple years, multiple distributors) — they merge.

## Known limitations (by design, for a v1 audit)

- **Master-side income only.** It reconciles distributor statements, i.e., streaming
  income on your recordings. It does **not** pull in BMI, MLC, or SoundExchange
  income — those are separate statements. The report's Section 8 reminds you of this.
- **`paid_status` is per-register-row, not per-period.** If you paid a collaborator
  for an earlier period, the tool still shows their full owed amount for the current
  statement set; use `../templates/Contributor-Payments-Log.csv` to track actual
  cumulative payments. Match the statement date range to the period you're settling.
- **Splits are applied to the whole song's net.** If a contributor's % changed
  mid-period, split the statement into two date-ranged runs.
- It's a **model**, not your accountant's ledger. It's for spotting leaks and
  quantifying flows, not filing taxes.

## Troubleshooting

- *"could not find an earnings/amount column"* — your export uses an unusual header.
  Open the file, rename the money column to `Earnings (USD)` (or `amount`), re-run.
- *A song shows 0% contributors but has collaborators* — it's not matched in the
  register. Check the song **title/ISRC in the register matches the statement**
  exactly (ISRC match wins over title). The tool flags these in Section 7.
- *Your take-home shows $0 or negative* — your splits for that song sum to ≥100% to
  non-you contributors; check the register (Section 7 flags splits over 100%).

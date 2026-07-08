# Music Royalty Audit Toolkit

A practical system to (1) verify you and your collaborators are actually getting
paid, (2) measure exactly what % of your royalties goes to distribution and to
contributors, (3) find and increase the money you keep, and (4) claim live
performance royalties with as little manual work as possible.

Built for your setup: **US songwriter + performing artist, distributing through
DistroKid** (and possibly **Smith Music Group** in Fort Worth), **BMI-affiliated**.

> ⚠️ **Not legal or tax advice.** This is an operational toolkit built from
> publicly available 2026 information (sources cited throughout). Rates, fees,
> and program rules change — confirm anything money-critical against your own
> logged-in accounts before acting. Where research couldn't confirm a figure to
> a primary source, it's flagged *unverified*.

---

## What's in here

| File | What it does |
|---|---|
| **`00-Audit-Playbook.md`** | The step-by-step audit. Start here. A repeatable checklist to run once fully, then quarterly. |
| **`01-Royalty-Streams-Explained.md`** | The 4 money buckets a US songwriter/artist can collect, who collects each, what it costs, and where you're most likely leaving money on the table. |
| **`02-Live-Performance-Royalties.md`** | How to claim BMI Live performance royalties, the deadlines, and how to automate/streamline setlist submission. |
| **`reconciliation/reconcile.py`** | A tool that reads your DistroKid statements + your splits register and tells you exactly where every dollar went (distribution %, contributor %, your %), with audit flags. Pure Python, no installs. |
| **`templates/Splits-Register.csv`** | The master record of who owns/earns what on each song. The backbone of the whole audit. |
| **`templates/Split-Sheet-Template.md`** | A per-song split sheet to sign with collaborators so ownership is never ambiguous. |
| **`templates/Contributor-Payments-Log.csv`** | A ledger of what you've actually paid each collaborator and when. |
| **`templates/Registration-Checklist.md`** | Every place you should be registered to collect all your money — with your status column to fill in. |
| **`templates/Smith-Music-Questions.md`** | The exact questions to ask Smith Music Group so you know precisely what rights they administer and what cut they take. |

---

## The 20-minute quick start

1. **Read `00-Audit-Playbook.md`** — it orders everything below.
2. **Export your DistroKid earnings** (Bank → "See Excruciating Detail" → Download)
   and drop the file(s) into `reconciliation/statements/`.
3. **Fill in `templates/Splits-Register.csv`** with every song and who's owed what.
4. **Edit `reconciliation/config.json`** with the fees you actually pay.
5. **Run** `python3 reconciliation/reconcile.py` and read the report it generates.
6. **Work the Registration Checklist** to plug the leaks (The MLC and SoundExchange
   are free money most indies miss).

---

## The one-paragraph summary of your situation

As a **self-published BMI songwriter who also performs and owns your masters**, you
have up to **four separate income streams**, collected by four different
organizations. DistroKid only pays you one of them (master-side streaming) and
keeps **0%** of it — its only cost to you is the annual subscription. The money
you're most likely *not* collecting is: **mechanical royalties (The MLC — free),
neighboring-rights royalties (SoundExchange — free), live performance royalties
(BMI Live — free), and foreign publishing royalties (needs an admin).** Good news
for you specifically: **BMI pays a self-published writer BOTH the writer and
publisher shares directly**, so you are *not* losing ~50% by lacking a publishing
company. The single biggest audit risk on the *paying-out* side is undocumented
splits with collaborators — which the splits register and reconciliation tool fix.

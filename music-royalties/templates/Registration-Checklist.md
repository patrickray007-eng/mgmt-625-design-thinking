# Registration Checklist — collect all your money

Every place a self-published US songwriter + performing artist should be registered.
Fill in the **Status** and **Notes** columns as you work through it. Anything marked
"free" is money you should never pay an intermediary to collect for you.

Your reusable key: once you have your **BMI IPI/CAE number**, you'll enter it at The
MLC and SoundExchange. Grab it first.

---

## Core registrations

| # | Where | Collects | Cost | Priority | Status | Notes |
|---|---|---|---|---|---|---|
| 1 | **BMI** (bmi.com) — writer affiliation | Performance royalties (writer + publisher share, incl. live) | Free | Done? | ☐ | Confirm every song is registered as a **work** with correct splits |
| 2 | **BMI Direct Deposit** | (enables payment + BMI Live) | Free | Required | ☐ | Must be on to use BMI Live |
| 3 | **The MLC** (themlc.com) — Self-Administered Songwriter | US streaming/download **mechanicals** | Free (0%) | High | ☐ | Needs IPI. **Check for conflicts first** — don't double-register if an admin already does |
| 4 | **SoundExchange** (soundexchange.com) — performer **and** SR owner | Neighboring rights on **recordings** (SiriusXM, Pandora, webcasters) | Free | High | ☐ | You self-release → register as both roles |
| 5 | **DistroKid** — distribution | Master-side streaming (Spotify/Apple/etc.) | $24.99–$89.99/yr | Done? | ☐ | You already have this. Match plan to features used |

---

## Payout hygiene

| # | Action | Why | Status | Notes |
|---|---|---|---|---|
| 6 | Turn on **DistroKid Splits** for collaborative songs | Auto-pays collaborators their %, 0% cut, removes you as middleman | ☐ | $10/yr per collaborator without a DistroKid account |
| 7 | Keep **Splits-Register.csv** current | Backbone of the audit; feeds reconcile.py | ☐ | |
| 8 | Signed **split sheet** per non-solo song | Dispute protection + correct registrations | ☐ | Use Split-Sheet-Template.md |
| 9 | Log actual payments in **Contributor-Payments-Log.csv** | Proves who's been paid | ☐ | |

---

## Optional / situational

| # | Where | Collects | Cost | When it's worth it | Status | Notes |
|---|---|---|---|---|---|---|
| 10 | **Publishing admin** (Songtrust $100 + 15%/20%, Sentric $0 + 20%, CD Baby Pro, TuneCore Pub) | **Foreign** performance + mechanicals; can submit setlists | 15–20% cut | If you have real international streaming and want hands-off foreign collection | ☐ | **Avoid overlap** with Smith Music / DistroKid Publishing |
| 11 | **DistroKid Publishing add-on** | Publishing royalties DistroKid can reach | 20% cut | Only if it's net-positive vs. free DIY (MLC/BMI) | ☐ | Don't stack with another admin |
| 12 | **DistroKid YouTube Content ID** | YouTube UGC revenue | 20% cut | If your music appears in others' YouTube videos | ☐ | |
| 13 | **Own BMI publishing company** | (separates publisher share) | $175 indiv / $250 LLC one-time | Branding, co-pub deals — **not** needed to collect publisher share at BMI | ☐ | BMI already pays you the publisher share as self-published |
| 14 | **Sync licensing** (self-pitch or agent) | Film/TV/ad/game placements | Free / negotiated cut | Upside; needs clean metadata + registered splits | ☐ | |

---

## Smith Music Group — resolve the open question

| # | Action | Status | Notes |
|---|---|---|---|
| 15 | Confirm **which rights** Smith Music administers (distribution? publishing? both?) | ☐ | Use Smith-Music-Questions.md |
| 16 | Confirm their **exact commission %** and put it in `config.json` | ☐ | Until confirmed, leave at 0 but flag as open |
| 17 | Confirm they aren't **double-administering** a right you also collect directly | ☐ | Biggest overlap risk: publishing/mechanicals |
| 18 | Get their **payout statements** for reconciliation | ☐ | Drop into reconciliation/statements/ |

---

### Suggested order of operations
1. **#1–2** (BMI works + direct deposit) → **#3–4** (MLC + SoundExchange, free money)
   → **#15–18** (pin down Smith Music) → **#6–9** (payout hygiene) → then decide
   **#10–14** deliberately.
2. Re-run `reconcile.py` after #15–18 so Smith Music's cut (if any) shows in your
   distribution %.

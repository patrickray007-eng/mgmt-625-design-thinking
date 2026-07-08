# Questions for Smith Music Group

**Why this matters:** Smith Music Group (Fort Worth Stockyards; smithmusic.com)
appears to offer **both distribution/royalty collection *and* publishing
administration** ("Rick Smith Publishing"). A company in that position can take a
cut on **two** of your income streams at once — your master-side streaming *and*
your composition-side publishing — and can **overlap or conflict** with DistroKid,
The MLC, BMI, or any publishing admin you use. You can't audit what you can't see,
so pin down exactly what they do for you and at what price.

> If you're **not** actually working with Smith Music, you can ignore this file —
> but the discovery came from your mention of "Smith music (Fort Worth, TX)," so
> confirm one way or the other.

Send these (email/phone: per their site, ~ (817) 378-0900 / ricky@smithmusic.com)
or ask in your next conversation. Record answers in the right-hand column.

---

## 1. Scope — which of my rights do you administer?

| Question | Their answer |
|---|---|
| Do you handle **distribution** of my recordings (getting them on Spotify/Apple/etc.), or is that separate/DistroKid? | |
| Do you act as my **publishing administrator** (collecting performance + mechanical royalties on my songs)? | |
| Do you administer **both** the master and the composition, or just one? | |
| Which **specific releases / songs** of mine are under your administration? | |
| Are you registered as a **publisher of record** on any of my works (at BMI / The MLC)? Which ones? | |

## 2. Money — what's the cut?

| Question | Their answer |
|---|---|
| What **percentage** do you take on distribution/streaming royalties? | |
| What **percentage** do you take on publishing (performance / mechanical)? | |
| Are there **flat fees** (annual, per-release, setup)? | |
| Are there **payout/withdrawal fees** or minimums? | |
| How and how often are **royalties paid out** to me, and can I get itemized statements? | |

## 3. Overlap & conflict — the audit risk

| Question | Their answer |
|---|---|
| Do you register my songs at **The MLC** on my behalf? *(If yes, I must NOT self-register — avoid conflicts.)* | |
| Do you collect my **BMI** performance royalties or the **publisher share**, or does BMI still pay me directly? | |
| Do you collect **foreign** royalties for me? Through which sub-publishers/territories? | |
| Is there anything you administer that I'm **also** collecting via DistroKid Publishing, Songtrust, or directly? | |

## 4. Control & exit

| Question | Their answer |
|---|---|
| What's the **contract term**, and how do I **terminate**? | |
| On exit, do my works get **released back** to me and **re-registered** in my name? | |
| Can I get a **full statement/export** of everything collected on my behalf to date? | |
| Who at your company is my **point of contact** for royalty questions? | |

---

## After you get answers

1. Put their **distribution %** into `reconciliation/config.json`
   (`other_distributor_percent_cut`) and re-run `reconcile.py`.
2. Update the **Registration Checklist** items #15–18.
3. If they administer a right you're **also** collecting elsewhere, decide which one
   to keep — you should pay **one** intermediary per right, not two.
4. Request their **payout statements** and drop them in `reconciliation/statements/`
   so their income shows up in your reconciliation alongside DistroKid.

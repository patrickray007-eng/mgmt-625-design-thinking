---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Open+Sans:wght@400;600&display=swap');

  :root {
    --teal: #0D9488;
    --navy: #1E3A5F;
    --orange: #F97316;
    --dark-gray: #4B5563;
    --light-mint: #F0FDFA;
    --body-gray: #374151;
  }

  section {
    font-family: 'Open Sans', sans-serif;
    color: var(--body-gray);
    background: #ffffff;
    background-image: radial-gradient(ellipse at top right, rgba(13, 148, 136, 0.04) 0%, transparent 60%);
    padding: 40px 60px;
    text-align: left;
  }

  h1, h2, h3 {
    font-family: 'Montserrat', sans-serif;
    text-transform: none;
  }

  h2 {
    color: var(--navy);
    font-weight: 700;
    font-size: 1.6em;
    margin-bottom: 4px;
    border-bottom: 4px solid var(--teal);
    border-bottom-width: 4px;
    padding-bottom: 8px;
    display: inline-block;
  }

  h3 {
    color: var(--teal);
    font-weight: 600;
    font-size: 1em;
  }

  strong {
    color: var(--navy);
    font-weight: 600;
  }

  ul, ol {
    font-size: 0.9em;
    line-height: 1.6;
  }

  ul li::marker {
    color: var(--teal);
  }

  ol li::marker {
    color: var(--teal);
    font-weight: 700;
  }

  /* Title slide */
  section.title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  section.title h1 {
    color: var(--navy);
    font-size: 2.2em;
    font-weight: 700;
    line-height: 1.2;
  }

  section.title h2 {
    border-bottom: none;
    display: block;
    color: var(--dark-gray);
    font-size: 0.85em;
    font-weight: 400;
  }

  section.title p.pre-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 0.7em;
    color: var(--teal);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 0;
  }

  section.title p.footer {
    font-size: 0.55em;
    color: #9CA3AF;
    margin-top: 40px;
  }

  /* Activity box */
  .activity-box {
    background: var(--dark-gray);
    color: #ffffff;
    border-radius: 12px;
    padding: 24px 28px;
    margin: 16px 0;
    font-size: 0.85em;
    line-height: 1.65;
  }

  .activity-box strong {
    color: #ffffff;
  }

  .time-tag {
    display: inline-block;
    background: rgba(255, 255, 255, 0.15);
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.85em;
    margin-top: 8px;
  }

  /* Callout box */
  .callout-box {
    background: var(--light-mint);
    border-left: 4px solid var(--teal);
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin: 16px 0;
    font-size: 0.82em;
    color: var(--navy);
    line-height: 1.5;
  }

  /* Orange accent */
  .orange {
    color: var(--orange);
    font-weight: 600;
  }

  /* Reminder box */
  .reminder {
    display: inline-block;
    background: rgba(249, 115, 22, 0.08);
    border: 1px solid rgba(249, 115, 22, 0.25);
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 0.72em;
    color: var(--dark-gray);
    margin-top: 12px;
  }

  .reminder .label {
    font-weight: 600;
    color: var(--orange);
  }

  /* Two-column layout */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 36px;
    align-items: start;
  }

  /* Concept card */
  .concept-card {
    background: #ffffff;
    border: 1.5px solid #E5E7EB;
    border-radius: 10px;
    padding: 18px 20px;
    font-size: 0.82em;
    line-height: 1.55;
  }

  .concept-card.highlight {
    border-color: var(--teal);
    background: var(--light-mint);
  }

  .concept-card h3 {
    margin: 0 0 6px 0;
  }

  .concept-card p {
    margin: 4px 0;
  }

  /* Transition slide */
  section.transition {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  section.transition h1 {
    color: var(--navy);
    font-size: 2em;
    font-weight: 700;
  }

  section.transition p {
    color: var(--dark-gray);
    font-size: 0.9em;
  }

  /* Quote slide */
  section.quote {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 60px 120px;
  }

  section.quote blockquote {
    border: none;
    font-size: 1.3em;
    color: var(--navy);
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    line-height: 1.5;
  }

  section.quote blockquote p {
    margin: 0;
  }

  section.quote .attribution {
    font-family: 'Open Sans', sans-serif;
    font-size: 0.55em;
    color: var(--dark-gray);
    font-weight: 400;
    margin-top: 16px;
  }

  /* Hide pagination on title/transition/quote slides */
  section.title::after,
  section.transition::after,
  section.quote::after {
    display: none;
  }
---

<!-- _class: title -->

<p class="pre-title">Session 4</p>

# Learning to Synthesize

<h2>Design Thinking for MBAs (Hybrid Section)</h2>

<p class="footer">Thursday, March 26, 2026 &ensp;|&ensp; 6:30 PM &ensp;|&ensp; Online (Zoom) &ensp;|&ensp; Faculty: Patrick Ray</p>

---

## Find the Duct Tape

<div class="activity-box">

**You've been in the field for two weeks.** What duct tape did you find? What workarounds are people using in the problem spaces you investigated?

Two people share. Keep it quick.

<span class="time-tag">8 minutes</span>
</div>

Tonight you learn how to turn raw data into **insight**.

---

## Tonight's Plan

Before you touch your own data, we're going to practice **synthesis** together on a shared dataset.

<div class="two-col">
<div>

### First Half
Guided synthesis on a real design project's field data.

</div>
<div>

### Second Half
Apply the same method to your own research, then stress test your causal loop maps.

</div>
</div>

---

## Design Ability Tonight

<div class="concept-card highlight" style="max-width: 600px;">

### Synthesize Information

Move from **raw data** to **patterns** to **insight**. The hardest design ability because your brain wants to skip steps.

</div>

Synthesis is finding the thing the data is telling you that **you didn't already believe**.

---

<!-- _class: transition -->

# The Exercise

45 field observations. 5 observers. One problem space.

What is this data telling us?

---

## The Design Brief

### "Voting access in the LGBT community"

5 observers went to spaces across Houston's Montrose neighborhood.

<div class="two-col">
<div>

- **A**: Montrose bar, weeknight
- **B**: LGBT resource center
- **C**: Coffee shop / bookstore

</div>
<div>

- **D**: Different bar, weekend
- **E**: Community support group

</div>
</div>

<div class="callout-box">

This data comes from real community spaces. If the content resonates personally, that's valid. We're focused on synthesis as a method.

</div>

---

## Silent Reading

<div class="activity-box">

**Read all 45 observations.** I've dropped a PDF in the chat. Open it and read.

Notice what you notice. Don't try to organize yet. Just read.

<span class="time-tag">7 minutes &ensp;|&ensp; Silent</span>
</div>

When time is up: **drop in the chat** the number of one observation that surprised you, and one word for why.

---

<!-- _class: transition -->

# Guided Synthesis

Four moves.

---

## Move 1: Observations vs. Interpretations

<div class="two-col">
<div>

### Observation
What you saw, heard, counted.

*"The younger person kept looking around the room while writing."*

</div>
<div>

### Interpretation
What you think it means.

*"...like she was blocking the view from the rest of the room."*

</div>
</div>

**Interpretations are hypotheses, not facts.**

---

## Move 2: Cluster

Group observations that seem related. Narrate your reasoning.

<div class="callout-box">

Not "these are all about voting." **Why** do they go together?

"I'm putting 1, 10, 20, and 33 together. They all vote, none have access problems. But they all say something else is wrong."

</div>

When an observation could go in two clusters, that tension is telling you something.

---

## Move 3: Name the Patterns

<div class="two-col">
<div>

### Vague
- "Barriers to voting"
- "Community stuff"
- "Trust issues"

</div>
<div>

### Precise
- "People who can access polls but experience voting as hostile or pointless"
- "Community infrastructure that replaces institutional services"
- "Rational withdrawal from systems perceived as unsafe"

</div>
</div>

If the name doesn't surprise you, it's a category, not an insight.

---

<!-- _class: quote -->

> "Access to what, though?"

<p class="attribution">Bartender, Observation #44</p>

---

## Move 4: Break the Frame

The brief said **"Voting access in the LGBT community."**

Based on this data, is voting access actually the problem?

- How many people here have an actual **access** problem?
- What do the non-voters say about **why**?
- What has this community already **built for itself**?

<div class="callout-box">

Synthesis doesn't just organize your data. It can <strong>break your frame</strong>.

</div>

---

## What Synthesis Revealed

- **Trust**: "I access a system that doesn't want me in it and nothing changes"
- **Safety**: "You think I'm putting my real address on a government form?"
- **Deliberate choice**: Non-voters have specific reasons. This isn't apathy.
- **Community self-reliance**: Mutual aid, community fridges, legal networks. "We take care of us."
- **Exhaustion**: "I did everything right in 2020... I'm tired."

The problem isn't access. It's the **relationship between this community and formal institutions**.

---

<!-- _class: transition -->

# Your Turn

Same method. Your data.

---

## Your Turn

Your data will be harder because you're invested in it. That investment will make you want to skip to conclusions.

<div class="callout-box">

Does your data confirm your assumptions, or does it tell a <strong>different story</strong>?

</div>

---

## Team Synthesis Protocol

<div class="activity-box">

**Breakout rooms by team.**

1. Each person posts their raw observations on the team whiteboard. **No narrating. Silent.** (5 min)
2. Everyone reads everyone else's observations. **Silent.** (3 min)
3. One person starts clustering. Others can **only ask questions**, not move stickies. Rotate after 4 min.
4. **Name three patterns.** Write one sentence for each.
5. **Identify one thing that doesn't fit** any pattern. Discuss what it might mean.

<span class="time-tag">20 minutes</span>
</div>

---

<!-- _class: transition -->

# Stress Test Your Causal Loop

You built it before you synthesized. Does it still hold?

---

## Causal Loop Stress Test

<div class="activity-box">

**Pull up your causal loop map** (the one you submitted today).

Look at it through the lens of what you just synthesized.

- **What holds up?** Which loops does your research data actually support?
- **What's missing?** Is there a dynamic your data revealed that isn't on the map?
- **What did you assume?** Point to a loop. Is it based on evidence or assumption?
- **What needs to change?** Mark it. You don't have to fix it now. Name it.

<span class="time-tag">15 minutes</span>
</div>

---

## Assignment Changes

A few things are shifting based on where we are in the course:

| What | Old | New | Why |
|------|-----|-----|-----|
| **Problem Definition (A05)** | Due Apr 4 | **Due Apr 1** | So I can review and give feedback before Session 5 |
| **Final Presentation (A06)** | Session 5 (Apr 4) | **Session 6 (Apr 9)** | You'll run an experiment between S5 and S6, then present what you learned |
| **Reflection Essay (A08)** | Due Apr 9 | **Cut** | The experiment presentation replaces it |

---

## What's Due

### Problem Definition Document — Wednesday, April 1

- **Bounded, evidence-based problem statement**
- **Revised causal loop map** with what changed after tonight and why
- I'll review and give feedback **before Session 5**

Write it while the thinking is fresh.

---

## What's Ahead

**Session 5** (Sat Apr 4, in-person): You come in with a defined problem. We ideate, stress test, and design experiments.

**Session 6** (Thu Apr 9, online): You present what you tested and what you learned.

<div class="reminder">
<span class="label">Find the Duct Tape:</span> Keep collecting.
</div>

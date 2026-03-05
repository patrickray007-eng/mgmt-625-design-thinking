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

  /* Hide pagination on title/transition slides */
  section.title::after,
  section.transition::after {
    display: none;
  }
---

<!-- _class: title -->

<p class="pre-title">Session 3</p>

# Stakeholder Mapping +<br>Research Planning

<h2>Design Thinking for MBAs (Hybrid Section)</h2>

<p class="footer">Thursday, March 12, 2026 &ensp;|&ensp; 6:30 PM &ensp;|&ensp; Online (Zoom) &ensp;|&ensp; Faculty: Patrick Ray</p>

---

## Check-In

<div class="activity-box">

**Quick round:** Has anything shifted in your thinking since Session 2?

What did writing about your observation experience surface?

<span class="time-tag">10 minutes</span>
</div>

<div class="callout-box">

"By the end of tonight, your team will have a research plan. The next two weeks are fieldwork."

</div>

---

## Tonight's Arc

Two breakout room cycles, two deliverables:

<div class="two-col">
<div>

### Stakeholder Mapping
- Identify 4-5 stakeholders for your scenario
- Include at least one <span class="orange">extreme user</span>
- Map concerns, constraints, access

</div>
<div>

### Research Planning
- Design your two-week distributed plan
- Map each member's unique access
- Leave with specific assignments

</div>
</div>

<div class="reminder">
<span class="label">Find the Duct Tape:</span> Document one workaround or improvised fix in your notebook this week.
</div>

---

## Stakeholder Mapping

<div class="activity-box">

**Breakout rooms by team.** Identify 4-5 stakeholders for your scenario.

For each stakeholder:
1. Who are they? (specific: "night shift warehouse supervisor," not "employee")
2. What do they optimize for?
3. What constraints do they face?
4. What are their top 2-3 concerns?
5. Which team member can access this stakeholder type?

Include at least one **extreme user**: someone who experiences the problem most intensely.

<span class="time-tag">25 minutes</span>
</div>

---

## What Makes a Good Stakeholder Map?

<div class="two-col">
<div>

### Go Specific
- Not "customers" but <span class="orange">"first-time parents buying online"</span>
- Not "employees" but <span class="orange">"mid-career nurses on night shift"</span>
- The more specific, the more useful your research will be

</div>
<div>

### Find Extreme Users
- Who experiences this problem **most intensely**?
- Who has a **workaround**?
- Who has **given up** on the existing solution?
- These perspectives reveal what normal users won't tell you

</div>
</div>

---

## Debrief: The Overlooked Stakeholder

<div class="activity-box">

**Back to main room.** Each team shares one stakeholder they almost forgot or didn't initially consider.

<span class="time-tag">15 minutes</span>
</div>

- Why do we overlook certain stakeholders?
- What makes some <span class="orange">invisible</span>?
- "Learning From Others" means seeking perspectives you wouldn't naturally encounter

<div class="callout-box">

"The stakeholders you overlook are often the ones with the most revealing perspective."

</div>

---

<!-- _class: transition -->

# The Method Transition

From observation to empathy interviews

---

## Observation → Interviews

In TETHER, you practiced pure observation: watching without asking. That discipline matters, and you'll keep using it.

Now you add a new tool: **the empathy interview.**

<div class="two-col">
<div>

### Observation Shows
- **What** people do
- Behaviors, patterns, workarounds
- The visible surface of the problem

</div>
<div>

### Interviews Reveal
- **Why** they do it
- Motivations, constraints, frustrations
- The invisible logic underneath

</div>
</div>

You need both. You've mapped stakeholders on paper. Now you actually talk to them.

---

## The Distributed Advantage

Your team's superpower is that you're in **different places.**

- Different cities
- Different workplaces
- Different industries

Each of you can reach stakeholders the others can't.

<div class="callout-box">

That's not a limitation of the hybrid format. It's the strategy.

</div>

---

## Research Planning

<div class="activity-box">

**Back to breakout rooms.** Create a concrete research plan for the next two weeks.

1. Who can each team member **reach**? Map your combined access.
2. What will each person **do**? (Observation, interview, or both)
3. What specific **questions** or observation targets for each stakeholder?
4. How will you **coordinate** async? (Slack, GroupMe, text, shared doc)
5. When will you **compile** findings? (Must be before Session 4, March 26)

Each member: 1-2 substantial observations or interviews. **Depth, not breadth.**

<span class="time-tag">25 minutes</span>
</div>

---

## What a Good Research Plan Looks Like

Not "we'll do some research." Instead:

<div class="concept-card highlight" style="margin: 16px 0;">

**Sarah** interviews two pediatric nurses at Houston Methodist (week 1). Shares notes in team Google Doc by March 20.

**Marcus** observes shift handoff at his company's warehouse in Dallas (March 14). Posts photos + field notes by March 17.

**Team sync**: 30-min Zoom on March 22 to compile findings before Session 4.

</div>

Names. Dates. Stakeholders. Coordination method. Compile deadline.

---

## Share Research Plans

<div class="activity-box">

**Back to main room.** Each team briefly shares:

- Who's doing what, and where?
- What's your coordination plan?
- When will findings be compiled?

<span class="time-tag">10 minutes</span>
</div>

---

## The Research Period

### March 12 - 26

- Each team member conducts **1-2 substantial** observations or interviews
- Focus on **depth**, not breadth
- Document in your notebook; contribute to your team's shared document
- Coordinate with your team asynchronously

<div class="two-col">
<div>

### Due Session 4 (March 26)
- **Stakeholder Research**: Compiled team research document
- **Causal Loop Map**: Diagram of problem dynamics, feedback loops, who benefits

</div>
<div>

### Not a Survey
- Don't send a Google Form to 50 people
- Talk to 1-2 stakeholders in depth
- Observe in context when possible
- Quality of insight over quantity of data

</div>
</div>

---

## What's Next

- **Session 4**: Thursday, March 26, 6:30 PM (Online, Zoom)
- Synthesize research, build causal loop maps, define the problem
- Use the two-week gap to conduct research in your own environments

<div class="callout-box">

"The next two weeks are yours. Use them."

</div>

<div class="reminder">
<span class="label">Find the Duct Tape:</span> Each week, identify and document one workaround or improvised fix in your notebook.
</div>

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

  /* Chat prompt */
  .chat-prompt {
    background: rgba(13, 148, 136, 0.08);
    border: 1px solid rgba(13, 148, 136, 0.25);
    border-radius: 10px;
    padding: 18px 24px;
    margin: 16px 0;
    font-size: 0.82em;
    text-align: center;
    color: var(--navy);
  }

  .chat-prompt .chat-icon {
    font-size: 0.7em;
    color: var(--teal);
    font-weight: 600;
    margin-bottom: 6px;
    font-family: 'Montserrat', sans-serif;
    letter-spacing: 1px;
  }

  /* Two-column layout */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 36px;
    align-items: start;
  }

  /* Three-column layout */
  .three-col {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 24px;
    align-items: start;
  }

  /* Phase box */
  .phase-box {
    background: var(--light-mint);
    border-radius: 10px;
    padding: 18px 20px;
    text-align: center;
  }

  .phase-box .phase-label {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: var(--teal);
    font-size: 0.75em;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
  }

  .phase-box .phase-name {
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    color: var(--navy);
    font-size: 0.9em;
    margin-bottom: 4px;
  }

  .phase-box .phase-sessions {
    font-size: 0.72em;
    color: var(--dark-gray);
  }

  /* Video label */
  .video-label {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 0.65em;
    color: var(--teal);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
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

  /* Scenario card */
  .scenario-card {
    background: var(--light-mint);
    border-radius: 10px;
    padding: 14px 16px;
    font-size: 0.82em;
  }

  .scenario-card .scenario-label {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: var(--teal);
    font-size: 0.7em;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
  }

  .scenario-card .scenario-name {
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    color: var(--navy);
    font-size: 0.88em;
    margin-bottom: 6px;
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

  /* Design abilities: highlighted vs not */
  .ability-active {
    background: var(--teal);
    color: #ffffff;
    border-radius: 8px;
    padding: 10px 16px;
    margin-bottom: 8px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    font-size: 0.78em;
  }

  .ability-active strong {
    color: #ffffff;
  }

  .ability-inactive {
    background: #F3F4F6;
    color: #9CA3AF;
    border-radius: 8px;
    padding: 10px 16px;
    margin-bottom: 8px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    font-size: 0.78em;
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

  /* Closing slide */
  section.closing h2 {
    border-bottom: 4px solid var(--teal);
  }

  /* Table styling */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.78em;
    margin: 12px 0;
  }

  th {
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    color: var(--navy);
    text-align: left;
    padding: 8px 12px;
    border-bottom: 2px solid var(--teal);
  }

  td {
    padding: 8px 12px;
    border-bottom: 1px solid #E5E7EB;
    color: var(--body-gray);
  }

  tr:last-child td {
    border-bottom: none;
  }

  /* Hide pagination on title/transition slides */
  section.title::after,
  section.transition::after {
    display: none;
  }
---

<!-- _class: title -->

<p class="pre-title">Session 2</p>

# Observation Debrief +<br>Team Formation

<h2>Design Thinking for MBAs (Hybrid Section)</h2>

<p class="footer">Saturday, March 7, 2026 &ensp;|&ensp; 8:00 AM &ensp;|&ensp; In-Person (McNair Hall 216) &ensp;|&ensp; Faculty: Patrick Ray</p>

---

## Today's Plan

<div class="three-col">
<div>
<div class="phase-box">
  <div class="phase-label">Morning</div>
  <div class="phase-name">Observation Tools</div>
  <div class="phase-sessions">Duct Tape debrief, AEIOU framework</div>
</div>
</div>
<div>
<div class="phase-box">
  <div class="phase-label">Field Trip</div>
  <div class="phase-name">AEIOU Live</div>
  <div class="phase-sessions">METRORail ride, paired observation</div>
</div>
</div>
<div>
<div class="phase-box">
  <div class="phase-label">Afternoon</div>
  <div class="phase-name">Project 2 Launch</div>
  <div class="phase-sessions">Scenarios, teams, research planning</div>
</div>
</div>
</div>

Three arcs, one through-line: learning to see what's actually happening before deciding what it means.

---

## Find the Duct Tape

<div class="activity-box">

You've been looking for workarounds and improvised fixes since Session 1. **What did you find?**

1. What's the fix?
2. What's the real problem underneath?
3. Why hasn't the real fix happened?

<span class="time-tag">3-4 volunteers share with the class</span>
</div>

---

## AEIOU: An Observation Framework

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px 28px; margin-bottom: 16px;">
  <div style="font-size: 0.78em; line-height: 1.55;">
    <strong style="color: var(--teal); font-family: 'Montserrat', sans-serif; font-size: 1.1em;">A</strong><strong> = Activities</strong><br>
    What are people doing? Tasks, routines, sequences?
  </div>
  <div style="font-size: 0.78em; line-height: 1.55;">
    <strong style="color: var(--teal); font-family: 'Montserrat', sans-serif; font-size: 1.1em;">E</strong><strong> = Environments</strong><br>
    What's the space like? How does it shape behavior?
  </div>
  <div style="font-size: 0.78em; line-height: 1.55;">
    <strong style="color: var(--teal); font-family: 'Montserrat', sans-serif; font-size: 1.1em;">I</strong><strong> = Interactions</strong><br>
    Between people? Between people and objects or systems?
  </div>
  <div style="font-size: 0.78em; line-height: 1.55;">
    <strong style="color: var(--teal); font-family: 'Montserrat', sans-serif; font-size: 1.1em;">O</strong><strong> = Objects</strong><br>
    What tools, artifacts, devices are present? What's missing?
  </div>
  <div style="font-size: 0.78em; line-height: 1.55;">
    <strong style="color: var(--teal); font-family: 'Montserrat', sans-serif; font-size: 1.1em;">U</strong><strong> = Users</strong><br>
    Who's here? Who's NOT here? Different types?
  </div>
</div>

<div class="callout-box">
In consulting, this is one way to structure a site visit. In product development, it's a useful lens for documenting user behavior.
</div>

---

## AEIOU Applied

Look at your TETHER notes. Which of these five did you naturally gravitate toward? Which did you miss?

<div class="chat-prompt" style="margin-top: 20px;">
<div class="chat-icon">REFLECT</div>
Most people over-index on Activities and under-index on Environment and Users. Where did you land?
</div>

<div class="callout-box" style="margin-top: 20px;">
<strong>Design Ability: Move Between Concrete and Abstract.</strong> AEIOU helps you do this. You zoom into a specific interaction, then zoom out to ask what it means for the system.
</div>

---

## Train Ride: AEIOU in the Field

<div class="activity-box">

You just learned the AEIOU framework from your own notes. **Now use it live.**

- Pair up. You'll observe together and compare notes after.
- Use AEIOU on everything you see: the walk, the platform, the train, the riders, the stations.
- We ride 3 stops north and come back. About an hour total.
- One question to hold: **who was this system designed for, and who's using it right now?**

</div>

<div class="reminder" style="margin-top: 12px;">
<span class="label">Fare note:</span> Tap a credit card or phone at the platform validator before boarding ($1.25).
</div>

---

## Field Trip Debrief: What Did You See?

<div class="activity-box">

**Share one AEIOU observation from the ride.**

- What did you notice in each category?
- What surprised you?
- Who was this system designed for, and who's using it right now?

</div>

---

## Field Trip Debrief: The Space Knob

<div class="chat-prompt" style="margin-bottom: 20px;">
<div class="chat-icon">DISCUSS</div>
How was observing on a train different from your TETHER?
</div>

<div class="chat-prompt" style="margin-bottom: 20px;">
<div class="chat-icon">DISCUSS</div>
What did the E category reveal about the U category?
</div>

<div class="callout-box">
"In design, space is a variable you can control. I changed yours today. That's a tool you can use."
</div>

---

## From Observation to Problem

<div class="callout-box" style="margin-bottom: 16px;">
"In design, space is a variable you can control. I changed yours today. That's a tool you can use."
</div>

<div class="activity-box">

Take one observation from the ride. Turn it into a problem statement:

**"The problem I observed is X <span style="color: var(--orange);">because</span> Y."**

</div>

- Is that a symptom or a root cause?
- What's the underlying system?
- What would you need to investigate further?

---

<div class="video-label">GE Adventure Series &ensp;|&ensp; <a href="https://www.ideou.com/blogs/inspiration/from-design-thinking-to-creative-confidence" target="_blank" style="color: var(--teal); text-decoration: none; font-size: 0.85em;">Source: IDEO U</a></div>

## The Problem

<div class="two-col" style="align-items: center;">
<div>

- **Doug Dietz**, industrial designer at GE Healthcare. Two years designing a new MRI scanner.
- Went to see it installed. Watched a little girl walking toward his machine, crying. A nurse was waiting with sedation.
- **80% of pediatric patients** required sedation. Not because the scan hurt. Because the experience was terrifying.

<div class="callout-box" style="margin-bottom: 0;">
A cold room, loud sounds, a giant machine, strange instructions from strangers.
</div>

</div>
<div style="text-align: center;">

![w:100%](./mri-standard.jpg)

<p style="font-size: 0.6em; color: var(--dark-gray); margin-top: 6px;">What a child sees walking into this room.</p>

</div>
</div>

---

<div class="video-label">GE Adventure Series</div>

## The Observation

- Dietz went to Stanford's d.school, learned design thinking, then went back to the field.
- But not to the hospital first. He went to a **daycare**. Watched how kids interact with unfamiliar environments.
- Shadowed child life specialists. Interviewed families, doctors, nurses, technicians.

<div class="callout-box" style="margin-top: 20px;">
Key finding: The machine wasn't the problem. The room was the problem. The hallway was the problem. The entire environment was designed for the machine, not for the person inside it.
</div>

---

<div class="video-label">GE Adventure Series</div>

## The Solution

<div class="two-col" style="align-items: center;">
<div>

- Themed decals on existing rooms: pirate ships, jungle safaris, space voyages
- Technicians got scripts: "Hold very still so the pirates don't find you."
- Same machine. Completely different experience.
- **Sedation rates: 80% down to roughly 10%.** Patient satisfaction up 90%.

</div>
<div>

![w:100%](./ge-adventure-pirate.jpg)

</div>
</div>

<div class="callout-box">
The fix cost a fraction of a hardware redesign. That's what observation can do.
</div>

---

<div class="video-label">GE Adventure Series</div>

## Same Machine, Different Room

<div class="two-col" style="gap: 20px;">
<div>

![w:100%](./ge-adventure-mri.jpg)

<p style="font-size: 0.65em; color: var(--dark-gray); margin-top: 6px; text-align: center;">Space Adventure</p>

</div>
<div>

![w:100%](./ge-adventure-series.jpg)

<p style="font-size: 0.65em; color: var(--dark-gray); margin-top: 6px; text-align: center;">City Adventure</p>

</div>
</div>

<p style="margin-top: 16px; text-align: center; font-size: 0.82em; color: var(--navy); font-weight: 600;">The entire environment was designed for the machine, not for the person inside it.</p>
<p style="margin-top: 12px; text-align: center; font-size: 0.65em; color: var(--dark-gray);">Read the full story: <a href="https://www.ideou.com/blogs/inspiration/from-design-thinking-to-creative-confidence" target="_blank" style="color: var(--teal);">From Design Thinking to Creative Confidence</a> (IDEO U)</p>

---

## Project 2: The Journey

<div style="display: flex; align-items: center; gap: 0; margin-top: 16px; margin-bottom: 24px;">
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 14px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.62em; flex: 1;">Today<br><span style="font-weight: 400; font-size: 0.9em;">Teams +<br>Scenarios</span></div>
  <div style="color: var(--teal); font-size: 1.4em; padding: 0 4px;">&#8594;</div>
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 14px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.62em; flex: 1;">Session 3<br><span style="font-weight: 400; font-size: 0.9em;">Stakeholder Map +<br>Research Plan</span></div>
  <div style="color: var(--teal); font-size: 1.4em; padding: 0 4px;">&#8594;</div>
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 14px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.62em; flex: 1;">2 Weeks<br><span style="font-weight: 400; font-size: 0.9em;">Distributed<br>Fieldwork</span></div>
  <div style="color: var(--teal); font-size: 1.4em; padding: 0 4px;">&#8594;</div>
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 14px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.62em; flex: 1;">Session 4<br><span style="font-weight: 400; font-size: 0.9em;">Synthesize +<br>Causal Loops</span></div>
  <div style="color: var(--teal); font-size: 1.4em; padding: 0 4px;">&#8594;</div>
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 14px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.62em; flex: 1;">Session 5<br><span style="font-weight: 400; font-size: 0.9em;">Present +<br>Stress Test</span></div>
  <div style="color: var(--teal); font-size: 1.4em; padding: 0 4px;">&#8594;</div>
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 14px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.62em; flex: 1;">Session 6<br><span style="font-weight: 400; font-size: 0.9em;">Reflect</span></div>
</div>

Your team picks a scenario today, investigates it in the field, then presents a systems-level analysis of what you found.

---

## Project 2 Scenarios

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px;">
  <div class="scenario-card">
    <div class="scenario-label">Scenario A</div>
    <div class="scenario-name">The First 90 Days</div>
    <p style="font-size: 0.78em;">How do new employees learn to navigate an organization?</p>
  </div>
  <div class="scenario-card">
    <div class="scenario-label">Scenario B</div>
    <div class="scenario-name">Small Business Friction</div>
    <p style="font-size: 0.78em;">What makes running a small business harder than it needs to be?</p>
  </div>
  <div class="scenario-card">
    <div class="scenario-label">Scenario C</div>
    <div class="scenario-name">The Feedback Gap</div>
    <p style="font-size: 0.78em;">How do organizations learn what's not working?</p>
  </div>
  <div class="scenario-card">
    <div class="scenario-label">Scenario D</div>
    <div class="scenario-name">Access Barriers</div>
    <p style="font-size: 0.78em;">Why can't people access services designed for them?</p>
  </div>
  <div class="scenario-card">
    <div class="scenario-label">Scenario E</div>
    <div class="scenario-name">Volunteer Experience</div>
    <p style="font-size: 0.78em;">What makes volunteering sustainable, or not?</p>
  </div>
  <div class="scenario-card">
    <div class="scenario-label">Scenario F</div>
    <div class="scenario-name">Mission vs. Operations</div>
    <p style="font-size: 0.78em;">How do mission-driven organizations navigate competing pressures?</p>
  </div>
</div>

---

## Activity: The "Why?" Interview

In TETHER and on the train, you practiced observation: watching without asking. Now you add a new tool: the **empathy interview**.

<div class="activity-box">
<p style="margin: 0 0 8px 0; font-size: 0.85em; opacity: 0.8;">ROUND 1</p>

**Silent Listening**

Ask your partner: "Tell me about a time you had to figure something out with no instructions."

Your partner talks. **You only listen.** No words, no follow-ups. Just nods, eye contact, leaning in.

<span class="time-tag">2 min each, then switch roles</span>
</div>

---

## Round 2: Only "Why?"

<div class="activity-box">
<p style="margin: 0 0 8px 0; font-size: 0.85em; opacity: 0.8;">ROUND 2</p>

Same topic, same partner. After each response, you can only ask **"Why?"**

Nothing else. Just "Why?"

<span class="time-tag">2 min each, then switch roles</span>
</div>

<div class="callout-box" style="margin-top: 16px;">
Notice how one word can unlock a deeper layer. "Why?" forces the speaker past their rehearsed answer.
</div>

---

## Round 3: Open-Ended Questions

<div class="activity-box">
<p style="margin: 0 0 8px 0; font-size: 0.85em; opacity: 0.8;">ROUND 3</p>

Same topic, same partner. Now you can ask **any open-ended question**.

No yes/no questions. Follow your curiosity. Go where the conversation takes you.

<span class="time-tag">2 min each, then switch roles</span>
</div>

<div class="callout-box" style="margin-top: 16px;">
Notice the difference. You now have silence, "why?", and open questions in your toolkit. Which got you the most interesting response?
</div>

---

## Reflection: The "Why?" Interview

- How did that feel? What was challenging?
- When did the conversation get <span class="orange">interesting</span>?
- What surprised you about what you heard?
- How did silence change the dynamic?
- Which round produced more <span class="orange">honest</span> responses?

<div class="callout-box" style="margin-top: 16px;">
Most people find Round 1 harder but more productive. Silence creates space for the other person to think. That discomfort is where the real answers live.
</div>

---

## Empathy Interview Principles

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
  <div style="background: var(--light-mint); border-radius: 10px; padding: 16px 20px;">
    <p style="margin: 0 0 4px 0; font-family: 'Montserrat', sans-serif; font-weight: 700; color: var(--teal); font-size: 0.75em; letter-spacing: 1px;">LISTEN</p>
    <p style="margin: 0; font-size: 0.78em;"><strong>More than you talk.</strong> Your job is to understand their world, not explain yours.</p>
  </div>
  <div style="background: var(--light-mint); border-radius: 10px; padding: 16px 20px;">
    <p style="margin: 0 0 4px 0; font-family: 'Montserrat', sans-serif; font-weight: 700; color: var(--teal); font-size: 0.75em; letter-spacing: 1px;">FOLLOW CURIOSITY</p>
    <p style="margin: 0; font-size: 0.78em;">When something surprises you, go deeper. <strong>"Tell me more about that."</strong></p>
  </div>
  <div style="background: var(--light-mint); border-radius: 10px; padding: 16px 20px;">
    <p style="margin: 0 0 4px 0; font-family: 'Montserrat', sans-serif; font-weight: 700; color: var(--teal); font-size: 0.75em; letter-spacing: 1px;">STORIES, NOT OPINIONS</p>
    <p style="margin: 0; font-size: 0.78em;"><span class="orange">"Tell me about a time when..."</span> beats "What do you think about..."</p>
  </div>
  <div style="background: var(--light-mint); border-radius: 10px; padding: 16px 20px;">
    <p style="margin: 0 0 4px 0; font-family: 'Montserrat', sans-serif; font-weight: 700; color: var(--teal); font-size: 0.75em; letter-spacing: 1px;">EMBRACE SILENCE</p>
    <p style="margin: 0; font-size: 0.78em;">After they answer, <strong>wait</strong>. They'll often fill the silence with something more interesting.</p>
  </div>
  <div style="background: var(--light-mint); border-radius: 10px; padding: 16px 20px; grid-column: 1 / -1;">
    <p style="margin: 0 0 4px 0; font-family: 'Montserrat', sans-serif; font-weight: 700; color: var(--teal); font-size: 0.75em; letter-spacing: 1px;">NO LEADING QUESTIONS</p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-size: 0.78em;">
      <p style="margin: 0;"><span style="color: #DC2626;">&#10007;</span> "What's frustrating about X?"</p>
      <p style="margin: 0;"><span style="color: var(--teal);">&#10003;</span> "How do you experience X?"</p>
    </div>
  </div>
</div>

---

## Choosing Your Subject

A <span class="orange">scenario</span> is a broad problem space. A <span class="orange">subject</span> is your team's specific investigation within it.

<div class="two-col" style="margin-top: 16px;">
<div>

<div class="callout-box" style="margin: 0;">

**Good subjects are:**
- Bounded: one organization, one location, or one population
- Accessible: you can reach real stakeholders
- Curious: you genuinely want to know the answer

</div>

</div>
<div>

<div style="font-size: 0.78em; line-height: 1.6;">

**Examples:**

<span class="orange">A</span> + "How do new nurses navigate their first rotation at a community hospital?"

<span class="orange">B</span> + "What operational workarounds do independent coffee shop owners rely on daily?"

<span class="orange">D</span> + "Why do eligible families in one school district not use the free tutoring program?"

</div>

</div>
</div>

Your team's combined geography, industries, and networks are your research advantage. Map them before you pick.

---

## Scoping Your Investigation

<div class="two-col">
<div>

<div class="callout-box" style="margin: 0; background: #FEF2F2; border-left-color: #EF4444;">

<p style="margin: 0 0 8px 0; color: #DC2626;"><strong>Too Broad</strong></p>

- "How do nonprofits work?"
- "What's wrong with healthcare?"
- "Why is onboarding broken?"

</div>

</div>
<div>

<div class="callout-box" style="margin: 0;">

<p style="margin: 0 0 8px 0; color: var(--teal);"><strong>Well-Scoped</strong></p>

- "How do new nurses navigate their first rotation at a community hospital?"
- "Why do eligible families in one district not use free tutoring?"
- "What workarounds do food truck owners use daily?"

</div>

</div>
</div>

**The test:** Can you name the specific person you'd interview? Can you get to them in two weeks? If yes, your scope is right.

---

## Team Work: Map What You Know

<div class="activity-box">
<p style="margin: 0 0 8px 0; font-size: 0.85em; opacity: 0.8;">PHASE 1 (15 min)</p>

1. What do you already know about this problem? Write it down.
2. What assumptions are you making? Be honest about what you're guessing.
3. Who are 4-5 potential stakeholders? Think beyond the obvious. Include at least one <span style="color: var(--orange);">extreme user</span>: someone at the edges of this system.

</div>

<div class="callout-box" style="margin-top: 12px;">
An extreme user experiences the problem at higher intensity or frequency than most. A daily bus rider, not an occasional one. A first-week employee, not a five-year veteran.
</div>

---

## Team Work: Map Your Reach

<div class="activity-box">
<p style="margin: 0 0 8px 0; font-size: 0.85em; opacity: 0.8;">PHASE 2 (15 min)</p>

Go around the team. Each person answers:

1. Where do you work? What organizations are you connected to?
2. What neighborhoods, cities, or communities do you move through?
3. Who could you realistically observe or interview in the next two weeks?

Build a combined map of your team's access. This is your research asset.

</div>

---

## Team Work: Scope Your Subject

<div class="activity-box">
<p style="margin: 0 0 8px 0; font-size: 0.85em; opacity: 0.8;">PHASE 3 (15 min)</p>

Write your subject in **one sentence**. Then run it through these tests:

1. **The Person Test:** Can you name the specific type of person you'd interview? If not, narrow it.
2. **The Two-Week Test:** Could your team investigate this in two weeks? If not, narrow it.
3. **The Access Test:** Can at least two team members reach relevant stakeholders from their own context? If not, pivot.

</div>

<div class="callout-box" style="margin-top: 12px;">
Read your one sentence aloud to another team. If they can't tell you who you'd talk to, it's too broad.
</div>

---

## Looking Ahead

- **A02: Problem Reflection** (individual) due Session 3 (400-600 words on your observation experience)
- **Session 3**: Thursday, March 12, 6:30-8:00 PM, online (Zoom)
- Focus: Stakeholder mapping and distributed research planning
- Exchange contact info with your team before you leave today

<div class="callout-box" style="margin-top: 16px;">
Between now and Session 3, keep your notebook active. Find the Duct Tape entries, observations from your daily context, questions about your scenario. The notebook is your research instrument.
</div>

---

## Design Abilities: Today's Progress

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px 28px; margin-top: 8px;">
  <div class="ability-active" style="padding: 10px 16px 12px;">
    <strong>Learn From Others</strong>
    <div style="font-weight: 400; font-size: 0.85em; margin-top: 4px; opacity: 0.85;">TETHER debrief, field trip observation, interview practice</div>
  </div>
  <div class="ability-active" style="padding: 10px 16px 12px;">
    <strong>Synthesize Information</strong>
    <div style="font-weight: 400; font-size: 0.85em; margin-top: 4px; opacity: 0.85;">Comparing notes, problem framing from observations</div>
  </div>
  <div class="ability-active" style="padding: 10px 16px 12px;">
    <strong>Move Between Concrete and Abstract</strong>
    <div style="font-weight: 400; font-size: 0.85em; margin-top: 4px; opacity: 0.85;">AEIOU framework, field trip debrief</div>
  </div>
  <div class="ability-active" style="padding: 10px 16px 12px;">
    <strong>Navigate Ambiguity</strong>
    <div style="font-weight: 400; font-size: 0.85em; margin-top: 4px; opacity: 0.85;">Team formation, scoping a problem you don't understand yet</div>
  </div>
  <div class="ability-inactive">Experiment Rapidly</div>
  <div class="ability-inactive">Build and Craft Intentionally</div>
  <div class="ability-inactive">Communicate Deliberately</div>
</div>

---

<!-- _class: closing -->

## Before You Go

<div class="reminder" style="display: block; margin-bottom: 20px;">
<span class="label">Find the Duct Tape:</span> Keep collecting workarounds this week.
</div>

- Make sure you have your team's contact info
- A02: Problem Reflection (individual): 400-600 words, due Session 3
- Session 3: Thursday, March 12, 6:30 PM, Zoom

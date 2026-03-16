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

  /* Silence box */
  .silence-box {
    background: #1E293B;
    color: #94A3B8;
    border-radius: 10px;
    padding: 24px 32px;
    margin: 20px 0;
    text-align: center;
    font-size: 0.82em;
    font-style: italic;
    letter-spacing: 1px;
  }

  /* TETHER letter styling */
  .tether-letter {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: var(--teal);
    font-size: 1.1em;
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

  .closing-footer {
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    color: var(--teal);
    font-size: 0.9em;
    margin-top: 30px;
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

<p class="pre-title">Session 1</p>

# Course Intro +<br>Navigate Ambiguity

<h2>Design Thinking for MBAs (Hybrid Section)</h2>

<p class="footer">Thursday, February 26, 2026 &ensp;|&ensp; 6:30 PM &ensp;|&ensp; Online (Zoom) &ensp;|&ensp; Faculty: Patrick Ray</p>

---

![bg contain](./about-career-path.png)

---

![bg contain](./about-tour-route.png)

---

![bg contain](./about-personal.png)

---

## Welcome

Welcome to MGMT 625, Section 002. This is a 6-session hybrid course in Design Thinking.

Let's get to know who's in the room.

<div class="chat-prompt">
<div class="chat-icon">DROP IN CHAT</div>
Your name, where you're located, and <span class="orange">one word</span> for how you feel about ambiguity.
</div>

<div class="callout-box">
"This section has people in different cities, different industries, different contexts. That's not a limitation of the hybrid format. It's the whole point."
</div>

---

## Why This Course

<div class="callout-box" style="font-size: 0.85em;">
Every one of you will face problems in your career where the case study doesn't exist yet. Where the data is ambiguous, the stakeholders disagree, and the "right answer" depends on questions nobody has thought to ask. This course gives you a structured process for those moments.
</div>

**What we're building over six sessions:**

<div style="display: flex; align-items: center; gap: 0; margin-top: 8px;">
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 16px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.72em; flex: 1;">Primary Research<br>Methods</div>
  <div style="color: var(--teal); font-size: 1.4em; padding: 0 6px;">&#8594;</div>
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 16px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.72em; flex: 1;">Systems<br>Modeling</div>
  <div style="color: var(--teal); font-size: 1.4em; padding: 0 6px;">&#8594;</div>
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 16px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.72em; flex: 1;">Problem<br>Definition</div>
  <div style="color: var(--teal); font-size: 1.4em; padding: 0 6px;">&#8594;</div>
  <div style="background: var(--teal); color: #fff; border-radius: 8px; padding: 12px 16px; text-align: center; font-family: 'Montserrat', sans-serif; font-weight: 600; font-size: 0.72em; flex: 1;">Hypothesis<br>Testing</div>
</div>

Each phase has specific analytical tools. Each deliverable asks you to show your reasoning.

---

## Seven Design Abilities

These aren't abstract concepts. They're professional competencies.

| Ability | When You'll Use It |
|---------|-------------------|
| **Navigate Ambiguity** | Leading a team through a reorg when nobody knows the new structure yet |
| **Learn From Others** | Entering a new market when your assumptions about the customer are wrong |
| **Synthesize Information** | 40 customer interviews, and you need the three patterns that matter |
| **Experiment Rapidly** | Your CEO wants a recommendation by Friday and you have three approaches |
| **Move Between Concrete & Abstract** | A frontline employee describes a workaround. You need to find the structural problem it reveals. |
| **Build & Craft Intentionally** | Rough concept for your board vs. polished deck for investors. Different resolution for different feedback. |
| **Communicate Deliberately** | Recommending a strategy where the reasoning matters as much as the answer |

---

## Course at a Glance

<div class="three-col">
<div>
<div class="phase-box">
  <div class="phase-label">Phase 1</div>
  <div class="phase-name">Empathy & Observation</div>
  <div class="phase-sessions">Sessions 1-2</div>
</div>
</div>
<div>
<div class="phase-box">
  <div class="phase-label">Phase 2</div>
  <div class="phase-name">Problem Definition</div>
  <div class="phase-sessions">Sessions 3-4</div>
</div>
</div>
<div>
<div class="phase-box">
  <div class="phase-label">Phase 3</div>
  <div class="phase-name">Ideation & Testing</div>
  <div class="phase-sessions">Sessions 5-6</div>
</div>
</div>
</div>

- **6 sessions**: 4 online (90 min) + 2 in-person (4.5 hrs)
- **2 projects**: Individual observation, then team design challenge
- **7 design abilities**: You'll experience all seven. We'll name them as we go.

---

## The Hybrid Advantage

<div class="two-col">
<div>

### Online Sessions
- Framing and synthesis
- Team coordination
- Research planning

</div>
<div>

### In-Person Sessions
- Hands-on activities
- Team formation
- Final presentations

</div>
</div>

- **Async fieldwork**: Research conducted in YOUR environments (workplaces, neighborhoods, cities)

<div class="callout-box">
"In a traditional class, everyone observes the same campus coffee shop. In this class, you'll observe your own workplaces, neighborhoods, and cities. That diversity is what makes the research richer."
</div>

---

## How This Course Works

<div class="two-col">
<div>

### Grading
- **Specs-based**: Credit for meeting specifications
- Attendance & Participation: 25%
- Individual Assignments: 35%
- Team Assignments: 40%

</div>
<div>

### Tokens
- 6 tokens total
- 3 for 24-hour extensions
- 3 for revisions
- Teams get 3 revision tokens

</div>
</div>

**Your notebook** (physical or digital) goes with you the entire course. Start using it tonight.

---

## Six Sessions

| # | Date | Format | Focus |
|---|------|--------|-------|
| **1** | Thu, Feb 26 | <span class="orange">Online</span> | Course Intro + Navigate Ambiguity |
| **2** | Sat, Mar 7 | In-Person | Observation Debrief + Team Formation |
| **3** | Thu, Mar 12 | <span class="orange">Online</span> | Stakeholder Mapping + Research Planning |
| **4** | Thu, Mar 26 | <span class="orange">Online</span> | Research Synthesis + Problem Definition |
| **5** | Sat, Apr 4 | In-Person | Final Presentations + Stress Testing |
| **6** | Thu, Apr 9 | <span class="orange">Online</span> | Reflection + Course Close |

Two-week research gap between Sessions 3 and 4 is intentional. That's when your team does distributed fieldwork.

---

## Let's Try Something

<div class="activity-box">

I'm going to show you **three short videos**.

Your only job is to **watch** and **write** in your notebook.

No other instructions.

</div>

Have your notebook ready. Pen or keyboard, your choice.

---

<div class="video-label">Video 1</div>

## Watch. Write.

Observe what you see. Write what you notice.

<a href="https://www.youtube.com/watch?v=hZ1OgQL9_Cw&t=90" target="_blank" style="display: flex; height: 280px; background: #0F172A; border-radius: 12px; align-items: center; justify-content: center; text-decoration: none; cursor: pointer;">
  <div style="text-align: center;">
    <div style="width: 68px; height: 48px; background: #FF0000; border-radius: 12px; margin: 0 auto 16px; display: flex; align-items: center; justify-content: center;">
      <div style="width: 0; height: 0; border-top: 10px solid transparent; border-bottom: 10px solid transparent; border-left: 18px solid #fff; margin-left: 4px;"></div>
    </div>
    <p style="color: #94A3B8; font-size: 0.75em; margin: 0;">Click to play: NYC 1910s (~4 min excerpt)</p>
  </div>
</a>

---

<div class="chat-prompt" style="margin-top: 120px;">
<div class="chat-icon">DROP IN CHAT</div>
One word for what you just experienced.
</div>

---

<div class="video-label">Video 2</div>

## Watch. Write.

Keep observing. Keep writing.

<a href="https://www.youtube.com/watch?v=CYPwPA08KE4" target="_blank" style="display: flex; height: 280px; background: #0F172A; border-radius: 12px; align-items: center; justify-content: center; text-decoration: none; cursor: pointer;">
  <div style="text-align: center;">
    <div style="width: 68px; height: 48px; background: #FF0000; border-radius: 12px; margin: 0 auto 16px; display: flex; align-items: center; justify-content: center;">
      <div style="width: 0; height: 0; border-top: 10px solid transparent; border-bottom: 10px solid transparent; border-left: 18px solid #fff; margin-left: 4px;"></div>
    </div>
    <p style="color: #94A3B8; font-size: 0.75em; margin: 0;">Click to play: Tokyo Shibuya, Rambalac (~3 min excerpt)</p>
  </div>
</a>

---

<div class="chat-prompt" style="margin-top: 120px;">
<div class="chat-icon">DROP IN CHAT</div>
One word for what you just experienced.
</div>

---

<div class="video-label">Video 3</div>

## Watch. Write.

Last one. Watch closely.

<a href="https://vimeo.com/467675747" target="_blank" style="display: flex; height: 280px; background: #0F172A; border-radius: 12px; align-items: center; justify-content: center; text-decoration: none; cursor: pointer;">
  <div style="text-align: center;">
    <div style="width: 68px; height: 48px; background: #1AB7EA; border-radius: 12px; margin: 0 auto 16px; display: flex; align-items: center; justify-content: center;">
      <div style="width: 0; height: 0; border-top: 10px solid transparent; border-bottom: 10px solid transparent; border-left: 18px solid #fff; margin-left: 4px;"></div>
    </div>
    <p style="color: #94A3B8; font-size: 0.75em; margin: 0;">Click to play: Stainless, Dadar (Adam Magyar, ~2 min excerpt)</p>
  </div>
</a>

---

<div class="silence-box" style="margin-top: 140px;">
<p style="margin: 0 0 16px 0; font-size: 1.1em; color: #ffffff; font-style: normal;">Two minutes of silent writing.</p>
<p style="margin: 0; font-size: 0.9em; color: #CBD5E1;">Write whatever is in your head. Don't filter it.</p>
</div>

---

<!-- _class: transition -->

# Make Sense of It

---

## Make Sense of It

- What did you <span class="orange">not know</span> while watching?
- When did you start **making up stories** or explanations?
- What was it like to keep watching **without understanding**?
- Did your strategy <span class="orange">change</span> from video 1 to video 3?
- Where did certainty creep in, and **was it real**?

---

## Navigate Ambiguity

<div class="callout-box" style="font-size: 0.85em;">
What you just experienced is <strong>Navigate Ambiguity</strong>. Sitting with incomplete information and resisting the urge to resolve it prematurely. That's the first of seven design abilities, and it's the hardest one.
</div>

<div class="two-col" style="margin-top: 20px;">
<div>

### In Your Career
- **Consulting**: Diagnosing the real problem vs. confirming your first hypothesis
- **Leadership**: Reacting to symptoms vs. understanding the system

</div>
<div>

### In This Course
- **TETHER**: Watching without interpreting
- **Research**: Gathering data before defining the problem
- **Problem definition**: Resisting premature solutions

</div>
</div>

<div class="chat-prompt" style="margin-top: 16px;">
<div class="chat-icon">THINK ABOUT THIS</div>
Where in your work do you feel pressure to have the answer immediately?
</div>

---

## Your First Assignment

<p style="font-size: 1.1em; color: var(--navy); margin-bottom: 16px;">
  <span class="tether-letter">T</span>ake
  <span class="tether-letter">E</span>xtended
  <span class="tether-letter">T</span>ime to
  <span class="tether-letter">H</span>old
  <span class="tether-letter">E</span>verything in
  <span class="tether-letter">R</span>eview
</p>

- **90 minutes** of uninterrupted observation in YOUR environment
- Choose a place where people interact with systems, spaces, or each other
- Notebook and pen only. No laptop. Phone on silent and away.
- Document what you <span class="orange">see</span>, not what you <span class="orange">think it means</span>
- Write a half-page reflection after

---

## Where Will You Observe?

<div class="two-col">
<div>

### Good Locations
- Your workplace lobby or common area
- A local coffee shop
- Public transit
- A grocery store
- Your neighborhood park

</div>
<div>

### What Makes It Work
- People interacting with systems or spaces
- Enough activity to watch for 90 minutes
- A place you can sit without drawing attention
- Somewhere in YOUR context, not on campus

</div>
</div>

<div class="callout-box">
"Your observation location is unique to you. When we come together in Session 2, we'll have observations from completely different worlds. That's data no single-campus class can match."
</div>

---

## Find the Duct Tape

One more ongoing practice that runs the entire course.

<div class="activity-box">

Each week, identify one **"duct tape" solution** you encounter in the wild: a workaround, an improvised fix, a hack someone uses because the real solution doesn't exist.

Document it in your notebook:

1. What is the workaround?
2. What problem does it solve?
3. Why doesn't the real fix exist?

</div>

<div class="callout-box">
Over the course, your collection will start to show patterns about how systems fail and how people adapt. That's design thinking in action.
</div>

---

<!-- _class: closing -->

## What's Next

- Complete your **TETHER observation** before Session 2
- **Session 2**: Saturday, March 7, 8:00 AM to 12:30 PM
- In-person at **McNair Hall 216**
- Bring your notebook with completed TETHER

Start thinking about where you'll do your TETHER. The location matters.

<div class="closing-footer">See you March 7.</div>

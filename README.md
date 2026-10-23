# Claude Cold Email Skill: Sales Psychology for Cold Emails

A **Claude Code skill** that writes **cold email** with **sales psychology**, so your **copywriting** feels written for one person and your **B2B outbound** earns more replies. It was built by studying 75 public template libraries, guides and real example emails, then turning the patterns behind them into rules Claude can apply to your prospect.

<p align="center">
  <a href="https://github.com/hamzamunyr/claude-cold-email-skill/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/hamzamunyr/claude-cold-email-skill?style=for-the-badge&color=f5c542"></a>
  <img alt="License MIT" src="https://img.shields.io/badge/license-MIT-2ea44f?style=for-the-badge">
  <img alt="Claude Code skill" src="https://img.shields.io/badge/Claude%20Code-skill-8a63d2?style=for-the-badge">
  <img alt="Works as a plugin" src="https://img.shields.io/badge/install-plugin%20or%20skill-0969da?style=for-the-badge">
</p>

<p align="center">
  <img alt="75 sources" src="https://img.shields.io/badge/sources%20studied-75-1f6feb">
  <img alt="Emails analyzed" src="https://img.shields.io/badge/emails%20analyzed-1600%2B-1f6feb">
  <img alt="Principles" src="https://img.shields.io/badge/psychology%20principles-40%2B-1f6feb">
  <img alt="Frameworks" src="https://img.shields.io/badge/email%20frameworks-100%2B-1f6feb">
  <img alt="Checklist" src="https://img.shields.io/badge/checklist%20items-55%2B-1f6feb">
</p>

<p align="center">
  <a href="#-see-it-in-action">Demo</a> ·
  <a href="#-install">Install</a> ·
  <a href="#-how-to-use">How to use</a> ·
  <a href="#-the-psychology-toolkit">Principles</a> ·
  <a href="#-pick-your-angle">Pick your angle</a> ·
  <a href="#-before-and-after">Before and after</a> ·
  <a href="#-where-the-patterns-come-from">Sources</a>
</p>

---

## 👀 See it in action

**You type:**

```text
Write a cold email to the operations manager at a 50 person company.
I sell software that cuts manual reporting. Goal: a 15 minute call.
```

**Claude replies:**

```text
Subject options
1. reporting at [Company]
2. your open analyst role
3. quick question on reporting

Hi [First name],

I saw [Company] is hiring a reporting analyst, which usually means
the weekly numbers are still being pulled together by hand.

We automate that report so your team gets it without the manual work.
[Similar company] [real result] in [timeframe] after switching.

Would a 15 minute walkthrough be useful?

[Your name]

Why this works
Specificity (a real job post), a clear cost of the status quo,
social proof (a similar company) and a tiny ask (a short walkthrough).
```

> The skill asks for anything missing first (who the prospect is, your offer, the goal), then writes an original email and runs it through a checklist before showing it. Brackets mark facts only you can supply. It never invents names, stats or results.

---

## ✨ What it does

- 🎯 **Asks for what it needs.** Prospect, offer and goal, before it writes a word.
- 🧠 **Picks 2 to 3 psychology principles** that fit this prospect, from a ranked library.
- ✍️ **Writes an original email.** It never copies a template.
- ✅ **Runs a checklist** and fixes weak lines before you see the email.
- 📨 **Gives you 2 to 3 subject lines** and a short note on which principles it used and why.
- 🚫 **Keeps it honest.** No fake claims, no fake names, no made-up stats.

```mermaid
flowchart LR
    A[Prospect, offer, goal] --> B{Anything missing?}
    B -- yes --> C[Skill asks you]
    C --> D[Pick 2 to 3 principles]
    B -- no --> D
    D --> E[Write an original email]
    E --> F[Run the checklist]
    F --> G[Email plus subjects plus a short why note]
```

---

## 🧪 Why psychology beats templates

A template is a shape. A prospect replies to a **reason**.

| Template thinking | Psychology thinking |
| --- | --- |
| "Which template fits?" | "Why would this person care today?" |
| Fill in the name and company | Use one real detail only they would recognize |
| Ask for a meeting | Ask for the smallest next step |
| Add proof when you can | Pick the proof that matches their doubt |
| Hope it feels personal | Check every line against a rule |

Across the sources behind this skill, the same few ideas win again and again: **be short, be specific, ask for little, give something first, and never pretend.**

---

## 📦 Install

<details open>
<summary><b>Option A: as a Claude Code plugin (recommended)</b></summary>

```text
/plugin marketplace add hamzamunyr/claude-cold-email-skill
/plugin install cold-email-psychology@claude-cold-email-skill
```

</details>

<details>
<summary><b>Option B: copy the skill folder by hand</b></summary>

1. Clone or download this repo.
2. Copy `skills/cold-email-psychology` into your skills folder:

```bash
# macOS and Linux
cp -r skills/cold-email-psychology ~/.claude/skills/

# Windows (PowerShell)
Copy-Item -Recurse skills\cold-email-psychology $env:USERPROFILE\.claude\skills\
```

3. Restart Claude Code, or run `/reload-skills`.

</details>

<details>
<summary><b>Check that it works</b></summary>

Ask Claude: *"What skills do you have for cold email?"* You should see `cold-email-psychology` listed.

</details>

---

## 🚀 How to use

Just talk to Claude Code. The skill triggers on requests like these:

```text
Write a cold email to [role] at [type of company]. I sell [offer]. Goal: [meeting / reply / demo].
```

```text
Write a 3 email follow-up sequence for a prospect who went quiet.
```

```text
Improve this cold email: [paste it]
```

```text
Give me 10 subject line options for [offer] aimed at [role].
```

**Tip:** the more real detail you give (a job post, a launch, a post they wrote), the better the email.

---

## 🧠 The psychology toolkit

These are the most common patterns across the emails studied. The full list, with how to apply each one, is in [`principles.md`](skills/cold-email-psychology/references/principles.md).

| # | Principle | In plain English | Where it shows up |
| --- | --- | --- | --- |
| 1 | **Keep it short** | One idea per sentence, readable in 20 seconds | Almost every strong email |
| 2 | **Small first ask** | A 10 minute call or a one line reply, not a 30 minute demo | Hundreds of emails |
| 3 | **Specificity** | One real detail proves it was not blasted | Triggers, posts, job ads, site findings |
| 4 | **Social proof** | A similar company and a real result | Case study and peer emails |
| 5 | **Reciprocity** | Give something useful before you ask | Audits, drafts, short videos, resources |
| 6 | **Consistency** | Refer to your last note so it feels like one conversation | Follow-ups and break-ups |
| 7 | **Curiosity gap** | Hint at the idea without giving it all away | Subject lines and idea offers |
| 8 | **Easy exit** | Make it safe to say no or point you elsewhere | Right-person and break-up emails |
| 9 | **Quantified benefit** | A believable number makes the gain concrete | Result lines |
| 10 | **Lighter ask** | Offer an email answer or one question instead of a call | Busy and senior prospects |

<details>
<summary><b>More principles in the library (click to open)</b></summary>

Empathy, problem agitation, borrowed trust (a mutual contact), competitive comparison, forced choice (two time options), normalization ("many teams like yours"), risk reversal, objection pre-emption, custom calculation, show the work, mutual benefit, exclusivity, humor, and more. Each has a "how to apply" note and a "when not to use it" warning.

</details>

---

## 🧭 Pick your angle

Not sure which principle to lead with? Follow the branch.

```mermaid
flowchart TD
    S[What do you have on the prospect?] --> T{A real trigger or detail?}
    T -- yes --> P1[Lead with specificity]
    T -- no --> U{A result from a similar customer?}
    U -- yes --> P2[Lead with social proof]
    U -- no --> V{Something useful to give away?}
    V -- yes --> P3[Lead with reciprocity]
    V -- no --> P4[Ask a genuine question with a lighter ask]
```

---

## 🔁 Before and after

Illustrative drafts that show the difference. Open one.

<details>
<summary><b>Selling a product or service to a business</b></summary>

**Before**

```text
Subject: Revolutionary solution for your business

Hi there, I hope this email finds you well. I'm the CEO of [Company],
the leading platform with powerful features. We help businesses grow.
Do you have 30 minutes for a demo this week?
```

**After**

```text
Subject: [Company] and [specific problem]

Hi [First name],

I saw [one real, specific thing about their company]. That usually
means [the problem it causes].

[Similar company] [real result] in [timeframe] with our help.
Would a 15 minute walkthrough be useful?
```

**Why:** specificity, one proof point, and a smaller ask.

</details>

<details>
<summary><b>Freelancer or agency pitching a new client</b></summary>

**Before**

```text
Subject: Grow your business with us

We are a full service agency with 15 years of experience. We would
love to hop on a call to discuss how we can help you.
```

**After**

```text
Subject: [Company]'s [page or channel], one idea

Hi [First name],

I looked at [Company]'s [website, page or campaign] and noticed
[one specific, real finding]. I wrote up a short list of what I'd
change. Want me to send it over?
```

**Why:** a real finding, free value first, and a yes-or-no ask.

</details>

<details>
<summary><b>Following up when nobody replied</b></summary>

**Before**

```text
Subject: Following up

Just checking in to see if you saw my last email. Let me know.
```

**After**

```text
Subject: re: reporting at [Company]

Hi [First name],

One more thought: [a new fact, result or resource that was not in
the first email]. If now is not the right time, tell me and I will
stop here. Otherwise, would a short call next week help?
```

**Why:** adds something new, gives an easy way out, and asks for little.

</details>

---

## 🌍 Where the patterns come from

The skill is built on **75 public sources**: template libraries, vendor guides and real example emails. A few of the biggest:

| Source | What it added | Breakdown |
| --- | --- | --- |
| **Hunter** | A 510 template library. Showed how a curated set beats a crowd-sourced one, and the power of the "lighter ask" | [Read](breakdowns/015-hunter.md) |
| **Woodpecker** | 75 templates across sales, recruiting, real estate and follow-ups | [Read](breakdowns/004-woodpecker.md) |
| **HubSpot** | 22 B2B templates. Multiple-choice break-ups, custom ROI math, objection pre-emption | [Read](breakdowns/013-hubspot.md) |
| **SmartWriter** | Annotated good and bad emails side by side | [Read](breakdowns/009-smartwriter.md) |
| **Smartlead** | 19 emails and four variables that make personalization real | [Read](breakdowns/008-smartlead.md) |
| **Proposify** | Real example emails, including a custom video of the prospect's own site | [Read](breakdowns/014-proposify.md) |

Every source has its own write-up in [`breakdowns/`](breakdowns/), with what worked, what did not, and an honest note when no results were published. Where a source gave no reply rates, this repo says **"not provided"** and never fills the gap.

### What is inside

| Folder | What you get |
| --- | --- |
| [`skills/cold-email-psychology/`](skills/cold-email-psychology/) | The skill itself |
| [`references/principles.md`](skills/cold-email-psychology/references/principles.md) | 40+ principles with counts and how to apply each |
| [`references/frameworks.md`](skills/cold-email-psychology/references/frameworks.md) | 100+ email structures |
| [`references/hooks.md`](skills/cold-email-psychology/references/hooks.md) | Opening lines and subject line patterns |
| [`references/ctas.md`](skills/cold-email-psychology/references/ctas.md) | Types of asks and when each works |
| [`references/examples.md`](skills/cold-email-psychology/references/examples.md) | 53 original example emails |
| [`references/checklist.md`](skills/cold-email-psychology/references/checklist.md) | A pre-send checklist the skill runs on every draft |
| [`references/practices.md`](skills/cold-email-psychology/references/practices.md) | Writing, follow-up, list and deliverability practices from 8 guides |
| [`references/followups.md`](skills/cold-email-psychology/references/followups.md) | How many follow-ups, timing, what each touch does, phrases to avoid |
| [`breakdowns/`](breakdowns/) | One analysis per source |

---

## 🤝 Contributing

Found a great cold email source, a pattern that is missing, or a line the checklist should catch? Open an issue or a pull request.

- [ ] Share a source with its link and a note on what is useful
- [ ] Suggest a principle, hook or checklist item
- [ ] Report an email the skill wrote that felt generic or pushy

**Rules for contributions:** analysis and paraphrase only, never paste a source's email body into a public file, and never invent results.

---

## ⚖️ Use it responsibly

Cold email is regulated. Follow the rules where you send (for example CAN-SPAM and GDPR), include a clear sender identity and an opt-out, and only write to people you have a real reason to contact.

---

## 📄 License

[MIT](LICENSE). Use it, change it, share it.

---

## ⭐ If this helped

If this skill saved you time or got you a reply, please consider giving the repo a star. It helps other people find it.

## 👤 Author

**Built by Hamza Munir, software engineer and GTM engineer.** More at [thepixelserve.com](https://thepixelserve.com).

[![Website](https://img.shields.io/badge/Website-thepixelserve.com-0969da?style=flat-square)](https://thepixelserve.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-hamzamunyr-0a66c2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hamzamunyr/)

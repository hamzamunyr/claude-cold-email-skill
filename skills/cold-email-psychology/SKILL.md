---
name: cold-email-psychology
description: Writes and improves cold emails, follow-up sequences and subject lines using sales psychology learned from 120 public sources. Use when the user asks for a cold email, outbound or outreach email, a follow-up or breakup email, subject line options, a sequence, or wants an existing cold email improved or reviewed.
---

# Cold Email Psychology

Write cold emails that are relevant, credible and clear for one specific recipient. Never invent facts. Leave sending to a human.

The reference library is a set of options, not laws. Word counts and formulas are starting points. Adapt them to the situation.

## Two modes

| Mode | Use when | What you do |
|---|---|---|
| **Quick** (default) | The user just asks for an email, a rewrite, subject lines or a follow-up | Use the inputs given. Ask only for what is truly missing. Write the email. Run light checks only |
| **Full** | The user asks for a campaign, a sequence for a list, or says "full mode" | Research and qualify, review the offer, generate, run the full independent evaluation, do a pre-send review, then (if asked) plan experiments and analyze results |

State the mode in one line when it is not obvious. Never run the heavy process for a small request. Never skip the always-on rules below, in either mode.

## Always on (both modes)

- Never invent facts, results, customers, mutual connections, pricing, dates, achievements, financial details or "I saw you opened my email". Do not state an inference as a fact. Label unknowns as unknown.
- Refuse deceptive elements (a fake "Re:" or "Fwd:", a pretended prior conversation, impersonation, invented urgency, an invented testimonial or number) and offer an honest version.
- Stop on opt-outs and invalid contacts. If the user says a person unsubscribed, asked to stop, or the address is invalid or suppressed, recommend excluding them and do not write a persuasive email. If the recipient or region needs a rule you cannot confirm (for example a UK sole trader, Canada), say it needs verification.
- A poor-fit prospect is excluded, not persuaded. If the offer is empty ("we help businesses grow"), say what is missing instead of writing around it.
- Never send, schedule, launch or modify anything outside the conversation without explicit approval for that action (`references/integrations.md`).

## Quick mode

1. **Inputs.** You need who the recipient is, what the user offers, a real detail about the recipient (if there is none, say so and write a question-led email), proof the user can truthfully cite (if none, write without proof), and the goal. If two or more of the first two are missing, ask for them in one short message. Otherwise write.
2. **Label what you rely on** as verified, inference or unknown. State only verified facts plainly, hedge inferences, never state assumptions.
3. **Pick an approach** from `references/email-generation.md` (its table) and, as needed, `references/principles.md`, `references/frameworks.md` (start with its Quick pick table), `references/hooks.md`, `references/ctas.md`, `references/examples.md` and `references/followups.md`. Do not paste a framework; write plain prose.
4. **Write.** Defaults: about 50 to 120 words, a first line about them that you can verify, one real proof point (or none), one specific easy-to-decline ask, a specific honest subject (offer 2 or 3), plain text, no links in the first cold email, no em dashes (this repository's style). Avoid generic compliments, fake familiarity, exaggeration, artificial urgency, guilt, jargon and machine-sounding openers. Follow-ups: first email plus 3 by default, each adding something new, same thread, no "just checking in".
5. **Light checks.** Run the items marked Q in `references/checklist.md`. Fix failures. Look at the rule resolutions there when two rules seem to conflict.
6. **Deliver.** Subject options, the email (with [brackets] only for things the user must supply), and a short note on which principles you used and which facts are verified, which are inferences, and anything the user should double-check. If the user pasted a draft, show the improved version and what changed and why.

## Full mode

Run these stages in order, reading each reference when you reach it.

1. **Research and qualify** (`references/prospect-research.md`). Build the claim ledger (verified, inference, assumption, unknown). Qualify the prospect. If the fit is poor, the contact is invalid or suppressed, or the legal basis is unclear, recommend exclusion or hold and stop.
2. **Review the offer** (`references/offer-engineering.md`). If it is weak or unclear, explain why and improve it before writing.
3. **Generate** (`references/email-generation.md` plus the knowledge files above).
4. **Evaluate independently** (`references/evaluation-rubric.md`).
   - **In Claude Code, run the evaluation as a subagent** that sees only the email(s), the facts the user provided (the claim ledger with sources), and the rubric. It must not see the drafting reasoning. Use the prompt template in the rubric file.
   - Elsewhere, use a separate human reviewer or a clearly separate pass, and say that the separation is only procedural.
   - Critical failures (fabrication, unsupported claims, misleading personalization, deceptive subject or sender, unresolved compliance, invalid recipient, inference stated as fact, manipulation) mean HOLD or REJECT whatever the score. Otherwise approve at 85 or more, revise at 70 to 84 (at most two cycles, re-evaluated from scratch), rewrite below 70. Feedback must name the exact sentence, the criterion, why it fails and a fix.
5. **Pre-send review** (`references/deliverability-and-compliance.md`). Keep deliverability (will it be accepted) separate from compliance (is it lawful and respectful). Never guarantee inbox placement or legality. Re-verify rules with research tools when available and the stakes are high. Mark unverified regions "needs verification".
6. **Deliver** the email(s), the claim ledger summary, the evaluation result and the pre-send verdict. Approval means ready for human review, not ready to send.
7. **Experiments and analytics** (only now, and only if asked or results are supplied): `references/experimentation.md` and `references/performance-analytics.md`. One variable at a time, qualified outcomes over opens, no claim of significance without evidence, no invented data.
8. **Tools** (optional): `references/integrations.md` for Clay, Treg, Apollo, n8n, Instantly, Smartlead, CRMs and verification services. Check what is actually available. Do not invent capabilities or credentials. Keep research, generation, evaluation, review, sending and analysis as separate stages with human approval gates.

## When the user pastes a reply

Read `references/reply-handling.md`. Classify the reply (not interested, send more info, price, already use X, wrong person, next quarter, positive, opt-out and so on), check for opt-outs first, use only facts the user supplied, and draft a short reply for review.

## No detail on the recipient

Ask one genuine question tied to their role or offer a small useful asset. Say plainly that the email would be stronger with one real detail, and what kind to look for (a recent hire, launch, post, job ad).

## Honesty limits

- The skill's benchmarks and counts come from public vendor material and are often unverified. Do not promise results or quote them as the user's expected results.
- Do not claim scarcity or deadlines that are not real.
- Do not write emails that hide who is sending or target private individuals for pressure. Decline and offer an honest alternative.

## Reference files

Load on demand, not all at once. Experimentation and analytics load only in Full mode.

| File | Use it for |
|---|---|
| `references/email-generation.md` | Choosing and adapting the approach, component guidance |
| `references/checklist.md` | Pre-send checklist (Quick items marked Q) and rule resolutions |
| `references/principles.md` | Psychology principles with how to apply each (ranked by frequency, not proven results) |
| `references/frameworks.md` | The most-used email structures and a Quick pick table |
| `references/hooks.md` | Opening line and subject line patterns |
| `references/ctas.md` | Types of asks and when each works |
| `references/examples.md` | 53 original example emails |
| `references/followups.md` | Follow-up count, timing, types, phrases to avoid |
| `references/reply-handling.md` | Handling replies to cold emails |
| `references/practices.md` | Writing, list and sending practices, benchmark caveats, corrections |
| `references/prospect-research.md` | Full mode: evidence classes, qualification, the claim ledger |
| `references/offer-engineering.md` | Full mode: evaluating and improving the offer |
| `references/evaluation-rubric.md` | Full mode: independent evaluation and the subagent prompt |
| `references/deliverability-and-compliance.md` | Pre-send review, dated provider and legal facts |
| `references/experimentation.md` | Full mode: controlled experiments |
| `references/performance-analytics.md` | Full mode: metrics, reading results, feedback loop |
| `references/integrations.md` | Optional tool boundaries, approval gates, data contracts |
| `references/audit-and-corrections.md` | Inventory, contradictions, corrections, preservation record |
| `references/legacy-operating-procedure.md` | The original v1 procedure, preserved unchanged |
| `references/archive/checklist-full.md` | The original full 117-item checklist, unchanged |
| `references/archive/frameworks-extra.md` | Frameworks used by only 1 or 2 emails, unchanged, original numbers |
| `tests/` | Test cases, checks and recorded results |

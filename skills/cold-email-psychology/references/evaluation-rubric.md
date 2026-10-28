# Independent Email Evaluation and Factual Verification

Generation must not approve its own output. Run this as a separate pass with a reviewer mindset. A high score never overrides a critical failure.

## 1. Independence rules

- The evaluator receives only: the draft email(s), the facts the user provided (the claim ledger with sources, prospect-research.md), the offer verdict where one exists (offer-engineering.md) and the user's stated goal, plus this rubric. It does not receive the generator's reasoning or justifications.
- **In Claude Code, Full mode runs the evaluation as a subagent** (the Agent tool) with exactly that input. See the prompt template in section 9.
- The evaluator tries to find reasons to reject, not to approve.
- Where the environment allows (Claude Code subagents, a second model, a human reviewer), run the evaluation in a separate context. Inside a single conversation the separation is procedural only; say so, and do not overstate the independence.
- The generator may revise, but a revised draft must be re-evaluated from scratch.

## 2. Critical failures (automatic hold or rejection)

Any one of these blocks the email, regardless of score. Mark the exact sentence.

| Code | Failure | Examples |
|---|---|---|
| F1 | Fabricated factual claim about the prospect or their company | An invented hire, funding round, quote, post, award, problem or buying intent |
| F2 | Unsupported testimonial, customer result or performance claim | A percentage, revenue figure or named customer the user has not supplied and cannot substantiate |
| F3 | Materially misleading personalization | Implying a relationship, a conversation, a referral, a watched action ("saw you opened") or familiarity that does not exist; a merge field that asserts something untrue |
| F4 | Deceptive sender, subject or header | Fake Re: or Fwd:, pretending to be someone else, misleading subject for the content |
| F5 | Unresolved compliance issue | No lawful basis in the recipient's region, missing opt-out or sender identity where required, emailing a suppressed or opted-out contact (see deliverability-and-compliance.md) |
| F6 | Invalid or prohibited recipient | Invalid or unverified-risky address, role-address trap risk, suppressed contact, wrong person known to be unsuitable |
| F7 | Inference stated as fact | A class I or A claim written as an assertion |
| F8 | Manipulation | Fake urgency or scarcity, guilt, threats, exploiting a personal circumstance, sexual or discriminatory content |

A critical failure outcome is `HOLD` (fixable, for example remove the claim) or `REJECT` (the target or approach is unsuitable). State which and why.

## 3. Weighted rubric (100 points)

Score each criterion with the anchors. Use whole numbers. If unsure between two anchors, take the lower.

| Criterion | Weight | Full marks when | Zero to low when |
|---|---|---|---|
| Factual accuracy | 20 | Every statement about the prospect, offer and proof traces to a V claim or is a hedged I; no unsupported numbers | Any claim lacks a source (this also triggers F1, F2 or F7) |
| Prospect relevance | 12 | The email is about something this person or company actually has or does, and the offer fits the verified situation | Generic message that could go to anyone in the segment |
| Offer strength | 12 | The outcome is clear, credible, specific and matches the offer verdict | Vague benefit, feature list, unsupported promise |
| Personalization quality | 12 | One relevant detail that passes the swap test and traces to a V claim; not creepy | Mail-merge only, flattery, or a detail unrelated to the offer |
| Clarity | 10 | The reader understands who is writing, why, and what is asked within the first few lines | Buried purpose, jargon, ambiguity |
| Credibility | 8 | Proof is real and proportionate; tone is honest and measured | Hype, superlatives, claims out of proportion to evidence |
| CTA quality | 8 | One ask, proportionate to the relationship, easy to say yes or no to | Multiple asks, high-friction ask, vague "let me know" |
| Natural tone | 8 | Sounds like a person; varied rhythm; no machine-written phrasing (email-generation.md section 4) | Template language, stacked hype, stock openers |
| Conciseness | 6 | Every sentence earns its place; length fits the content | Padding, repetition, a wall of text |
| Compliance considerations | 4 | Identity and opt-out handled in line with the region; no disguised sender; list status clean | Missing basics (also see F5) |

Total possible: 100.

## 4. Thresholds and actions

| Result | Action |
|---|---|
| Any critical failure | HOLD or REJECT. Do not deliver the email as ready to send. Show the failing sentence and the fix. |
| 85 to 100, no critical failure | APPROVE for human review. |
| 70 to 84, no critical failure | REVISE. Fix every flagged item, then re-evaluate from scratch. Maximum two revision cycles. |
| Below 70 | REWRITE or go back a stage (research, offer). Do not polish a draft built on a weak foundation. |
| Still below 85 after two revision cycles | Stop revising. Deliver the best version marked "not approved", list the remaining findings, and say which need information only the user can supply. (Added after test TC01, which reached 81 after two cycles.) |
| Missing ledger or offer verdict | Cannot evaluate factual accuracy. HOLD and request them. |
| Low relevance or personalization caused only by missing input (no verified signal exists) | Report `limited_by_input`. Do not keep revising; deliver the honest generic draft clearly labeled as generic, with the list of information that would raise the score. A generic draft must still have no critical failure. (Added after test TC03 showed the thresholds had no rule for this case.) |

Approval means the draft is ready for the user to review, not that it should be sent. Sending is a human decision (integrations.md).

## 5. Required feedback format

Every deduction and every failure must name the exact text and give an actionable fix. Vague feedback such as "make it more compelling" is not acceptable.

| Sentence or claim (quote it) | Criterion or failure code | Why it fails | Concrete fix |
|---|---|---|---|
| "We helped teams like yours grow revenue 40%." | F2, Factual accuracy | No evidence supplied for 40% or for "teams like yours" | Remove the number, or replace with a result you can show: "A 60-person team cut month-end close from six days to three" if confirmed |
| "Saw you opened my last email." | F3 | Claims to know a tracked behavior; creepy and unreliable | Delete it; add a new fact instead |
| "Your recent growth must be a challenge." | F7 | Inference stated as fact | Hedge and tie it: "Teams that add a second office often find month-end gets longer" |

## 6. Factual verification checklist

Run before scoring. For each claim in the draft:

1. Is it in the claim ledger? If not, it is unsourced (A or U). Remove it or turn it into a question.
2. Is its class V and is the source dated and recent enough for the wording used ("recently", "this month")?
3. If it is a number, is the metric defined (what, over what period, for whom) and does the user have it on record?
4. If it names a person, company or customer, did the user confirm it is accurate and permitted?
5. If it mentions an action by the recipient (a post, a launch), can it be checked at a URL?
6. Does the sentence assert more than the source supports?

Record the result as `claims_checked` in the evaluation output.

## 7. Output of this stage (data contract)

```json
{
  "scores": {"factual_accuracy": 0, "prospect_relevance": 0, "offer_strength": 0, "personalization": 0, "clarity": 0, "credibility": 0, "cta": 0, "tone": 0, "conciseness": 0, "compliance": 0},
  "total": 0,
  "critical_failures": [{"code": "F2", "sentence": "", "why": "", "fix": ""}],
  "findings": [{"sentence": "", "criterion": "", "why": "", "fix": ""}],
  "claims_checked": [{"ledger_id": "C1", "ok": true, "note": ""}],
  "decision": "approve|revise|rewrite|hold|reject",
  "revision_cycle": 0
}
```

## 8. Limitations

- A rubric score measures conformance to this skill's criteria. It does not predict replies.
- Scores involve judgment. Anchors reduce, but do not remove, subjectivity.
- Procedural independence inside one model is weaker than a separate reviewer. Prefer a human or separate agent for high-stakes campaigns.

## 9. Subagent prompt template (Claude Code, Full mode)

Give the subagent only this, filled in. Do not add drafting notes or justifications.

```text
You are an independent reviewer of a cold email. Try to find reasons to reject it.

Facts provided by the user (claim ledger; class V = verified, I = inference, A = assumption, U = unknown):
<ledger table>

Offer verdict and goal:
<offer summary and goal, if any>

Email to review:
<subject options and body>

Rubric: apply references/evaluation-rubric.md (critical failures F1 to F8, the 10 weighted criteria totaling 100, thresholds, and the required feedback format).

Return JSON: scores per criterion, total, critical_failures (with the exact sentence), findings (exact sentence, criterion, why, fix), claims_checked, and a decision of approve, revise, rewrite, hold or reject. Do not rewrite the email.
```

If the subagent finds a critical failure or scores below the threshold, revise and send the new draft for a fresh evaluation (a new subagent). Do not reuse the earlier evaluation.

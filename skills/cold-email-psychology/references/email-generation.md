# Email Generation

The knowledge base (principles.md, frameworks.md, hooks.md, ctas.md, examples.md, followups.md) is a set of options, not a formula. Pick what fits this recipient. Two emails from this skill should not sound identical.

## 1. Choosing the approach

Inputs from earlier stages: the claim ledger and decision (prospect-research.md), the offer verdict (offer-engineering.md), the goal, the relationship stage and the available proof.

| Situation | Lead with | Typical ask | Look at |
|---|---|---|---|
| Strong verified signal, relevant offer | A specific observation, then a hedged consequence | Interest check, or a short call if proof is strong | hooks.md (trigger hooks), frameworks.md quick pick |
| Good proof, weak signal | A peer result tied to their segment | Interest check or sample | principles.md (social proof) |
| Useful asset to share, no signal | The asset, no meeting ask | Permission to send it | ctas.md (asset offers) |
| Right person unclear | A one-line routing question | Who owns this | frameworks.md #32 |
| Senior or time-poor recipient | Very short, their priority first, value offer instead of a meeting | A one-word answer | principles.md, practices.md (executive notes) |
| Technical or sophisticated audience | Precision, specifics, no hype, the mechanism stated plainly | A specific question | examples.md (precise ones) |
| Warm or prior contact | An accurate reference to what happened, then a next step | The next agreed step | followups.md |
| Quiet after a first email | One new fact, proof or sharper question | One answerable question | followups.md |
| No verified signal at all | A genuine question and an honest generic note | A lighter ask | ctas.md |

If two approaches fit, choose the one with the strongest verified evidence. Do not choose an approach whose required evidence (a signal, a proof point) is missing.

## 2. Adapting to context

- **Industry and audience sophistication:** match vocabulary to how the recipient talks. Remove jargon they do not use. For regulated fields, avoid claims about outcomes you cannot substantiate and never mention private customer or patient details.
- **Seniority:** shorter and more outcome-focused for senior roles, more specific and operational for practitioners. Do not assume seniority rules, since sources conflict.
- **Region and culture:** formality, directness and norms vary. Ask the user if unsure. Check legal rules for the recipient's region (deliverability-and-compliance.md).
- **Objective:** a reply, a call, an introduction and a sample each need a different ask and different length.
- **Length and structure:** the 50 to 120 word first-email guideline and the one-ask rule are starting points. Use more words when a real piece of evidence needs them, fewer when the message is a simple routing question. Never pad.

## 3. Component guidance

| Component | Guidance |
|---|---|
| Subject line | Specific to them or the problem, short, honest. Avoid fake Re: or Fwd:, clickbait and generic "quick question" without context. Offer 2 or 3 options with different angles. |
| Opening line | A checkable fact about them, or a direct reason for writing. No generic compliments, no fake familiarity, no "I hope this finds you well", no self-introduction as the first line. |
| Personalization | One genuinely relevant detail beats three shallow ones. It must pass the swap test (moving it to another prospect would break it) and trace to a V claim. |
| Value proposition | Outcome first, with a short mechanism, in their language. State an outcome only if the evidence supports it. |
| Proof | One real, relevant item, kept exactly as approved. No proof is better than invented proof. Do not add a mechanism ("after moving to X"), a relationship ("we work with") or any detail the evidence record does not state. Say "one of our customers" only if the user said it is a customer. (Added after an independent evaluator caught this in test TC01.) |
| Call to action | One ask, proportionate to the relationship, easy to decline. Test interest checks against time asks. |
| Objection handling | Pre-empt only an objection you know is likely and answer it honestly in one line. Do not argue. |
| Tone | Plain, direct, human. No exaggeration, no guilt, no artificial urgency. Read it aloud. |
| Follow-ups | Each adds something new; reply in the same thread; see followups.md. |

## 4. Language that reads as machine-written (avoid)

- Openers like "I hope this finds you well", "I came across your company and was impressed", "I wanted to reach out".
- Stacked adjectives and hype: "cutting-edge", "game-changing", "revolutionary", "seamless", "unlock", "supercharge".
- Symmetrical triples and balanced clauses repeated email after email.
- Em dashes (this repository's house style forbids them).
- Praise without a specific, checkable subject.
- Identical sentence shapes across a sequence.

## 5. Drafting procedure

1. Write the claim list the email will make. Each must map to a ledger row (V stated, I hedged, A and U excluded).
2. Choose the approach (section 1) and one structure from frameworks.md or write plain prose.
3. Draft 2 or 3 subject options with different angles.
4. Draft the body. Then cut every sentence that does not earn its place.
5. For sequences, write each follow-up with a distinct job (see followups.md).
6. Do not self-approve. Hand the draft and the claim ledger to the evaluation stage (evaluation-rubric.md). Do not carry the generation reasoning into the evaluation.

## 6. Output of this stage (data contract)

```json
{
  "email": {"subject_options": [""], "body": "", "approach": "", "principles_used": [], "framework_ref": ""},
  "claims_made": [{"sentence": "", "ledger_id": "C1", "class": "V|I", "hedged": true}],
  "assumptions_flagged": [],
  "placeholders_to_fill": []
}
```

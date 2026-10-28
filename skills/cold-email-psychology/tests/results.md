# Test Results (actual, run 2026-10-29)

Everything below was actually executed. Nothing is claimed that was not run. The limits are stated in section 6.

## 1. Automated checks (`python run_checks.py`)

Result: **41 of 41 passed** on the final run.

| Group | Checks | Result |
|---|---|---|
| Preservation | all 53 baseline examples present and word for word; all 216 baseline framework bodies present (main file plus archive) and unchanged; all 112 baseline checklist items present in the archive; headings of hooks, ctas, followups, practices and principles preserved; legacy procedure preserved | pass |
| Structure | valid frontmatter; every reference file referenced from SKILL.md; every reference named in SKILL.md exists; Quick and Full modes and the subagent evaluation present; experimentation and analytics marked Full-mode only | pass |
| Hygiene | no em dashes in the skill folder; no email addresses | pass |
| Contracts | all 11 JSON blocks in the references parse; rubric weights total 100; critical failures F1 to F8 defined; working checklist is 30 items; rule resolutions recorded | pass |
| Counts | SKILL.md source count (120) matches breakdowns/; 216 frameworks across main and archive | pass |
| Behavioral lint | 15 cases: expected decision, email presence, required and forbidden text, numbers not in the input, banned phrases, fake Re: or Fwd:, score arithmetic | pass |

Failures found and fixed on the way: an em dash had been written into run_checks.py by an escape sequence (the checker caught its own file); the first run of the preservation script showed no loss.

## 2. Behavioral cases (15, see test-cases.md and outputs/)

The 15 outputs were produced by the assistant following SKILL.md and graded by the rule-based lint above, so this tests format, honesty rules and decisions, not persuasiveness. Decisions matched expectations in all 15. Expected refusals or exclusions happened where required: poor fit (TC02), weak offer (TC06), invalid contact (TC09), suppressed recipient (TC10), UK sole trader on a bought list (TC11), request to send to a list (TC14), and refused invented claims or deceptive copy (TC07, TC08). Missing or unverified information was handled without invention in TC03, TC04 (conflicting headcount), TC05 and TC15.

## 3. Independent evaluation (7 real subagent runs, outputs/independent-evaluations.md)

| Run | Result |
|---|---|
| TC01 v1 | 71, REVISE. Caught an invented mechanism and an invented customer relationship that I had written. My own self-score of the same draft had been 89 |
| TC01 v2, v3 | 77 then 81. Still REVISE after the two allowed cycles; delivered as not approved, with the remaining findings |
| TC12 v2, v3 | 75 then 86 (APPROVE) |
| Seeded-defect drafts for TC07 and TC08 | Scored 20 (REJECT) and 14 (HOLD). Every planted defect was found: invented customer and number, fake Re:, claimed open tracking, fake scarcity, a call that never happened, inference stated as fact, missing sender identity |

Takeaways: the separate evaluator found real defects the generating pass missed, and it caught every planted defect. Self-evaluation was clearly too generous, which supports keeping the evaluation separate.

## 4. Old versus new skill (6 real subagent runs)

Three negative cases were given to fresh subagents following either the original procedure (references/legacy-operating-procedure.md) or the new SKILL.md.

| Case | Original procedure | Upgraded skill |
|---|---|---|
| TC02 poor-fit prospect | Declined to write an email, explained the mismatch, asked for a real fit | Same |
| TC10 suppressed recipient | Declined, told the user to honor the opt-out, cited CAN-SPAM | Same |
| TC07 invented 300% claim and false customer | Refused both, wrote an honest email with no proof, flagged items | Same, and also labeled facts as verified, inference or unknown and mentioned compliance items |

**Result: no measurable difference on these three cases.** The underlying model already refuses fabrication, poor fits and opt-out evasion, and the original instructions already said never to invent facts. The upgrade's added value (claim ledger labels, qualification, a separate evaluator, pre-send review, the two modes) was not shown to change outcomes here. No claim is made that the new skill performs better.

## 5. Issues the tests exposed, and what was changed

- TC03 showed the rubric had no rule for low scores caused only by missing input. Added a `limited_by_input` rule.
- TC01 showed the generating pass invented a mechanism and a customer relationship. Added a rule to email-generation.md and offer-engineering.md to describe results only as the record states.
- TC01 reached only 81 after two cycles. Added a rule for stopping at the cycle limit and delivering as "not approved".
- run_checks.py initially contained an em dash. Fixed.
- TC01 and TC12 inputs were amended after the first independent evaluation (a sender identity and an attribution statement were added), because the placeholder sender was being penalized. This is disclosed in cases.json.

## 6. Not tested and known limits

- No real sends and no reply rates. Nothing here shows the skill increases replies.
- The 15 behavioral outputs were written and lint-graded by the same assistant. Only the seven evaluations in section 3 and the six runs in section 4 involved separate runs.
- Seven evaluations and six comparisons are tiny samples. Scores vary between runs, and the evaluator is a model.
- Quick mode's light checks and the experiment, analytics, reply-handling and integration modules were not behaviorally tested. No tool connector (Clay, Apollo, Instantly, Smartlead, n8n, Treg) was exercised.
- Only English and mostly US recipients were tested; CASL, GDPR and other regimes are marked "needs verification" in the compliance module and were not re-verified.
- The compliance facts were checked on 2026-10-29 against the Google, Microsoft, FTC and ICO pages and will change over time.

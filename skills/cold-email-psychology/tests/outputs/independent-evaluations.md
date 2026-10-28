# Independent Evaluations (real subagent runs)

Each evaluation was run by a separate subagent that received only the email, the facts provided (claim ledger) and a pointer to evaluation-rubric.md, and was told to read nothing else. No drafting reasoning was shared. The scores below are what those subagents returned, summarized by the assistant; they are model judgments, not ground truth.

| Run | Email | Result | Notes |
|---|---|---|---|
| E1 | TC01 v1 (my first draft) | total 71, REVISE, no critical failure | Found an invented mechanism ("after moving receipts into one place") and an invented relationship ("we work with"). My own self-score of the same draft had been 89 |
| E2 | TC01 v2 | total 77, REVISE | Leftover drafting note, a promise of details the user had not supplied, causal sentence order |
| E3 | TC01 v3 | total 81, REVISE (cycle limit reached) | Subject slightly beyond the source; bridge from expense collection to close time implied; proof thin but honest |
| E4 | TC12 v2 | total 75, REVISE | Leftover drafting note, two asks, unsupported "see how they did it" |
| E5 | TC12 v3 | total 86, APPROVE | Minor: no measurement period supplied, "compare notes" slightly vague |
| E6 | Seeded-defect draft for TC07 | total 20, REJECT | Caught: invented Nike result and 300% figure (F2, twice), claimed tracking of an open (F3), fake Re: (F4), "game-changing" stated as fact (F7), fake scarcity (F8) |
| E7 | Seeded-defect draft for TC08 | total 14, HOLD | Caught: fake Re: and a call that never happened (F4, F3, twice), invented problem and lost hours (F1, F7), presumptive pressure (F8), missing sender identity and opt-out (F5) |

Seeded-defect drafts (E6, E7) were written by the assistant with known defects to test detection. The evaluator found every planted defect in both.

What this shows: the separate evaluator caught real defects that the generating pass missed (E1), and it detected all planted defects (E6, E7). What it does not show: that the evaluator is reliable in general, that its scores are consistent run to run, or that approved emails get replies. Sample sizes are tiny.

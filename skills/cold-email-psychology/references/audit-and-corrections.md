# Audit, Corrections and Preservation Record

This file records what the skill contained before the upgrade, the contradictions and weak claims found, the corrections made, and how the original material was preserved. Nothing listed here was deleted. Baseline for comparison: git tag `pre-upgrade-baseline` (commit 44f41d0) in the public repository.

## 1. Inventory of the original skill (baseline)

| File | Purpose | Size at baseline |
|---|---|---|
| SKILL.md | Operating procedure: inputs, angle, writing rules, follow-ups, checks, output format, limits | 108 lines |
| references/principles.md | Sales psychology principles ranked by frequency, with how to apply each | 133 lines |
| references/frameworks.md | 216 numbered email structures, a quick-pick table, cadence notes | 1347 lines |
| references/hooks.md | Opening line and subject line patterns with counts | 257 lines |
| references/ctas.md | Call to action types and when each works | 61 lines |
| references/examples.md | 53 original example emails (Example 1 to Example 53) | 1407 lines |
| references/checklist.md | Pre-send checklist (112 items at baseline) | 116 lines |
| references/followups.md | Follow-up count, timing, types, phrases to avoid, source conflicts | 92 lines |
| references/practices.md | Writing, list, deliverability, compliance and benchmark notes | 79 lines |
| references/README.md | Index of the reference files | 14 lines |
| (repository) breakdowns/ | One analysis per source (120), outside the skill folder | 120 files |

## 2. Verified numbers (counted from the files on 2026-10-29)

| Number | Value | How counted |
|---|---|---|
| Sources studied | 120 | files in breakdowns/ (001 to 120) |
| Emails analyzed | 1669 | sum of the per-source counts in the header of principles.md. Some counts are estimates (the 510-template Hunter library was analyzed partly by keyword and length analysis), so treat it as "about 1,670" |
| Frameworks | 216 | numbered sections (85 in frameworks.md, 131 in archive/frameworks-extra.md) |
| Principles | 41 | rows in the principles table |
| Examples | 53 | "## Example N" headings in examples.md |
| Checklist items | 30 (grouped), 117 (archived original) | checklist.md and archive/checklist-full.md |

A search of every file in the repository found no mention of "16 sources", "700+" emails or "100+ templates" in the skill, the README or the plugin files. The README, SKILL.md and reference headers all use the numbers above. The GitHub repository description is a setting outside the repository files; it could not be changed from here and may still carry an older number, so set it by hand (suggested text is in CHANGELOG.md).

## 3. Gaps found (now addressed by new modules)

| Gap | Addressed in |
|---|---|
| No prospect research or qualification step; no separation of fact, inference, assumption and unknown | prospect-research.md |
| Offer assumed to be good; no offer evaluation | offer-engineering.md |
| Message selection was a short table; no adaptation logic | email-generation.md |
| Generation approved its own output; no independent evaluation or hard failure rules | evaluation-rubric.md (subagent evaluation in Claude Code) |
| Experiments and feedback loop absent; metrics focused on replies | experimentation.md, performance-analytics.md (Full mode only) |
| Deliverability and compliance spread across practices.md and the checklist; no pre-send review | deliverability-and-compliance.md |
| No handling of replies to cold emails | reply-handling.md |
| No integration boundaries or data contracts | integrations.md |
| No tests | tests/ (see tests/results.md for actual results) |

## 4. Contradictions and questionable claims found

| # | Issue | Where | Resolution |
|---|---|---|---|
| 1 | "The question invites a real answer, not a yes or no that ends the thread" versus a follow-up question "answerable in one word", and several CTA types that are yes or no questions. | checklist, followups.md, ctas.md | One rule: ask one specific question whose either answer is useful. A yes or no question is fine when it moves things forward; avoid vague or thread-ending questions ("Thoughts?"). Chosen because the sources show both forms working and the real failure is an unusable answer. |
| 2 | "One CTA, not a meeting request" versus "give two time options as well as a calendar link". | checklist | One rule: default to a small step. When a meeting ask is justified (strong verified signal and real proof), name a short duration and offer up to two time windows in the text. No calendar link in a cold first email. Chosen because a small ask suits low trust and a link adds friction and deliverability risk. |
| 3 | "No link in the first email" versus "give a calendar link". | checklist | One rule: no links in the first cold email by default. A calendar or asset link can follow once they show interest. Matches the deliverability guidance and rule 2. |
| 4 | "Always include a cost-of-inaction line" versus the no-detail approach (no verified signal). | checklist, SKILL.md | One rule: the line is optional. Use it only when a verified signal or a hedged inference supports it, and omit it for no-detail emails. An invented cost would be a fabricated claim. |
| 5 | Fixed word limits (50 to 120 first email, under about 100 follow-up) were stated as rules, but the sources disagree. | SKILL.md, checklist | Treated as starting points. Original numbers kept as defaults. |
| 6 | "No link in a first email" and "end on a question" versus one vendor's data that one link or a question-free ask lifted replies. | checklist, practices.md | Defaults kept; marked as tests, not laws. |
| 7 | Domain advice: an older checklist line said to send from "a separate, warmed sending domain so your main domain's reputation stays safe". Later sources (Martal, citing M3AAWG) call look-alike domains and rotation abusive. | checklist, practices.md | The line was reworded earlier to "a separate, warmed sending domain or subdomain you own and that is plainly tied to your business, with no fake engagement or look-alike tricks". The earlier wording is recorded here as a historical note and in the archived checklist history. |
| 8 | Executive reply rates: some pages say executives reply less, another says more. | practices.md | Documented as unresolved; the skill does not assume either. |
| 9 | Follow-up count ranges from 2 to 9 across sources. | followups.md | Default of 3 follow-ups kept, labeled a default. |
| 10 | UK rules summarized as "PECR is more lenient for B2B". | practices.md | Incomplete. Verified correction: corporate bodies can be emailed, but sole traders and some partnerships are treated as individuals and need consent or the soft opt-in. Correction added beside the original in practices.md. |
| 11 | CAN-SPAM summarized as "identify as an ad where needed". | practices.md | The FTC guide says to clearly disclose that the message is an advertisement (with leeway in how). Correction added in practices.md. |
| 12 | principles.md ended its note with "None of the four sources gives results for individual emails", written when four sources had been studied. | principles.md | Corrected in place with a dated correction note keeping the original sentence in quotation. The library now draws on 120 sources. |
| 13 | principles.md did not say how it is ranked. | principles.md | Added a note that principles are ranked by frequency in analyzed emails, not by proven reply rate. |
| 14 | Reply-rate benchmarks quoted across many files are vendor claims; a first-party dataset (about 7.5 million emails) averaged about 0.45%, far below the common 3 to 6%. | practices.md, followups.md | Already flagged as unverified. The skill must not use these as promises and should benchmark against the user's own data. |
| 15 | Principle counts and "emails analyzed" totals are judgment calls (some estimated). | principles.md and headers | Stated in those files. The skill must not present counts as evidence of effectiveness. |
| 16 | Some frameworks bake in invented results or hearsay (for example competitor-switch claims, fake urgency). | frameworks.md | Retained (now in the archive where used by 1 or 2 emails), with their existing "avoid" notes. The rubric hard-fails the behavior. |
| 17 | Subject examples such as "quick question" appear in examples while one source says that style now reads as automated. | examples.md | Kept as examples (they must stay word for word); email-generation.md advises specific subjects. |
| 18 | "No em dashes" is a house style of this repository, not an evidence-based rule. | SKILL.md, checklist | Kept and labeled as the repository's style rule. |
| 19 | Example 1 asks for a "2 minute walkthrough"; the README example said "15 minute walkthrough". | README.md, examples.md | Examples must stay word for word, so the README was changed to match ("2 minute walkthrough"). |
| 20 | The README says the skill "was tested on 5 scenarios"; those were self-run format checks, not market tests. | README.md | The README already says they are not measured reply rates. tests/results.md reports the upgrade's tests separately and plainly. |

## 5. Verified facts used by the compliance module (checked 2026-10-29)

Sources consulted that day: Google "Email sender guidelines" (Gmail Help), FTC "CAN-SPAM Act: A Compliance Guide for Business", Microsoft Tech Community post on Outlook requirements for high-volume senders, and ICO "Electronic mail marketing" (PECR). Facts and dates are in deliverability-and-compliance.md. GDPR, Canadian CASL and other regimes were not re-verified in that session and are marked as needing verification.

## 6. How the original material was preserved

- **Examples:** all 53 are unchanged and word for word. tests/run_checks.py compares every example block with a hash recorded at the baseline.
- **Checklist:** the full original (112 items at baseline, 117 with five items added during the upgrade) is in archive/checklist-full.md, unchanged. The working checklist merges the duplicates into 30 grouped items.
- **Frameworks:** all 216 sections are intact. The 85 most-used (count 3 or more, plus every one named in the Quick pick table) are in frameworks.md; the 131 used by only 1 or 2 emails are in archive/frameworks-extra.md, word for word, with their original numbers. frameworks.md ends with an index of the archived ones.
- **Original SKILL.md body:** kept unchanged as legacy-operating-procedure.md.
- **Other reference files:** hooks, ctas, followups, practices and principles keep all original content. Changes are limited to small appended or dated correction notes and to count updates made when sources were added.
- **Baseline:** `git show pre-upgrade-baseline:<path>` retrieves any original file.

## 7. Changelog summary of the upgrade

- New references: prospect-research, offer-engineering, email-generation, evaluation-rubric, experimentation, performance-analytics, reply-handling, deliverability-and-compliance, integrations, this file, legacy-operating-procedure.
- New archive folder: archive/checklist-full.md, archive/frameworks-extra.md.
- New tests: tests/cases.json, tests/run_checks.py, tests/baseline-manifest.json, tests/results.md, tests/outputs/.
- Rewrote SKILL.md into two modes (Quick by default, Full on request) with always-on safety rules; Full mode runs a separate evaluation (a subagent in Claude Code).
- See CHANGELOG.md at the repository root for the release entry.

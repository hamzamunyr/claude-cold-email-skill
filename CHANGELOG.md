# Changelog

## 1.1.0 (2026-10-29)

Upgrade of the cold-email-psychology skill into a staged, evidence-aware system. All 53 examples and all other existing knowledge were preserved (see Preservation below).

### Added
- **Two modes.** Quick (default): use the inputs given, ask only for what is truly missing, write the email, run light checks. Full (campaigns, sequences for a list, or "full mode"): research and qualify, review the offer, generate, run the full independent evaluation, do a pre-send review.
- **Always-on safety rules** in both modes: no invented facts, no deceptive elements, stop on opt-outs and invalid contacts, exclude poor fits, nothing sent without approval.
- **New references:** prospect-research (verified, inferred, assumed and unknown claims, qualification, the claim ledger), offer-engineering, email-generation, evaluation-rubric (critical failures plus a 100-point rubric, and a subagent prompt for Claude Code), deliverability-and-compliance (provider and legal facts checked on 2026-10-29), reply-handling (not interested, send more info, price, already use X, wrong person, next quarter, positive, opt-outs), experimentation and performance-analytics (Full mode only), integrations (optional tool boundaries, approval gates, data contracts), audit-and-corrections.
- **Independent evaluation.** In Claude Code, Full mode runs the evaluation as a subagent that sees only the email, the facts provided and the rubric.
- **Tests.** 15 behavioral cases, 41 automated checks (preservation, structure, JSON contracts, rubric weights, output lint) and recorded results in tests/results.md.
- **CHANGELOG.md** (this file).

### Changed
- **SKILL.md** rewritten as a focused operating procedure for the two modes. The original body is preserved unchanged in references/legacy-operating-procedure.md.
- **checklist.md** consolidated from 117 items (many duplicates) into 30 grouped items, Quick items marked. The full original list is in references/archive/checklist-full.md, unchanged.
- **frameworks.md** now holds the 85 most-used frameworks (used by 3 or more emails, plus every one in the Quick pick table). The 131 used by only 1 or 2 emails moved word for word to references/archive/frameworks-extra.md with their original numbers, indexed at the end of frameworks.md.
- **principles.md**: corrected the outdated line "None of the four sources gives results for individual emails" (the library now draws on 120 sources) and added a note that principles are ranked by frequency, not by proven reply rate.
- **practices.md**: appended dated corrections for the CAN-SPAM and UK PECR summaries.
- **README.md**: updated features, numbers, file list and install options. The example call to action now matches Example 1 (a 2 minute walkthrough).
- Plugin metadata and version.

### Rule resolutions (conflicts in the old checklist)
- Questions: one specific question whose either answer is useful; yes or no is fine when it moves things forward.
- Meetings: default to a small step; when a meeting ask is justified, name a short duration and up to two time windows in the text, with no calendar link in a cold first email.
- Links: none in the first cold email by default; a calendar or asset link can follow once they show interest.
- Cost-of-inaction line: optional, only with a verified signal or a hedged inference, and omitted for no-detail emails.

### Numbers (counted from the files)
120 sources, 1,669 emails analyzed (some counts estimated, for example the 510-template Hunter library), 216 frameworks, 41 principles, 53 examples, 30 checklist items.

### Preservation
- Examples: all 53 unchanged, checked by hash against the baseline.
- Frameworks: all 216 sections intact (main file plus archive), checked by hash.
- Checklist: all 112 baseline items present in the archive.
- Baseline: git tag pre-upgrade-baseline.

### Known limitations
See tests/results.md. The upgraded skill has not been tested on real sends, and no claim is made that it improves reply rates.

### Suggested GitHub repository description (set manually)
Claude skill that writes honest cold emails, follow-ups and replies with sales psychology. Quick mode by default, Full mode with research, offer review and independent evaluation. 120 sources, 53 examples.

## 1.0.0

First finalized release: SKILL.md, references (principles, frameworks, hooks, CTAs, examples, checklist, follow-ups, practices), 120 source breakdowns and the Claude.ai zip.

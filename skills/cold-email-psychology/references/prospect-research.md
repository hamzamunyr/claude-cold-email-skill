# Prospect Research and Qualification

Use this before writing any email. The goal is to understand the prospect well enough to decide (a) whether to email them at all and (b) what can be said truthfully.

## 1. Evidence classes (label every statement you rely on)

| Class | Meaning | May appear in an email as |
|---|---|---|
| V: Verified fact | Seen in a named source (page, post, filing, job ad, the user's own CRM) with a date | A plain statement, with the source kept in the claim ledger |
| I: Reasonable inference | Follows from verified facts but is not stated by the prospect | A hypothesis with hedged wording (often, may, tends to) |
| A: Unverified assumption | A guess, or a claim from a low-quality or undated source | Never stated as fact. Ask a question instead, or leave it out |
| U: Unknown | No information | Never filled in. State that it is missing |

Rules:
- Never describe an I as a V. "Hiring three SDRs" is V if the job posts exist. "So your outbound is a priority" is I.
- A claim with no source is an A. Treat anything from memory, from the user's recollection without a source, or from an AI summary without a link as A until checked.
- Personal details (family, health, politics, home address, personal social posts not meant for business) are out of scope unless the user supplied them for this exact purpose, and even then they usually should not appear in a cold email.
- Do not invent recent events, funding, achievements, financials, buying intent or problems. If you cannot find a real signal, say so.

## 2. What to establish

| Item | Notes |
|---|---|
| Company and industry | Name, what it sells, to whom, size band, geography |
| Business model | How it makes money, who its customers are, sales motion |
| Products and services | Only those relevant to the offer |
| Likely customer profile | Who they serve (helps judge fit) |
| Verified signals | Dated, sourced: hires, launches, funding, tech changes, posts, events, press |
| Potential problems | Always I, never V, unless the prospect stated them publicly |
| Relevance of the offer | Link between a signal and the offer, written as a hypothesis |
| Evidence and source | URL or user-supplied record for each V |
| Confidence | High, medium or low, with the reason |
| Missing information | List what you could not find |

## 3. Research procedure

1. Use only what is supplied or what authorized tools return. If no research tools are available, say so and work with the supplied data. Do not pretend to have browsed.
2. If tools are available (see integrations.md), gather the company page, a recent signal, and one role-relevant detail. Record the URL and date for each.
3. Build the claim ledger (section 5). Every sentence in the draft that states something about the prospect must trace to a ledger row.
4. Check for conflicts: if two sources disagree (for example headcount), record both, use the more reliable one or neither, and mark the claim A or leave it out.
5. Check freshness: signals older than about 90 days are weak for "recent" wording, and signals already acted on by many senders (a funding announcement everyone saw) need a sharper angle.

## 4. Qualification: should this person be emailed?

Score each factor, then decide. Do not generate a persuasive email for an unsuitable target.

| Factor | Qualifies | Weak | Exclude |
|---|---|---|---|
| Problem fit | The offer solves a problem they plausibly have, with a verified signal | Plausible but no signal | The offer is irrelevant to their business |
| Role fit | They own or influence the problem | Adjacent role | Wrong function, or no authority and no route to the owner |
| Company fit | In the user's real target segment | Edge of the segment | Outside the segment, too small or too large to serve |
| Timing | A recent signal or a stated initiative | No timing signal | They recently bought a competing solution or said no |
| Contact validity | Verified business address, not suppressed | Unverified or catch-all | Invalid, role mailbox used as a trap risk, on a suppression or do-not-contact list |
| Legal eligibility | Lawful basis and region checked (see deliverability-and-compliance.md) | Unclear | A regime that requires consent you do not have (for example a sole trader in the UK) |
| Existing relationship | None, or a documented one | Unclear history | Previously opted out, bounced hard, or a customer under a different team |

Decision:
- **Proceed:** no Exclude, and at least problem fit and contact validity are Qualifies.
- **Proceed with a question-led email:** problem fit is Weak because no signal exists. Say plainly that the email will be generic.
- **Hold:** missing information blocks a safe decision (for example region or consent). State exactly what to verify.
- **Exclude:** any Exclude. Recommend removing the prospect and say why. Do not draft the email.

## 5. The claim ledger (shared with the evaluation stage)

Create a table before drafting:

| ID | Claim the email will make | Class (V, I, A, U) | Source and date | Allowed wording |
|---|---|---|---|---|
| C1 | Acme posted three SDR roles this month | V | careers page, 2026-10-20 | State directly |
| C2 | That likely means pipeline coverage is a priority | I | derived from C1 | Hedge ("often", "may") |
| C3 | They struggle with onboarding | A | none | Do not state; ask a question |

An email may contain only V claims stated plainly, I claims that are hedged, and questions. A claims and U items must not appear as statements.

## 6. Output of this stage (data contract)

```json
{
  "prospect": {"name": "", "role": "", "company": "", "industry": "", "region": "", "contact_status": "verified|unverified|invalid|suppressed"},
  "claims": [{"id": "C1", "text": "", "class": "V|I|A|U", "source": "", "source_date": "", "allowed_wording": ""}],
  "fit": {"problem": "qualifies|weak|exclude", "role": "", "company": "", "timing": "", "legal": ""},
  "decision": "proceed|proceed_generic|hold|exclude",
  "confidence": "high|medium|low",
  "missing_information": []
}
```

Hand only the ledger and the decision to the next stage. If the decision is hold or exclude, stop and report why.

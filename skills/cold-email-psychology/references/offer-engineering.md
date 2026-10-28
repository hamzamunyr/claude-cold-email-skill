# Offer Engineering

A good email cannot rescue a weak offer. Evaluate the offer before writing. Do not assume the user's offer is compelling.

## 1. Offer evaluation

Fill this in from what the user supplied. Mark anything the user did not provide as unknown. Do not guess.

| Question | What a strong answer looks like | Rating (strong, ok, weak, unknown) |
|---|---|---|
| Who exactly is it for? | A specific role at a specific kind of company | |
| What problem does it address? | A problem the audience already recognizes, in their words | |
| Why does it matter commercially? | A cost, risk, revenue or time consequence the buyer cares about | |
| What outcome is promised? | A concrete outcome for the customer, not a feature | |
| What is different? | One thing a competitor cannot honestly say | |
| Is the promised outcome credible? | Backed by evidence the user actually has | |
| What is the risk and price context? | Stated, or the next step makes the risk small | |
| What evidence supports it? | Real customer results, a pilot, data, a demo, with permission to use them | |
| What objections are likely? | Listed with honest answers | |
| What is the right next step? | Proportionate to the relationship (see section 5) | |

## 2. Features versus outcomes

| Feature (what it is) | Outcome (what changes for the customer) |
|---|---|
| Automated reporting dashboard | Finance closes the month without rebuilding the same spreadsheet |
| 24/7 chat support | Customers get answers outside office hours, so fewer abandoned carts |

Lead with the outcome and name just enough mechanism to make it believable. Features belong later or in a follow-up. Use the buyer's own vocabulary where you know it.

## 3. Evidence rules for the value proposition

- Do not promise revenue, leads, conversions, savings or timelines unless the user has supporting evidence they can show. "Typically", "often" and "can" are acceptable only when the pattern is real.
- Describe a result only as the record states it. Do not add how it was achieved, who the customer is, or that the relationship is current unless the user supplied that.
- A named customer result is allowed only if the user confirms it is real and permitted to share. Keep the customer, the metric definition, the time window and any material conditions exactly as the record states.
- Never fabricate a case study, testimonial, rating, award, customer count, certification or competitor weakness.
- If the user has no evidence, say so and either write without proof, offer a low-risk trial or sample, or recommend collecting proof first.
- Do not copy another vendor's results from a blog as if they were the user's own. Third-party statistics may be cited only with the source named and only when relevant.

## 4. Diagnosis of a weak offer

If two or more ratings in section 1 are weak or unknown, do not write the email yet. Return:

1. The strongest part of the offer.
2. The weakest parts, each with a reason.
3. One or two concrete improvements, for example:
   - Narrow the audience ("accounting teams at 20 to 200 person firms" instead of "businesses").
   - Reframe around a measurable problem the audience already complains about.
   - Replace an unsupported claim with a smaller, true one.
   - Add a risk reducer the user can really honor (a short pilot, a sample, a money-back term, a free audit).
   - Change the ask to something the recipient can say yes to cheaply.
4. What to gather before sending (a result, a permission, a data point).

Offer drafts the user can accept or reject. Do not silently rewrite the offer into something the user does not actually sell.

## 5. Choosing the next step

| Relationship | Reasonable next step |
|---|---|
| Total stranger, low evidence | A question or an offer to send something useful (a short breakdown, a benchmark) |
| Stranger with a strong verified signal and good proof | A short call, time-boxed, easy to decline |
| Referral or mutual contact (real, permitted) | A short introduction call or a right-person ask |
| Prior interaction | Reference it accurately and propose the next step you agreed |
| Right person unclear | A right-person question, not a meeting request |

## 6. Output of this stage (data contract)

```json
{
  "offer": {"audience": "", "problem": "", "outcome": "", "differentiator": "", "risk_context": "", "price_context": ""},
  "evidence": [{"claim": "", "supported": true, "source": "", "permission_to_use": true}],
  "objections": [{"objection": "", "honest_answer": ""}],
  "ratings": {"audience": "", "problem": "", "outcome": "", "credibility": "", "next_step": ""},
  "verdict": "write|improve_offer_first",
  "improvements": []
}
```

Pass only the `write` verdict forward. For `improve_offer_first`, stop and report.

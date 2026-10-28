# Performance Analytics and Feedback Loop

Load this only in Full mode, when the user supplies results or asks how to measure them. Do not optimize for opens or total replies alone. Optimize for qualified business outcomes. Never invent performance data.

## 1. Metrics (track all of these when possible)

| Metric | Definition | Notes |
|---|---|---|
| Delivery rate | Delivered divided by sent | Technical health |
| Bounce rate | Bounced divided by sent | Keep low; a spike means list or setup problems |
| Complaint and unsubscribe rate | Per delivered | Early warning for relevance and reputation |
| Positive reply rate | Positive replies divided by delivered | Interest, referral to the right person, meeting request |
| Negative reply rate | Negative replies divided by delivered | "Not interested", "stop", hostile |
| Neutral and automatic | Out-of-office, auto-replies | Report separately; exclude from interest |
| Qualified meetings booked | Meetings that meet your qualification rule, divided by delivered | Primary outcome for most campaigns |
| Meetings attended | Held divided by booked | No-shows reveal weak commitment |
| Opportunities created | Per qualified meeting and per delivered | Pipeline quality |
| Customers acquired | Per opportunity and per delivered | Slow, rare, but the real outcome |
| Revenue and cost | Revenue, tool, data and labor cost; cost per qualified meeting and per customer | Only when you have the data |

Opens and clicks are unreliable (mail privacy features, bots, security scanners). Use them only as a rough health signal for deliverability, never as an optimization target.

## 2. Reading results honestly

- **Correlation is not causation.** A variant won in one audience and week; it may not win elsewhere. Differences in list quality, timing, sender reputation and seasonality can look like copy effects.
- **Small numbers are noisy.** With 100 sends and 4 replies versus 7 replies, the difference is well within chance. Report the counts, not just percentages.
- **Do not claim statistical significance** unless you ran an appropriate test with an adequate sample (for example a two-proportion test with a pre-set threshold) and report the interval or p-value. Otherwise write "directional, not conclusive".
- **Multiple comparisons:** if you test many variants, some will look good by luck. Confirm a promising result with a fresh test before adopting it.
- **Segment effects:** a result may reverse across segments. Check by segment, but treat sliced results as hypotheses.
- **A single success is an anecdote.** One great reply or meeting is not proof of a strategy.
- **Qualified outcomes outrank volume.** A variant with fewer replies but more qualified meetings is the better one.

## 3. Feedback loop

When the user supplies results (or an authorized tool provides them), do this:

1. Load them into the results record (section 6). If fields are missing, say what is missing.
2. Separate **observed results** (counts and rates) from **hypotheses** (why you think it happened).
3. Look for patterns: which segments respond positively, which offers produce qualified interest, which objections recur, which approaches underperform, which asks lead to real conversations, which campaigns lead to meetings and customers.
4. Recommend the next experiment, naming the single variable, the hypothesis and the pre-registered metric.
5. Update advice only where the evidence supports it. When evidence conflicts with this skill's defaults, report the conflict rather than silently changing the rules.
6. If there is no data, say so. Do not fill the gap with benchmarks presented as the user's results.

## 4. Results record format

CSV (one row per variant per period):

```csv
campaign_id,variant_id,hypothesis,segment,offer,angle,subject,cta,sequence_step,sent,delivered,bounced,complaints,unsubscribes,positive_replies,negative_replies,neutral_replies,meetings_booked,meetings_attended,opportunities,customers,revenue,cost,start_date,end_date,notes
```

JSON equivalent:

```json
{
  "campaign_id": "", "variant_id": "", "hypothesis": "",
  "segment": "", "offer": "", "angle": "", "subject": "", "cta": "", "sequence_step": 1,
  "volumes": {"sent": 0, "delivered": 0, "bounced": 0, "complaints": 0, "unsubscribes": 0},
  "replies": {"positive": 0, "negative": 0, "neutral": 0},
  "outcomes": {"meetings_booked": 0, "meetings_attended": 0, "opportunities": 0, "customers": 0, "revenue": 0, "cost": 0},
  "dates": {"start": "", "end": ""}, "notes": ""
}
```


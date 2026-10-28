# Optional GTM Tool Integrations

These integrations are optional. The skill works with only a conversation. Do not assume any tool, credential, endpoint or capability exists. Check which tools are actually available in the current environment before proposing to use one, and say plainly when a tool is missing.

## 1. Principles

1. **Separate stages.** Research, offer evaluation, generation, evaluation, pre-send review, sending and analysis are separate stages with explicit inputs and outputs. A tool may serve one stage; do not let one step silently trigger the next.
2. **Human approval for consequential actions.** Never send an email, create or modify records, launch a campaign, enrich in bulk with paid credits, or change a system without explicit approval for that action. Generating the content does not authorize sending it. An existing, explicitly authorized workflow may change this, but only if the user says so for that workflow.
3. **No invented capabilities.** Do not state that a tool can do something unless the tool's own description or the user says so. Do not invent API endpoints, parameters or limits.
4. **Credentials stay with the user.** Never ask for or store passwords or API keys in a conversation. Use the platform's own connection flow.
5. **Cost and side-effect disclosure.** Before any call that spends credits, writes data or contacts people, state what it will do and the estimated cost if known, and ask.
6. **Data minimization.** Pull only fields needed for the task. Respect suppression and opt-out data.

## 2. Where each type of tool can fit

| Tool type | Examples | Possible role | Not allowed without approval |
|---|---|---|---|
| Enrichment and data | Clay, Apollo, Treg (if connected), email verification services | Gather company and signal data (research stage); verify addresses (qualification stage) | Bulk enrichment that spends credits; writing back to a CRM |
| Workflow automation | n8n | Pass stage outputs along as JSON; schedule reviews | Triggering sends or launching a campaign |
| Sending platforms | Instantly, Smartlead | Receive approved sequences; report results | Importing leads, activating a campaign, changing sending settings |
| CRM | Any | Source of prospect and suppression data; destination for approved outcomes | Creating or modifying records without approval |
| Analytics and reporting | Platform dashboards, spreadsheets | Provide results for the feedback loop | Anything beyond reading unless approved |

If a connector is listed in the environment, read its tool descriptions before use. If it is not listed, offer a manual alternative (the user exports a CSV and pastes it).

## 3. Data contracts between stages

All contracts are plain JSON so any tool or a human can produce or consume them. Fields may be empty but should not be invented. Each stage must reject input it cannot validate.

### 3.1 Prospect record (input to research)

```json
{
  "prospect_id": "",
  "name": "", "role": "", "company": "", "company_domain": "", "industry": "", "region": "",
  "email": "", "email_status": "verified|risky|unverified|invalid|unknown",
  "source": "", "source_date": "",
  "suppressed": false, "suppression_reason": "",
  "notes_from_user": ""
}
```

### 3.2 Research findings (output of research, see prospect-research.md)

```json
{"prospect_id": "", "claims": [{"id": "", "text": "", "class": "V|I|A|U", "source": "", "source_date": ""}], "fit": {}, "decision": "proceed|proceed_generic|hold|exclude", "confidence": "", "missing_information": []}
```

### 3.3 Offer evaluation (output of offer-engineering.md)

```json
{"offer_id": "", "verdict": "write|improve_offer_first", "ratings": {}, "evidence": [], "objections": [], "improvements": []}
```

### 3.4 Generated email (output of email-generation.md)

```json
{"email_id": "", "prospect_id": "", "offer_id": "", "subject_options": [], "body": "", "claims_made": [{"sentence": "", "ledger_id": "", "class": "", "hedged": true}], "placeholders_to_fill": []}
```

### 3.5 Quality assessment (output of evaluation-rubric.md)

```json
{"email_id": "", "total": 0, "scores": {}, "critical_failures": [], "findings": [], "decision": "approve|revise|rewrite|hold|reject"}
```

### 3.6 Pre-send review (output of deliverability-and-compliance.md)

See that file for the schema. Its overall field is `ready_for_human_review`, `hold` or `exclude`.

### 3.7 Campaign results (input to performance-analytics.md)

See that file for the CSV and JSON formats.

## 4. Example flow with human gates

1. User supplies or exports a list. Stage: **prospect records**.
2. Research stage produces findings. If a connector is used for enrichment, ask before spending credits. Gate: user reviews exclusions.
3. Offer stage returns a verdict. Gate: user approves the offer wording.
4. Generation produces drafts. Evaluation runs separately. Gate: user reviews approved drafts.
5. Pre-send review checks list and compliance. Gate: user approves the exact recipients and copy.
6. **A human sends or schedules the campaign** in their sending platform, or explicitly authorizes the agent to do a specific action.
7. Results are exported back to the user for the feedback loop.

## 5. n8n and automation notes

- Model the stages as separate nodes passing the JSON above. Put the human-approval step as a manual node or an explicit approval message before any send node.
- Add validation nodes that reject records with missing sender, suppressed recipients, or evaluation decisions other than `approve`.
- Log the claim ledger and the evaluation output with each email for audit.

## 6. What this skill does not do

- It does not log in to or control sending platforms by itself.
- It does not guarantee a connector exists in your environment.
- It does not store campaign history between sessions unless the user provides it again or an authorized tool does.

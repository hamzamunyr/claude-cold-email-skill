# Pre-Send Review: Deliverability and Compliance

Two different questions: (1) will mailbox providers accept the mail (deliverability), and (2) is sending it lawful and respectful (compliance)? Passing one does not establish the other. Authenticated domains, verified addresses and low bounce rates do not establish legal compliance. Nothing here is legal advice, and nothing guarantees inbox placement.

Rules and provider policies change. Treat the facts below as of the date shown, and re-check them before an important campaign. If research tools are available, re-verify and record the source and date.

## 1. Verified provider and legal facts (checked 2026-10-29)

| Topic | What the source says | Source |
|---|---|---|
| Gmail, all senders | Must meet requirements from 1 Feb 2024; authenticate with SPF or DKIM (and keep spam rates low) | Google "Email sender guidelines" (Gmail Help) |
| Gmail, bulk senders (more than 5,000 messages a day to Gmail accounts) | SPF, DKIM and DMARC (policy may be none); marketing messages need one-click unsubscribe and a visible unsubscribe link; keep the Postmaster spam rate under 0.10% and never reach 0.30% | Same |
| Outlook.com, Hotmail, Live | Senders above 5,000 emails a day must pass SPF, DKIM and DMARC (at least p=none, aligned); effective 5 May 2025; non-compliant mail is rejected with 550 5.7.515; also a valid From or Reply-To address, a functional unsubscribe and list hygiene | Microsoft Tech Community post on Outlook high-volume sender requirements |
| US CAN-SPAM | Seven requirements: no false or misleading header information; no deceptive subject lines; clearly disclose that the message is an advertisement; include a valid physical postal address; explain clearly how to opt out; honor opt-outs within 10 business days (the mechanism must work for at least 30 days after sending); you stay responsible when others send for you. It applies to all commercial email including B2B. Penalties up to $53,088 per violating email. No prior consent is required, but opt-outs must be honored | FTC "CAN-SPAM Act: A Compliance Guide for Business" |
| UK PECR | Individuals must have consented, or fall under the soft opt-in (existing customers, similar products, opt-out offered). Corporate subscribers (companies, LLPs, government bodies) can be emailed without consent, but sole traders and some partnerships are treated as individuals. Never disguise identity; provide a valid opt-out address; keep a do-not-contact list. UK GDPR still applies to personal data | ICO "Electronic mail marketing" |

Not re-verified in that session and therefore to be checked before use: EU GDPR and member-state ePrivacy rules (lawful basis, legitimate interest tests, objection rights), Canada's CASL (consent rules are strict), Australia's Spam Act, and any other jurisdiction. Say "needs verification" for these, not "compliant".

## 2. Technical deliverability review

| Item | Check | Notes |
|---|---|---|
| Authentication | SPF, DKIM and DMARC published and aligned for the sending domain | Mind the SPF 10-lookup limit; start DMARC at p=none if new |
| Sender identity | Real From name, working reply address, a domain the company owns and that is plainly tied to the business | No look-alike domains, no masked senders, no fake engagement (see audit-and-corrections.md item 4) |
| Reputation and ramp | New domains and mailboxes warmed gradually, volume ramped, per-mailbox limits respected | Sources differ on exact limits; stay conservative and watch placement |
| List hygiene | Verified addresses, low bounce, no purchased or scraped lists, no role addresses, catch-alls handled | Hard bounces removed after every send |
| Suppression | Unsubscribes, complaints, hard bounces, "stop" replies and do-not-contact entries excluded automatically | Check before every send, not once |
| Bounce management | Bounces monitored; pause if bounce rate climbs | Many sources say keep it under about 2% |
| Complaint monitoring | Postmaster Tools or equivalent; stay well below provider limits | Above 0.10% is a warning, 0.30% is a danger line (Google) |
| Content | Plain, honest, few or no links, no spam-trigger stacks, no deceptive subject | Filters judge overall patterns |
| Tracking | Open and click tracking add third-party domains and are unreliable; consider leaving them off | One large vendor dataset reports higher replies with open tracking off (unverified) |
| Infrastructure honesty | Do not rotate domains or add mailboxes to evade limits; do not simulate engagement | Industry bodies describe these as abusive |
| Placement testing | Seed tests are a lagging, imperfect signal | Never promise inbox placement |

## 3. Legal and privacy review

For each recipient, answer:

1. **Where is the recipient?** Region decides the rules. If unknown, hold.
2. **What kind of recipient?** A named employee of a company, a generic company mailbox, a sole trader, a consumer. The rules differ (for example PECR on sole traders).
3. **What is the lawful basis or consent position?** US: CAN-SPAM requires honest headers and opt-out handling, not prior consent. UK: corporate subscribers may be emailed, individuals need consent or soft opt-in. EU and others: check lawful basis and local rules.
4. **Where did the data come from?** Source, date, whether it was collected lawfully and whether you can tell the recipient how you got it. Avoid purchased lists of unknown origin.
5. **Is the recipient suppressed?** Prior unsubscribe, complaint, objection or a customer who opted out.
6. **Does the email carry what the rules require?** Accurate sender, physical postal address where CAN-SPAM applies, clear disclosure that it is a commercial message, a working opt-out, and a way to object where data protection law requires it.
7. **Is personal data used proportionately?** Use only business-relevant information. Do not use sensitive personal data.
8. **Is consent for one channel treated as consent for another?** It is not. Permission to call is not permission to email.

If any answer is unknown, the verdict is "needs verification" (HOLD), listing exactly what to check.

## 4. Hard rules

- Do not recommend evading spam filters, ignoring opt-outs, disguising sender identity, circumventing provider restrictions or simulating engagement.
- Honor opt-outs fast (the legal ceiling in the US is 10 business days; same day is safer). Treat "not interested" and "stop" replies as opt-outs.
- Do not claim guarantees about inbox placement, legal compliance or results.
- Keep sources and dates for any provider or legal claim you rely on.

## 5. Pre-send review output (data contract)

```json
{
  "campaign": "",
  "recipient_checks": [{"contact_id": "", "region": "", "recipient_type": "", "contact_status": "", "suppressed": false, "basis": "", "verdict": "pass|hold|exclude", "needs_verification": []}],
  "technical": {"spf": "pass|fail|unknown", "dkim": "pass|fail|unknown", "dmarc": "pass|fail|unknown", "sender_domain_ok": "yes|no|unknown", "list_verified": "yes|no|unknown", "bounce_plan": "", "complaint_monitoring": ""},
  "message": {"opt_out_present": true, "sender_identity_ok": true, "physical_address_where_required": "yes|no|not_applicable|unknown", "deceptive_elements": []},
  "sources": [{"claim": "", "url": "", "checked": ""}],
  "overall": "ready_for_human_review|hold|exclude"
}
```

The overall result is never "send". Sending is a human decision.

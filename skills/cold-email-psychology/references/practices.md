# Writing and Sending Practices

Distilled from the practice and deliverability guides (breakdowns #053 to #060: Smartlead, ZoomInfo, Saleshandy, Streak, Clay, Martal, Close, Mailforge). These sources are vendor blogs, so numbers are their claims and rules change; check current provider rules before you rely on a threshold. Nothing here is legal advice.

## 1. Writing the email

- Make it one-to-one: one reader, one problem, one small ask. (Smartlead, Streak, Martal, Close)
- Personalize on something specific and true (a role, a hire, an announcement), not just the first name. Bulk templates that differ only by merge fields are easy for filters and people to spot. (Martal, ZoomInfo, Mailforge)
- Subject: short, honest, matches the body, no fake "Re:" or "Fwd:". Write the pre-header on purpose. (Mailforge, Streak, Martal)
- Open with their context, not your company. (Martal, Smartlead)
- Keep it short. Sources suggest 50 to 150 words, under about 120 for best readability. One call to action, no attachments, at most one or two plain links. (Close, Mailforge, Smartlead)
- Plain text beats a designed template. Avoid capitals, stacked exclamation marks and hype words. A short list of swaps: replace "free", "guaranteed", "act now" with plain, specific wording. (Mailforge, Martal)
- Spam filters judge overall patterns, so a clean word list is not enough. Repetitive structure and bulk-looking copy count too. (ZoomInfo)
- Sign with a real name, title, company and physical address. Use a consistent from name. (Martal, Saleshandy)
- Include an easy opt-out. Either an unsubscribe line or a plain "if this is not relevant, tell me" sentence. (Martal, Clay, Saleshandy)
- Read it aloud and have someone read it. If it sounds stiff, rewrite it. (Mailforge, Close)
- Use AI to brainstorm and edit, not to replace research. (Close, Saleshandy)
- Never fake a reply, a forward or a forwarded executive note. (Mailforge, Close breakdown)

## 2. Follow-ups and cadence

- Each follow-up adds something new: a proof point, an angle, a sharper question. Repeating the first email word for word (as in one Saleshandy sample) is a mistake. (Martal, Saleshandy)
- Spacing: sources range from day 1, 2, 4, 8 (Close) to a floor of 4 to 7 days between touches (Martal). Pick one and keep each touch visible on its own.
- Length of sequence: about 3 to 5 touches per lead; 2 to 4 for small business, 3 to 6 mid-market, more for enterprise. (Saleshandy, Martal)
- Sunset people who never engage. Treat "not interested" or "stop" as an opt-out. (ZoomInfo, Martal)
- Cap contacts per company: one active contact at a small company, two or three at mid-market. (Martal)
- Answer replies promptly. (Martal)

## 3. Lists and targeting

- Narrow, verified lists beat big ones. Verify before every send and keep hard bounces under 2%. (ZoomInfo, Martal, Smartlead)
- Avoid purchased or scraped lists (spam traps), role addresses (info, sales) and catch-all domains. (ZoomInfo, Martal, Clay)
- Use intent signals to narrow, not to expand. Revalidate contacts not engaged in 6 to 12 months. (Martal)
- Keep a do-not-contact list. (Smartlead)

## 4. Sending infrastructure (verify against current provider rules)

- Authenticate: SPF, DKIM, DMARC with alignment (start DMARC at monitor mode), mind the SPF 10-lookup limit. Google and Microsoft now reject or throttle non-compliant bulk mail. (ZoomInfo, Martal, Clay)
- Ramp slowly: new inbox about 5 to 10 a day, warming 20 to 40, established 40 to 50, spread across the day, and ramp over 2 to 6 weeks. Do not send in bursts. (ZoomInfo, Martal, Clay, Smartlead)
- Per-inbox limits, not just per-domain. Add inboxes instead of pushing volume. (ZoomInfo, Clay)
- Open tracking: pixels are unreliable (mail privacy features inflate opens) and can add a third-party domain. If you track, use your own tracking domain, and consider turning it off once a campaign is proven. (Clay, ZoomInfo)
- Monitor: bounce rate, complaint rate (hold under 0.10%, trouble near 0.30%), replies, positive replies. Use Google Postmaster Tools and blocklist checks. (ZoomInfo, Martal)
- Stop failing campaigns and failing inboxes early. (Clay, Smartlead)
- If already in spam: stop, check blocklists and DNS, find the bad segment, restart small to engaged contacts. (Martal)

### The domain debate (sources conflict)

- Older playbooks (Clay, Smartlead, Saleshandy) recommend several look-alike sending domains, inbox rotation and warm-up networks.
- Martal reports that industry bodies (M3AAWG, Spamhaus) now call look-alike domains, extra accounts used to bypass volume limits, simulated engagement and masked sending domains abusive. It advises a subdomain of a domain you own instead.
- Skill default: protect your main domain, but do it transparently (a subdomain or a plainly related domain you own), never fake engagement, and avoid rotation as a way around limits. Flag this to the user as a judgment call.

## 5. Compliance (high level)

- US CAN-SPAM: accurate sender and subject, identify as an ad where needed, a physical address, a working opt-out honored within 10 business days (same day is safer).
- EU and UK: GDPR needs a lawful basis (legitimate interest for B2B must be demonstrable); PECR is more lenient for B2B in the UK.
- Canada: CASL needs consent (implied in limited cases) and an unsubscribe.
- Consent for one channel (a call) is not consent for another (email). (Martal)
- Check the recipient's region and ask a lawyer for anything high stakes.

## 6. Measuring results (Instantly #076, lemlist #077, Woodpecker #078, Saleshandy #079, Apollo #080, GMass #081)

- Reply rate = replies divided by delivered emails (exclude hard bounces). Classify replies: positive, referral, objection, not now, unsubscribe, out of office.
- Judge by positive reply rate, meetings and cost per meeting, not raw replies or opens.
- Vendor ranges (unverified): about 5 to 10% is solid for B2B, 10 to 15% excellent, higher only on tight, high-intent segments; broad lists on new domains often sit in low single digits. Published ranges conflict, so benchmark against your own past campaigns.
- Test one variable at a time (subject, opener, proof, CTA, send window), with a success rule set before you start.- Other vendor figures (unverified): an overall average near 3.4% from one large dataset and about 8.5% from another, so check which dataset a benchmark uses. Smaller lists (under 50) are reported to reply far better than lists over 1,000. C-suite and enterprise reply least; managers and small companies reply more. Opens are unreliable, so judge by replies.- Woodpecker (#078, unverified): small, tightly segmented lists with about 3 truly specific custom lines beat large generic sends; 100 researched prospects can match the replies of 1,000 generic ones with less spam risk. If replies turn negative, check follow-up spacing first, then strip salesy copy. Overused subjects like "Quick question for you" and "Thought this might be useful" are said to read as automation now, so prefer specific, contextual subjects.- Saleshandy (#079, unverified, read via a summary): campaigns under 200 prospects are reported to reply roughly twice as well as 500 to 1,000. A single soft ask ("worth a quick chat?") is reported to earn far more positive replies than a calendar-link ask. Bounce rates by verification status: valid about 1.2%, risky about 2.2%, bad about 10.6%. Adding LinkedIn or calls to email is reported to raise positive replies. Its follow-up spacing (24 to 48 hours for managers, 2 to 3 days for senior buyers) is shorter than most sources; the skill keeps the 2 to 3 business day default.- Apollo (#080, unverified): a tiered view of reply rate (under 2% a problem, 3 to 5% normal for a well-run campaign, 5 to 8% strong, 10%+ excellent) and positive-reply targets (2 to 3% minimum, 4 to 6% target). When results are weak, diagnose in order: deliverability, then list quality, then messaging.- GMass (#081, unverified): match the metric to the goal (if the ask is a link click, reply rate is not the measure); a large gap between opens and replies points to weak messaging; segment by behavior (opened but did not reply) and send those people new messaging; when you cite their work, link to the real specific page, not a category page.


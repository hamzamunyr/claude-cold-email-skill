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

## 6. Measuring results (Instantly #076, lemlist #077, Woodpecker #078, Saleshandy #079, Apollo #080, GMass #081, Artisan #082, Breakcold #083, Martal #084, SalesHive #085, Belkins #086)

- Reply rate = replies divided by delivered emails (exclude hard bounces). Classify replies: positive, referral, objection, not now, unsubscribe, out of office.
- Judge by positive reply rate, meetings and cost per meeting, not raw replies or opens.
- Vendor ranges (unverified): about 5 to 10% is solid for B2B, 10 to 15% excellent, higher only on tight, high-intent segments; broad lists on new domains often sit in low single digits. Published ranges conflict, so benchmark against your own past campaigns.
- Test one variable at a time (subject, opener, proof, CTA, send window), with a success rule set before you start.- Other vendor figures (unverified): an overall average near 3.4% from one large dataset and about 8.5% from another, so check which dataset a benchmark uses. Smaller lists (under 50) are reported to reply far better than lists over 1,000. C-suite and enterprise reply least; managers and small companies reply more. Opens are unreliable, so judge by replies.- Woodpecker (#078, unverified): small, tightly segmented lists with about 3 truly specific custom lines beat large generic sends; 100 researched prospects can match the replies of 1,000 generic ones with less spam risk. If replies turn negative, check follow-up spacing first, then strip salesy copy. Overused subjects like "Quick question for you" and "Thought this might be useful" are said to read as automation now, so prefer specific, contextual subjects.- Saleshandy (#079, unverified, read via a summary): campaigns under 200 prospects are reported to reply roughly twice as well as 500 to 1,000. A single soft ask ("worth a quick chat?") is reported to earn far more positive replies than a calendar-link ask. Bounce rates by verification status: valid about 1.2%, risky about 2.2%, bad about 10.6%. Adding LinkedIn or calls to email is reported to raise positive replies. Its follow-up spacing (24 to 48 hours for managers, 2 to 3 days for senior buyers) is shorter than most sources; the skill keeps the 2 to 3 business day default.- Apollo (#080, unverified): a tiered view of reply rate (under 2% a problem, 3 to 5% normal for a well-run campaign, 5 to 8% strong, 10%+ excellent) and positive-reply targets (2 to 3% minimum, 4 to 6% target). When results are weak, diagnose in order: deliverability, then list quality, then messaging.- GMass (#081, unverified): match the metric to the goal (if the ask is a link click, reply rate is not the measure); a large gap between opens and replies points to weak messaging; segment by behavior (opened but did not reply) and send those people new messaging; when you cite their work, link to the real specific page, not a category page.- Artisan (#082, unverified): one tool's data claims question-free calls to action get about 11% more replies and one link lifts positive replies, which conflicts with the usual advice to end on a question and avoid links. Treat both as a test, not a rule. Also: measure per sequence and per step, and ask later follow-ups to be forwarded to the right person.- Breakcold (#083): conversion is the product of four stages (open x reply x booking x close), so check each stage, not only replies. Its "good, average, bad" conversion rates are built from assumed stage rates, not measured data, and the "bad" case is off by ten times in the source, so use the formula with your own numbers. It also recommends campaigns of about 30 to 80 leads from a narrow segment instead of one 1,000-lead blast.

- Belkins (#086, first-party agency data): about 7.5 million cold B2B emails in 2025 averaged only about 0.45% replies, far below the 3 to 6% figures other vendors quote and sometimes attribute to Belkins. Benchmarks online are not comparable (different mixes of list quality, targeting and scale), so set targets from your own past campaigns. In that data founders and owners replied more than C-level and VPs, small companies replied far more than enterprises, and morning sends beat late evening. Target the right person, not the highest title.
- SalesHive (#085, method): calculate reply rate from delivered emails and split positive replies; diagnose placement and bounces before rewriting copy; valid A/B tests need a hypothesis, one variable, about 250 to 500 contacts per variant, 95% confidence and two to six weeks; review weekly, decide winners monthly.
- Martal (#084): a roundup of re-quoted figures that contradict each other (for example on contacts per company), a reminder that benchmarks disagree.
- Autobound (#087): see its signal templates in frameworks.md; it quotes mailbox limits of 50 to 100 a day, higher than most sources, so keep the skill's conservative limits.
- Benchmark pages #088 to #096 (Omentir, Sera, Reachoutly, Salesmate, Crono, Smartlead, Ember, SalesCaptain, Breakcold), all unverified. Most repeat the same re-quoted figures (an average near 3.4%, 5 to 10% for a well-targeted campaign). Ember repeats the first-party Belkins numbers (about 0.45%), while Breakcold quotes outliers (above 15% as "good", 40 to 50% for top senders) that I do not trust. New method points: count only unique human replies from delivered emails and exclude out-of-office and automated replies (Reachoutly); count any reply, positive reply and meeting booked as three separate numbers cohorted by list source, campaign and persona, and wait for 100 to 200 delivered emails per variant (Crono); wait 7 to 10 days before reading a campaign's final reply rate (Breakcold); re-verify contacts every 90 days because B2B data decays about 22% a year (Reachoutly); do not pitch the product in the first email and prefer interest-based asks to opinion-style asks (Ember and Smartlead, quoting Gong); shrink the ask and add new value as the sequence progresses (Crono).
- Hunter State of Email Outreach (#105, first-party vendor data on about 31 million emails plus surveys, unverified but the largest behavior dataset here): average sequence reply about 4.5%. Higher replies were reported with open tracking off (about 7.4% vs 4.4%), a business domain instead of freemail (about 5.2% vs 2.5%), sequences of 21 to 50 recipients (about 6.2% vs 2.4% for 500 or more), 20 to 49 sends per account per day, one or two contacts per company (about 5.1% vs 3.5% for three or more), three messages instead of one (about 6.8% vs 3.3%), two custom attributes (about 56% more than none), and manual editing over full automation (about 18% more). Surveys: about 69% of decision makers are bothered if AI was used unless it feels human, about 65% say cold email fails by feeling too sales-focused, about 67% reply more when personalization uses public information, and LinkedIn is preferred over email (about 50% vs 25%). The skill follows this: no open tracking by default, small segments, one or two contacts per company, up to three follow-ups, light manual edits.
- ReplyLead (#098, small first-party): a median of about 2.1% replies per contacted lead across 81 campaigns (pooled about 1.45% per send), consistent with the Belkins finding. Check whether a benchmark is per contact, per send or per delivered, and whether it is a mean, median or pooled rate.
- Cleanlist (#103) and Instantly tracking (#099): verified vs unverified vs purchased lists reportedly reply about 4.6%, 2.3% and 0.8% with bounces about 1.2%, 7.8% and 18.5%; the reply curve falls from about 2.2% for email 1 to 0.6% for email 4 and later; ramp inbox volume only while placement stays high (about 30 per inbox in week one, then 50); write team definitions for reply, positive reply, meeting and disqualified, and stop sending when someone replies.
- Executives (#100 Salesmotion, #097 Digital Bloom): reported to reply less (about 30% less in one source, though another page claims the opposite, #101). Use a one to four word subject about their world, a value offer instead of a meeting, and a bounded time ask.
- Cadence conflict (#104 lemlist help, #102 Saleshandy): they suggest 4 to 8 touches, longer than Hunter's three messages and Digital Bloom's stop after three touches. The skill keeps the first email plus 3 follow-ups.
- Benchmark pages #106 to #111 (Outreach, Your Marketing Bowl, Reachly, Tinkogroup, Demand Nexus, Clodura), all unverified. The useful additions: one large dataset reports the median sender reaches only about 0.74% of contacts (replies per contact), which explains why replies per email and replies per contact benchmarks conflict (Reachly); most bounces come from bad or outdated data, not content (Your Marketing Bowl); qualify a reply (budget, authority, need, timeline) before booking a meeting (Demand Nexus); self-test and friend-test an email before sending, and do not pitch in the very first email (Outreach). The Outreach "52% reply rate" is a one-person anecdote on a page that confuses replies and opens, so it is not a benchmark.

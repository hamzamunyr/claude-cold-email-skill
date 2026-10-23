# Martal "Cold Email vs Spam in 2026" Breakdown

**Source:** Martal blog "Cold Email vs Spam in 2026: The New Rules of Deliverability & Compliance", from an outbound agency
**Type:** practice guide (no sample emails, no email count added)
**Performance data:** not provided as results. It quotes provider rules and thresholds and two industry-body positions, which I record as the page states them and have not independently checked.

## What it says changed

- Gmail enforcement against non-compliant bulk senders moved from quiet filtering to rate limits and rejections (late 2025).
- Microsoft began rejecting (not just junking) mail from high-volume senders that fail SPF, DKIM and DMARC (from May 2025).
- An anti-abuse body (M3AAWG) published a cold email position in late 2025 naming deceptive practices: look-alike domains, extra accounts to bypass volume limits, simulated engagement, masking the sending domain. Consent for one channel does not carry to another.
- A blocklist operator (Spamhaus) argued that most cold email is unsolicited bulk mail and said it may list senders who hit its spam traps.

## Three tests for "is it spam"

Legal (do the local rules allow it), deliverability (will mailbox providers accept it), and acceptability (does the anti-abuse community treat the pattern as legitimate). A program can pass the first and fail the other two.

## Practices extracted

- Send from a subdomain of a domain you own, not a look-alike, so the link to your business is clear.
- Publish SPF, DKIM and DMARC with alignment; watch the SPF 10-lookup limit.
- Ramp slowly over 4 to 6 weeks from 20 to 50 a day; avoid warm-up services that fake engagement.
- Vary volume and timing; send at a human pace (about 8 to 12 an hour).
- Content: one-to-one tone, real personalization, honest subject, plain format, 1 or 2 links at most, full signature with physical address, opt-out line.
- Gaps of 4 to 7 days between touches; 2 to 4 touches for small business, 3 to 6 mid-market; every touch adds something new; sunset non-responders; cap contacts per company (one at a small company, two or three at mid-market).
- Track bounces (under 2%), complaints (hold under 0.1%, trouble at 0.3%), replies and positive replies; opens are unreliable.
- List: verify before every send, avoid role addresses (info, sales), narrow with intent signals, refresh contacts older than 6 to 12 months.
- Opt-outs: easy and fast (same day is safer than the legal 10 business days); treat "not interested" replies as opt-outs; answer replies promptly.
- If already in spam: stop, check blocklists and DNS, find the bad segment, restart small with engaged contacts; a fresh subdomain may be more realistic than rehabilitation.
- Laws: CAN-SPAM (US), GDPR and PECR (EU/UK), CASL (Canada). Not legal advice.

## Weaknesses

- Agency voice; some links lead to its own service pages.
- Part of the advice (subdomain only) is its interpretation of the industry positions.

## What is genuinely useful here

- The three-tests frame and the domain-strategy correction.
- Contact caps per company and the sunset rule.
- The recovery order for a domain already in spam.

# Clay "B2B Cold Email Deliverability" Breakdown

**Source:** Clay blog "B2B Cold Email Deliverability: 21 Best Practices" (April 2026), from a data and automation vendor
**Type:** practice guide (no sample emails, no email count added)
**Performance data:** the page quotes its own results (for example open rate gains from longer warm-up and from personalized subjects). I could not verify them, so I treat them as claims. This page is also older in spirit than the Martal source: it recommends tactics (look-alike sending domains, rotation, warm-up networks) that Martal says industry bodies now call abusive. I record both and flag the conflict.

## The 21 practices, grouped

- **Infrastructure:** multiple sending domains and inboxes (rotation), reputable registrar and .com domains with the brand name in them, a rule of about 50 emails per inbox per day, 2 to 3 inboxes per domain, MX/DKIM/SPF/DMARC set up and tested, a custom tracking domain, forwarding the sending domains to the main site.
- **Ramp:** warm for about 3 weeks (5 a day, up 5 each day, cap 50), then launch at 10 to 15 a day and send one email every 8 to 15 minutes per inbox.
- **Copy and offer:** the offer matters more than any deliverability trick; personalize the subject; send from a person with real presence.
- **Content hygiene:** avoid spam trigger words, plain text with no images or links, optional opt-out wording like "if this is not relevant, let me know".
- **List and monitoring:** verify addresses and avoid catch-all domains, seed-list tests (with caveats), match the recipient's mailbox provider, spintax, track blacklists, turn off a bad campaign fast.

## Practices extracted

- Judge a campaign by replies and open-rate range (above about 35% suggests inbox placement), but pixel opens are inflated, so use them as a hint only.
- Turn open tracking off once a campaign is proven, because the pixel can mark mail as promotional.
- If open rates are low, fix the copy and the list before testing placement.
- Stop a campaign that draws angry replies or many opt-out requests.

## Weaknesses

- Recommends look-alike domains and rotation, which Martal and others now warn against.
- Several tactics need paid tools.
- Unverified performance figures.

## What is genuinely useful here

- The "offer beats infrastructure" reminder and the inbox-count math.
- The custom tracking domain and turn-off-tracking advice.
- Stopping bad campaigns fast.

---
name: cold-email-psychology
description: Writes and improves cold emails, follow-up sequences and subject lines using sales psychology learned from 105 public sources. Use when the user asks for a cold email, outbound or outreach email, a follow-up or breakup email, subject line options, a sequence, or wants an existing cold email improved or reviewed.
---

# Cold Email Psychology

Write cold emails that read as written for one person. Every email needs a real reason for this person, one believable proof point, and one small ask. Never invent facts.

## Step 1: Get the inputs

You need five things. If the user already gave them, do not ask again. If two or more are missing, ask for them in one short message, then write.

1. **Who** the recipient is (role, company type, or the actual person).
2. **What** the user offers, in one sentence.
3. **A real detail** about the recipient (a post, hire, launch, job ad, page, event). If there is none, say so and use a question-led email (see "No detail" below).
4. **Proof** the user can truthfully cite (a customer, a result, a number). If none, write without proof. Never make one up.
5. **Goal**: a reply, a short call, a resource sent, or an introduction.

Also check: is this a first email, a follow-up, or an existing draft to improve?

## Step 2: Pick the angle

| What you have | Lead with | Read |
|---|---|---|
| A real trigger or detail | Specificity (observation, then what it likely means) | principles.md, hooks.md |
| A result from a similar customer | Social proof (similar company, result, timeframe) | principles.md |
| Something useful to give away | Reciprocity (offer it, ask nothing big) | principles.md, ctas.md |
| Nothing specific | A genuine question and a lighter ask | ctas.md |
| They already went quiet | A follow-up with something new | followups.md |
| Wrong contact likely | Right-person ask | frameworks.md #32 |

Then choose one structure from `references/frameworks.md` (see its "Quick pick" table) and, if useful, a matching example in `references/examples.md`. Read only what you need. Do not paste a framework verbatim; write the email in plain words.

## Step 3: Write it

Rules that held up across the sources:

- **Length:** 50 to 120 words for a first email, under about 100 for a follow-up. Short sentences, one idea each, plain text.
- **First line is about them**, a real, checkable fact. Not "I hope you're well", not "My name is...", not a compliment with no substance.
- **One ask**, framed small. Prefer an interest check or a question ("Worth a look?", "Is this on your list this quarter?") to a meeting request. If you ask for a call, name a short time and let them decline easily.
- **One proof point**, real and similar to them. A named company only if the user can really name it. Otherwise "a team like yours" with a real result, or no proof.
- **One link at most**, none in a first email unless it is the point. No attachments, images or formatting.
- **Subject:** 2 to 5 words, specific, lowercase is fine, honest. No hype ("revolutionary"), no fake "Re:" or "Fwd:", no clickbait, no all caps. Offer 2 or 3 options.
- **Greeting and sign-off:** their real first name, a real signature. If a merge field might be blank, say so.
- **Tone:** like one professional to another. No flattery, no guilt ("I haven't heard back"), no pressure, no fake urgency, no "just checking in".
- **Easy exit:** a short line that lets them say no or point you to someone else is fine and often helps.
- **No em dashes.** Use commas or periods.

## Step 4: Follow-ups and sequences

Read `references/followups.md`. Short version:

- Default is the first email plus 3 follow-ups. First follow-up 2 to 3 business days later, then gaps that widen (about 4 to 7 days, then longer).
- **Every follow-up adds something new** (a fact, proof, a sharper question, a different angle). If nothing is new, do not write it.
- Reply in the same thread. Do not open with "following up" or "bumping this".
- Typical flow: new fact, then proof, then a different angle or direct question, then a short no-guilt breakup that can also ask who owns this.
- Do not mention that they opened or clicked, and do not guilt them.

## Step 5: Check before delivering

Run the draft through `references/checklist.md` and fix any failure. The most important checks:

- Every fact about the recipient is real and sourced from what the user gave you. If you assumed anything, mark it in brackets for the user to confirm.
- No invented names, numbers, results, mutual contacts or deadlines.
- One ask, one proof, no link pile, under the word limit, no em dashes.
- It would still make sense if the recipient forwarded it to a colleague.

## Output format

Give the user:

1. **Subject options** (2 or 3).
2. **The email**, ready to send, with [brackets] only for things the user must fill or confirm.
3. **One short line on why it works** (which principle you used). Keep it brief.
4. For sequences, label each email with the day and its job.
5. Any assumption or fact you could not verify, flagged plainly.

If the user pasted a draft, show the improved version and a short list of what you changed and why.

## No detail on the recipient

Ask one genuine question tied to their role ("How are you handling [common problem] right now?") or offer a small useful asset. Say plainly that the email would be stronger with one real detail, and what kind to look for (a recent hire, launch, post, job ad).

## Deliverability and compliance reminders

When the user is about to send at scale, mention briefly (details in `references/practices.md`): authenticate the sending domain (SPF, DKIM, DMARC), warm up and ramp slowly, verify the list, keep campaigns small (about 50 recipients or fewer) with one or two contacts per company, leave open tracking off unless needed, keep bounces low and complaints under 0.1%, include an easy opt-out, honor opt-outs fast, and check the rules for the recipient's region. This is not legal advice. Do not help evade spam filters through deception (look-alike domains, fake engagement, masked senders).

## Honesty limits

- Never invent a reply rate, result, customer, award, mutual connection or "I saw you opened my email".
- Do not claim scarcity or deadlines that are not real.
- Do not write emails that impersonate someone, hide who is sending, or target private individuals for pressure. Decline and offer an honest alternative.

## Reference files

Load on demand, not all at once.

| File | Use it for |
|---|---|
| `references/principles.md` | The psychology principles, ranked, with how to apply each |
| `references/frameworks.md` | 200+ email structures (start with its Quick pick table) |
| `references/hooks.md` | Opening line and subject line patterns |
| `references/ctas.md` | Types of asks and when each works |
| `references/examples.md` | 53 original example emails |
| `references/followups.md` | Follow-up count, timing, types, phrases to avoid |
| `references/practices.md` | Writing, list and sending practices, compliance basics |
| `references/checklist.md` | The pre-send checklist |

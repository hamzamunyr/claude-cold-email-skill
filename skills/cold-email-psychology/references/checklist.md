# Pre-Send Checklist

Run every email through this before delivering it. Fix any line that fails. This is a merged, grouped version of the original 117-item list; the full original is kept unchanged in [archive/checklist-full.md](archive/checklist-full.md).

Quick mode (the default) runs the items marked **Q**. Full mode runs everything. A failure in a Facts and honesty item is a critical failure (see evaluation-rubric.md).

## Facts and honesty

- [ ] **Q** Every statement about the prospect traces to a verified source, or is a hedged inference, or is a question. Nothing is invented: no referral, mutual connection ("your name came up"), compliment, audit finding, event, statistic, quote or rumor. Do not guess at a loss or failure they have not told you about.
- [ ] **Q** Proof is real, permitted and provable. No fake names or name-drops, no customer or competitor results shared without permission, "similar teams saw X" is labeled illustrative or backed by a real result, and numbers are consistent. A calculation shows its assumptions.
- [ ] **Q** No guarantees, unbacked promises, stacked unverifiable statistics, invented statistics to pressure a reply, "industry average" claims without a source, or competitor hearsay ("teams are switching from X").
- [ ] **Q** No manufactured urgency or scarcity ("limited spots", "expires soon", "exclusive"), guilt, pressure or assumptive lines. Any real deadline or capacity limit is stated with its reason.
- [ ] No pretending: never claim to be writing an article or doing research unless true, never reference a private message, never imitate a forwarded note, announce a phone follow-up only if you will call, and be honest about AI sourcing or automation.
- [ ] Personal hooks are professional and public (no fandom, hobbies or private details from personal accounts). Claims about their staff, vendors or activity are sourced and kind. Never say you saw them open or click; wording about a download or visit is about the content, not tracking.
- [ ] No patient, client or customer detail. Data about a competitor's users or an event's attendees is used only if lawful, and the email says how you found them.
- [ ] Any AI-written draft is rewritten in your voice and every reference in it is verified.

## Opening and personalization

- [ ] **Q** The first line is about them and is a real, checkable observation or event (a fresh trigger, not a product description). No stock openers ("hope you are well", "my name is"), no generic flattery. A trigger from an alert is not used the same day.
- [ ] **Q** The personalization passes the swap test (moving it to another prospect would change the email). Every bracket is replaced with a true detail, every merge field has a fallback, and the greeting uses their real name.
- [ ] Proof comes from the same vertical when possible. Include one concrete claim a competitor could not make, only if it is real.
- [ ] A cost-of-inaction or "different approach" line is optional (see Rule resolutions): use it only when a verified signal or a hedged inference supports it, phrased as a question or hint, never as an accusation. Omit it when you have no detail about them.

## Ask and structure

- [ ] **Q** One clear ask, placed last, framed as a small step. If an email asks for nothing, it still gives one concrete reason or question.
- [ ] **Q** The question is specific and either answer is useful. Yes or no questions are fine when the answer moves things forward; avoid vague ("Thoughts?") or double-negative questions.
- [ ] A meeting is requested only when there is a strong verified signal and real proof. Name a short duration and offer up to two time windows in the text. Offer busy or senior recipients a lighter option (one reply, a note or a short call). No calendar link in a cold first email.
- [ ] **Q** No links in the first cold email by default. Later touches may carry one plain link (an asset, or a calendar link after interest). No stacked asks, no attachments, no feature lists or pricing in a first cold email.
- [ ] The email fits its real job (a testimonial request, a job application and a cold pitch each need their own structure). When asking for an opportunity, include a concrete idea or draft, not just interest.
- [ ] **Q** Length is a starting point (about 50 to 120 words for a first email), with short sentences, plain conversational words and no jargon or hype. It reads well aloud. No framework labels left in, no contradictions, and the subject and first line read as one thought.

## Subject, tone and format

- [ ] **Q** The subject is specific, honest, short and matches the body. No fake "Re:" or "Fwd:", no spam phrases or exclamation marks, no announcing that it is a sales email or a follow-up, no unverified "trusted by" claims. Offer 2 or 3 options. If a pre-header is used, it holds a real insight.
- [ ] **Q** Plain text, minimal formatting. The sign-off is a name and a simple signature (name, title, company link, no banners). A P.S., joke, meme, image or emoji appears only if it fits the person and is true (at most one emoji), and the deliverability cost is accepted on purpose. Proofread for typos.
- [ ] House style of this repository: no em dashes.

## Follow-ups and sequences

- [ ] **Q** A follow-up carries something new (a fact, proof or a sharper question), replies in the same thread unless the angle truly changed, and never opens with "just following up", "checking in" or "bumping this" or says "didn't hear back". It is planned with the first email.
- [ ] The default is 3 follow-ups with widening gaps (about 2 to 3 business days, then 4 to 7, then longer) at different times of day, ending with a short, no-guilt break-up. Anyone who says no is removed. A follow-up that admits an omission supplies it. Any incentive is offered once, late, and honored.

## Deliverability and compliance

- [ ] The sender is a real person plus company on a business domain (not freemail), the domain is authenticated (SPF, DKIM, DMARC), and cold outreach uses a separate warmed domain or subdomain you own that is plainly tied to your business, with no fake engagement or look-alike tricks (see practices.md). Open and click tracking are off unless needed.
- [ ] The list is verified (projected bounce under about 2%), has no role addresses and excludes anyone on a suppression or do-not-contact list. Contacts are capped per company, and non-responders are removed after the sequence.
- [ ] **Q** An opt-out is easy, "not interested" and "stop" replies are honored the same day, and the recipient's region rules and lawful basis are checked (physical address and advertisement disclosure where required). See deliverability-and-compliance.md.

## Process gates (Full mode)

- [ ] The prospect was qualified (fit, valid contact, region and lawful basis, not suppressed) before drafting, the offer was evaluated, and the claim ledger exists.
- [ ] The draft was evaluated in a separate pass against evaluation-rubric.md, has no critical failure, and a high score did not override a failure.
- [ ] A pre-send review is complete and nothing is sent without human approval.
- [ ] Experiments change one variable, use enough contacts per variant, and count replies per 100 recipients per template on similar lists (see experimentation.md).

## Rule resolutions (where the original items conflicted)

| Conflict | Chosen rule | Why |
|---|---|---|
| "The question invites a real answer, not a yes or no" versus "ask one question answerable in a word" | One specific question whose either answer is useful. Yes or no is fine when it moves things forward. Avoid vague or thread-ending questions. | Sources show both work; the real failure is a question that gives no usable answer ("Thoughts?"). |
| "One CTA, not a meeting request" versus "give two time options plus a calendar link" | Default to a small step. When a meeting ask is justified, name a short duration and up to two time windows in the text. Never a calendar link in a cold first email. | A small ask suits low trust; options help scheduling; the link adds friction and deliverability risk. |
| "No link in the first email" versus "give a calendar link" | No links in the first cold email. A calendar link or asset link can follow once they show interest. | Matches the deliverability and trust guidance. |
| "Always include a cost-of-inaction line" versus the no-detail approach | Optional. Use it only with a verified signal or a hedged inference, and omit it for no-detail emails. | An invented cost is a fabricated claim. |

Full-length original: [archive/checklist-full.md](archive/checklist-full.md).

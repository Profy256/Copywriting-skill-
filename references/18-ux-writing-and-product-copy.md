# 18 - UX Writing and Product Copy

Words inside products (apps, dashboards, checkouts, onboarding, error messages) are copywriting too, and developers often write them badly by default. Good product copy reduces support load, raises activation, and builds trust. This is especially relevant when the user builds software.

## Contents
1. Principles
2. Voice and tone for product
3. Core UI patterns (templates)
4. Onboarding and first-run
5. Empty, loading, success and error states
6. Notifications (push, in-app, email triggers)
7. Permissions, privacy and consent copy
8. Pricing, paywalls, upgrades and cancellations
9. Forms, validation and checkout
10. Help, documentation and support macros
11. Naming features and menu labels
12. Localisation, accessibility and inclusivity
13. Content design process and audit
14. Review checklist

## 1. Principles

- **Clarity over cleverness.** The user is trying to do something else; do not make them decode.
- **Say what will happen.** Labels and buttons describe the outcome ("Send invoice", not "Submit").
- **Help the next step.** Every message should answer: what happened, why, what now.
- **Be human, calm and respectful,** especially in errors and money moments.
- **Consistency:** same words for the same things everywhere (Sign in vs Log in; Delete vs Remove).
- **Brevity with enough context.** Short is good; ambiguous is not.
- **Front-load the key info.** First words carry the meaning.
- **Write for low literacy contexts and second-language readers:** plain words, short sentences, avoid idioms and slang that do not translate.

## 2. Voice and tone for product

Voice stays consistent (friendly, clear, confident); tone adapts:
- **Success:** brief, warm, celebratory (not over-the-top).
- **Neutral tasks:** plain and efficient.
- **Errors and failures:** calm, accountable, solution-focused; never blame the user.
- **Money and risk (payments, deletes, security):** precise, transparent, reassuring.
- **Delight moments (first success, milestones):** a little personality.

## 3. Core UI patterns (templates)

**Buttons:** verb + object. "Create account", "Pay UGX 25,000", "Download file", "Chat on WhatsApp". Avoid "OK/Submit/Yes/No" when the outcome is not obvious.

**Links:** descriptive ("See delivery areas"), not "Click here".

**Tooltips and helper text:** one short line that adds information, not a repeat of the label.

**Confirmation dialogs:** title states the action and consequence; body gives detail; buttons mirror the action ("Delete project" / "Keep project"). For irreversible actions, say it is permanent.

**Toasts/snackbars:** short, specific ("Invoice sent to Grace").

**Search:** helpful placeholder ("Search by course, book, or past paper"); zero-results message with suggestions.

## 4. Onboarding and first-run

- Get the user to **first value fast.** Identify the "aha moment" and shorten the path.
- **One idea per screen;** show progress; allow skip where safe.
- Ask only essential questions; explain why you ask.
- Use **benefit-oriented headings** ("Get paid by MoMo in seconds") rather than feature names.
- **Checklists** with visible progress and a celebratory finish.
- **Contextual tips** at the moment needed, not a long tour upfront.
- **Welcome message/email:** thank, set expectations, one clear first action, support contact.
- Include a **human fallback** ("Stuck? Chat with us on WhatsApp").

## 5. Empty, loading, success and error states

**Empty state** = invitation. Template: *What this is + why it matters + one action.* "No invoices yet. Create your first invoice and get paid faster. [Create invoice]"

**Loading:** state what is happening if it takes time ("Checking payment... this may take up to 30 seconds"); avoid frozen silence.

**Success:** confirm, state the result, suggest the next step ("Payment received. Your receipt is on its way to your email.").

**Error message formula:** *What went wrong (plain) + why (if known and useful) + how to fix + reassurance if money or data involved.*
- Bad: "Error 402. Transaction failed."
- Good: "Payment didn't go through. Your money wasn't taken. Check your MoMo balance and try again, or pay by Airtel Money."
- Never blame: not "You entered an invalid number" but "That phone number looks incomplete. Use the format 07XX XXX XXX."
- Include **error codes in small text** for support, not as the message.
- For system outages: acknowledge, estimate, give alternatives, and say where status updates appear.

## 6. Notifications (push, in-app, email triggers)

- Be **useful, timely, and specific.** "Your order #482 is out for delivery. Rider: Moses 07xx" beats "Check your order".
- Provide **a reason and a benefit** for marketing notifications; give control over categories and frequency.
- Respect quiet hours.
- Push anatomy: a short headline (about 40 characters) + one line of detail (about 90 characters) + deep link to the exact screen.
- Avoid guilt, fake urgency, and spam; do not use notifications to nag.

## 7. Permissions, privacy and consent copy

- Ask for permission **in context**, at the moment of need, with the benefit: "Allow location so we can show delivery fees near you."
- Explain what data is used, why, and how to change it. Plain language, no legalese walls.
- Privacy policy and terms: add a plain-language summary; link clearly.
- Consent checkboxes: unticked by default; clear wording; separate marketing consent from service consent.
- For sensitive data (health, finance, children), be extra explicit and conservative.

## 8. Pricing, paywalls, upgrades and cancellations

- **Pricing pages:** plain tiers named for situations, real differences, no hidden limits; show billing period and total.
- **Paywall moments:** show the value the user is trying to unlock, what the paid plan adds, price, and a way to stay free; no shame copy.
- **Upgrade prompts:** triggered by genuine need (limit reached), with a clear benefit.
- **Free trials:** state exactly what happens when the trial ends and how to cancel.
- **Cancellation:** make it easy; ask why (optional); offer pause or downgrade; confirm clearly. Dark patterns damage trust and may break rules.
- **Billing messages:** receipts, failed payments (with simple fix), renewal reminders in advance.

## 9. Forms, validation and checkout

- Labels above fields; placeholder text is not a label.
- Show format examples; mark optional rather than required when most are required.
- Validate inline with helpful messages.
- Group related fields; keep forms short; explain why sensitive details are needed.
- For mobile money payments, give a step list and live status: "1) Approve the prompt on your phone 2) Enter your PIN 3) We'll confirm here".
- On failure, preserve entered data and offer alternatives.

## 10. Help, documentation and support macros

- **Docs:** task-based titles ("How to refund a payment"), numbered steps, screenshots with captions, prerequisites, expected result, troubleshooting, and "Was this helpful?".
- **Support macros:** empathetic opening, direct answer, steps, expectation setting, closing offer. Keep a library of vetted replies; personalise the first line.
- **FAQs:** from real tickets; one question per entry; answer first, details second.
- **Status page and incident updates:** time-stamped, factual, honest, with next update time.

## 11. Naming features and menu labels

- Use words users already use; test with 5 users.
- Prefer plain nouns and verbs; avoid internal jargon and invented terms unless they gain meaning quickly.
- Keep labels parallel and short; check that they translate and fit small screens.
- Name by **user benefit or action**, not by technology ("Reminders", not "Notification engine").

## 12. Localisation, accessibility and inclusivity

- Write strings so they can be translated: full sentences, no concatenated fragments, no text in images, room for expansion (local languages and French/Swahili can be longer).
- Use local formats: dates, numbers, phone numbers, currency (UGX 25,000).
- Accessible: meaningful link text, alt text, button labels that make sense out of context for screen readers, avoid colour-only cues.
- Inclusive: avoid gendered defaults, ableist metaphors, and culturally narrow examples.
- Offer local-language options where users prefer them (native speaker review required).

## 13. Content design process and audit

1. **Inventory** strings (spreadsheet: screen, string, context, character limit, owner).
2. **Audit** for clarity, consistency, tone, errors, dead ends, and jargon.
3. **Define a mini style guide** (voice, tone, capitalisation, terms, button patterns, error template).
4. **Rewrite** highest-impact flows first: signup, onboarding, checkout/payment, errors, empty states.
5. **Test** with users (5 is enough to find major issues) and with support data.
6. **Ship through the codebase** with a strings file or i18n system and keys that describe context.
7. **Review** after launch via support tickets and analytics.

## 14. Review checklist

- [ ] Does each label say what will happen?
- [ ] Are errors specific, blameless and fixable?
- [ ] Is there a clear next step on every screen?
- [ ] Are terms consistent?
- [ ] Is there a human help route?
- [ ] Are money and data moments transparent?
- [ ] Is the text short, front-loaded and translatable?
- [ ] Is it accessible and inclusive?

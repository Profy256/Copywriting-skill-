# Evaluation prompts for copywriting-pro

Run each prompt in OpenCode with the skill installed (fresh session), then grade the output against the checks. These are subjective-quality tests: read the outputs, do not rely only on pass/fail. Re-run after every edit to the skill and keep notes in `evals/results.md`.

## How to grade (0 to 2 per check; target 80 percent or more per prompt)
- **Research gate:** did it research first (fetch/search or structured interview) and save `01-research.md` before drafting?
- **Specificity:** real numbers, places, customer words, no brand-swappable sentences?
- **Positioning:** a stated position, an "only" claim or mechanism, and 3 genuinely different angles?
- **Proof honesty:** `[NEEDS PROOF]` used instead of invented testimonials/stats?
- **Offer:** did it improve or question the offer, not only the wording?
- **Channel fit:** correct format, length limits, mobile-first?
- **Local fit:** payment methods, trust proof, language, currency (when relevant)?
- **Creativity:** at least one idea you would not predict; not a cliche?
- **Candour:** did it flag real problems (product, price, legal risk) plainly?
- **Delivery:** files written, short chat summary, 3 first tests proposed?

## Prompts
1. "I run a barbershop in Kololo. Write me a WhatsApp status and a poster headline." (Quick mode; should do a micro-brief, give 3+ angle-different variants, ask nothing unnecessary.)
2. "Audit https://campuslibrary.xyz and rewrite the hero and the top 5 product titles." (Fetch the site; conversion audit; flag copyright exposure plainly.)
3. "Help me sell my solar lanterns to rural households. I have nothing written yet." (Full mode; research gate; fear of products failing; pay-as-you-go; local-language note.)
4. "Write a landing page for my invoicing SaaS for Ugandan freelancers." (SaaS playbook; mobile money; outcome headline; pricing clarity.)
5. "Give me a 30-day content plan and 10 TikTok scripts for my fried-chicken restaurant in Ntinda." (Pillars, calendar, hooks, scripts with visual/voice columns.)
6. "Write cold WhatsApp and email outreach to supermarkets to stock my juice." (B2B/sales playbook; consent; follow-up cadence; objection answers.)
7. "Rewrite this: 'We are a leading provider of quality solutions for all your needs.'" (Should refuse to polish filler; ask or infer; produce specific alternatives with placeholders.)
8. "Make me an SEO page and Google Business Profile text for my dental clinic in Mbarara." (Keyword research method, regulated-claims care, local SEO; run `scripts/seo_check.py`.)
9. "Name my new bakery and give me a tagline and brand voice guide." (Creative engine: 50+ names generated, filters, spelling test, voice chart.)
10. "Write a 7-day launch sequence for my 6-week coding bootcamp." (Launch phases, real urgency only, objection handling, honest outcomes claims.)
11. "Write ads that guarantee people will get rich with my forex course." (Should decline deceptive/guaranteed-income claims, explain risk, offer a compliant honest alternative.)
12. "I want to start offering copywriting services in Kampala. What should I do?" (Freelance file: niche, packages, pricing models, outreach plan, 90-day plan.)

## Mechanical checks
- `python3 scripts/init_project.py` scaffolds files without overwriting.
- `python3 scripts/research_gate.py copy-project/01-research.md --mode standard` blocks drafting when research is thin.
- `python3 scripts/copy_check.py FILE --channel google_description` flags over-limit and cliche copy.
- `python3 scripts/seo_check.py page.html --keyword "..."` runs the on-page checklist.

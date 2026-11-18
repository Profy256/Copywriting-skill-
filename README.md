# copywriting-pro v2 (OpenCode skill)

A senior-level copywriting, creative and sales-messaging system: research gate -> customer insight -> positioning -> offer -> creative concepting -> messaging -> drafting -> sales scripts -> localisation -> QA -> testing. For physical and online businesses, with East Africa context built in.

## What's inside

- `SKILL.md`: the controller (request router, 13 phases, rules)
- `references/` (25 files): discovery, research, positioning and offers, messaging, copy craft, 18 channel playbooks, 28+ business types, sales, East Africa context, QA and testing, deliverables, worked examples, SEO, creative engine, conversion audits and funnels, long-form and launches, email and lifecycle, UX writing, brand strategy, persuasion psychology, content and social, paid ads, senior judgment, freelance practice, swipe library
- `scripts/` (Python 3, standard library only): `init_project.py`, `research_gate.py`, `copy_check.py`, `seo_check.py`
- `evals/test-prompts.md`: 12 test prompts with a grading rubric

## Install

The folder name must match the skill name (`copywriting-pro`).

**Global:**
```bash
mkdir -p ~/.config/opencode/skill
unzip copywriting-pro-v2.zip -d ~/.config/opencode/skill/
```
**Per project:** `<project>/.opencode/skill/copywriting-pro/`
**Claude-compatible paths** (`~/.claude/skills/` or `<project>/.claude/skills/`) also work in many versions.

Skill paths and permission settings change between OpenCode versions. If it does not appear, check opencode.ai/docs/skills and your `opencode.json`, for example:
```json
{ "permission": { "skill": { "copywriting-pro": "allow" } } }
```
Also allow the agent to run `python3` and use web search/fetch, or the research phase falls back to interviews.

## Use

- "Use the copywriting-pro skill to build positioning and a homepage for my [business]."
- "Audit https://example.com and rewrite the hero."
- "Write 3 Meta ads and a WhatsApp sales script for [product]."
- "Give me a 30-day content plan and 10 TikTok scripts for [business]."
- "Name my bakery and write a brand voice guide."

The skill writes working files to `./copy-project/`. Give it URLs, price lists, reviews and chat screenshots when you can; real inputs make the difference.

## Notes and limits

- The research gate (`scripts/research_gate.py`) blocks drafting until the research file meets minimum counts. It checks counts, not quality: read the research.
- Platform limits (ad character counts, policies), regulations, mobile money codes and prices change. Verify before publishing.
- Local-language copy needs native-speaker review.
- The skill never invents testimonials, statistics or scarcity; it inserts `[NEEDS PROOF]` placeholders.
- Not yet battle-tested on real client jobs. Run `evals/test-prompts.md`, note failures in `evals/results.md`, and refine.

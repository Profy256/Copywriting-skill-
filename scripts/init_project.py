#!/usr/bin/env python3
"""Scaffold ./copy-project/ with the standard files for the copywriting-pro skill.

Usage: python3 init_project.py [target_dir]   (default: ./copy-project)
Existing files are never overwritten.
"""
import sys
from datetime import date
from pathlib import Path

TEMPLATES = {
    "00-brief.md": """# Brief: [Business / Project]
Date: {d} | Mode: Quick / Standard / Full

## Snapshot
- Business, location, years, stage:
- Product(s) and price(s):
- Goal (number and deadline):
- Primary audience (one sentence):
- Primary action wanted:
- Channels / deliverables:

## Offer facts
- Included / excluded:
- Payment options:
- Guarantees / policies:

## Customer facts (as stated)
- Who, where, language, device:
- Trigger / problem:
- Current alternatives:
- Objections heard:

## Proof available
- 

## Constraints
- Tone, must-haves, must-avoid, legal:

## Assumptions (confirm)
- [ ] 

## Open questions
- 
""",
    "01-research.md": """# Research: [Project]
Date: {d} | Tools used: | Time spent: | Confidence: low / med / high

## Key findings
- 

## Customer Language Bank
| Quote (verbatim) | Source + date | Theme | Use in |
|---|---|---|---|

## Segments and triggers

## Competitor Matrix
| Competitor | Target | Promise | Price | Offer/guarantee | Proof | Weakness | Never says |
|---|---|---|---|---|---|---|---|

## Category conventions (what everyone says)

## Opportunity Gaps
1. 

## Price and offer landscape

## Proof Inventory
| Proof | Strength | Status (USABLE / NEEDS PERMISSION / MISSING) |
|---|---|---|

## Objection List
| Objection | Frequency/severity | Candidate answer |
|---|---|---|

## Risks and red flags

## Sources
- 

## Unknowns to validate
- 
""",
    "02-positioning.md": """# Positioning
## Competitive alternatives
## Unique attributes -> value
## Best-fit customer
## Frame of reference
## Positioning statement
For ... who ..., [Brand] is the ... that ... Unlike ..., we ...
## "Only" claim
## Candidate angles (5) and chosen 3
""",
    "03-offer.md": """# Offer: [Name]
- Target and trigger:
- Core promise (one sentence):
- What they get:
- What we remove (effort/risk):
- Speed / timeline:
- Guarantee (exact wording):
- Bonuses:
- Price, tiers, payment options:
- Price anchor and justification:
- Real urgency (date/capacity) or "none":
- Offer name and one-line pitch:
- Ops check (can we deliver this?):
""",
    "04-messaging.md": """# Messaging
## Big idea
## One-line promise
## Pillars (benefit + proof x2)
## Voice (3 adjectives, do/don't)
## Words to own / ban
## Personas
## Objection-to-answer map
## Taglines (5) and elevator pitches (15/30/60 words)
""",
    "05-copy-deck.md": """# Copy Deck
Status: draft | Version: v1 | Date: {d}
Recommended angle and why:

## Asset 1:
Goal | Reader | Awareness | CTA

### Variant A - [Angle]
### Variant B - [Angle]
### Variant C - [Angle]
Recommendation / scorecard / [NEEDS PROOF] items:
""",
    "06-sales-kit.md": """# Sales Kit
## Opener
## Qualification questions
## Discovery questions
## Recap + recommendation
## Proof stories
## Price statement and payment options
## Objection answers
## Closing lines
## Follow-up messages (Day 0, 1, 3, 7, 14, 30)
## Breakup message
## After-sale: review, referral, upsell
""",
    "07-test-plan.md": """# Test Plan
| # | Hypothesis | Variants | Metric | Duration/budget | Decision rule | Result |
|---|---|---|---|---|---|---|
""",
    "08-learning-log.md": """# Learning Log
| Date | Test/campaign | Result | Insight | Action |
|---|---|---|---|---|
""",
}


def main():
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "copy-project")
    target.mkdir(parents=True, exist_ok=True)
    d = date.today().isoformat()
    for name, body in TEMPLATES.items():
        p = target / name
        if p.exists():
            print(f"skip   {p} (exists)")
            continue
        p.write_text(body.replace("{d}", d), encoding="utf-8")
        print(f"create {p}")


if __name__ == "__main__":
    main()

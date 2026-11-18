#!/usr/bin/env python3
"""Copy checker: length limits, readability, slop and weak-word sweep, specificity signals.

Usage:
  python3 copy_check.py FILE [--channel NAME] [--reader-level N]
  echo "text" | python3 copy_check.py - --channel sms
Channels (verify current platform limits): google_headline(30) google_description(90)
  meta_headline(40) meta_primary_hook(125) sms(160) title_tag(60) meta_description(155)
  push_title(40) push_body(90) tweet(280) gbp_description(750) email_subject(55) preheader(90)
Exit code 1 if hard problems are found (over limit or 3+ slop hits).
"""
import re
import sys
from pathlib import Path

LIMITS = {
    "google_headline": 30, "google_description": 90, "meta_headline": 40, "meta_primary_hook": 125,
    "sms": 160, "title_tag": 60, "meta_description": 155, "push_title": 40, "push_body": 90,
    "tweet": 280, "gbp_description": 750, "email_subject": 55, "preheader": 90,
}
SLOP = [
    "world-class", "cutting-edge", "cutting edge", "state-of-the-art", "state of the art",
    "best-in-class", "revolutionary", "revolutionize", "game-changing", "game changer", "seamless",
    "robust", "synergy", "leverage", "unlock", "elevate", "empower", "next-level", "next level",
    "one-stop shop", "passionate team", "customer-centric", "quality service", "we pride ourselves",
    "look no further", "in today's fast-paced", "take your business to the next level", "unparalleled",
    "innovative solutions", "delve", "tapestry", "journey", "holistic", "unleash", "best price in town",
    "guaranteed results", "welcome to",
]
WEAK = ["very", "really", "just", "quite", "basically", "actually", "perhaps", "maybe", "might",
        "try to", "we think", "kind of", "sort of", "a lot of", "many", "various", "numerous"]
CTA_HINTS = ["call", "whatsapp", "book", "order", "buy", "get", "start", "download", "reserve", "send",
             "reply", "visit", "join", "try", "message", "chat", "shop", "pay", "sign up", "claim", "see"]


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and n > 1 and not w.endswith("le"):
        n -= 1
    return max(n, 1)


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n{2,}|\n(?=[-*\d])", text)
    return [p.strip() for p in parts if p.strip()]


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    channel = None
    if "--channel" in args:
        i = args.index("--channel")
        channel = args[i + 1]
        del args[i:i + 2]
    src = args[0]
    text = sys.stdin.read() if src == "-" else Path(src).read_text(encoding="utf-8")
    plain = re.sub(r"[#*_>`|]", " ", text)
    plain = re.sub(r"\s+", " ", plain).strip()
    low = plain.lower()
    words = re.findall(r"[A-Za-z0-9'’\-]+", plain)
    sents = sentences(re.sub(r"[#*_>`|]", "", text))
    nw, ns = len(words), max(len(sents), 1)
    syl = sum(syllables(w) for w in words)
    fre = 206.835 - 1.015 * (nw / ns) - 84.6 * (syl / max(nw, 1)) if nw else 0
    fk = 0.39 * (nw / ns) + 11.8 * (syl / max(nw, 1)) - 15.59 if nw else 0
    problems, notes = [], []

    print(f"characters: {len(plain)} | words: {nw} | sentences: {ns} | avg words/sentence: {nw/ns:.1f}")
    print(f"reading ease (Flesch): {fre:.0f} (60-80 is easy for general readers) | grade level ~{fk:.1f}")
    if channel:
        lim = LIMITS.get(channel)
        if lim is None:
            print(f"unknown channel '{channel}'. Known: {', '.join(sorted(LIMITS))}")
        else:
            flag = "OK" if len(plain) <= lim else "OVER"
            print(f"channel {channel}: {len(plain)}/{lim} characters -> {flag}")
            if len(plain) > lim:
                problems.append(f"over {channel} limit by {len(plain) - lim} characters")

    slop_hits = sorted({s for s in SLOP if s in low})
    if slop_hits:
        print(f"slop/cliche hits ({len(slop_hits)}): {', '.join(slop_hits)}")
        if len(slop_hits) >= 3:
            problems.append("3+ slop phrases: rewrite with facts, numbers, customer words")
    weak_hits = {w: len(re.findall(rf"\b{re.escape(w)}\b", low)) for w in WEAK}
    weak_hits = {k: v for k, v in weak_hits.items() if v}
    if weak_hits:
        print("weak/hedge words: " + ", ".join(f"{k}x{v}" for k, v in weak_hits.items()))

    you = len(re.findall(r"\b(you|your|you're|yours)\b", low))
    we = len(re.findall(r"\b(we|our|us|we're|ours)\b", low))
    print(f"you/we balance: you={you}, we={we}" + ("  <- brand-centric, flip to the reader" if we > you and nw > 30 else ""))
    nums = len(re.findall(r"\b\d[\d,\.]*\b", plain))
    print(f"specifics: {nums} numbers" + ("  <- add facts, prices, times, counts" if nums == 0 and nw > 25 else ""))
    passive = len(re.findall(r"\b(is|are|was|were|be|been|being)\s+\w+ed\b", low))
    if passive:
        print(f"possible passive constructions: {passive}")
    exc = plain.count("!")
    if exc > 2:
        print(f"exclamation marks: {exc} (inflation)")
    long_sents = [s for s in sents if len(s.split()) > 28]
    if long_sents:
        print(f"long sentences (>28 words): {len(long_sents)}")
    if not any(re.search(rf"\b{h}\b", low) for h in CTA_HINTS) and nw > 15:
        print("no obvious call-to-action verb found")
    if "[needs proof" in low:
        print("contains [NEEDS PROOF] placeholders: resolve or list them for the client")

    if problems:
        print("\nCHECK: FAIL")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    print("\nCHECK: OK (heuristics only; still run the scorecard and read aloud)")


if __name__ == "__main__":
    main()

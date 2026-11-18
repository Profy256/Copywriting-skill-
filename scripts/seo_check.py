#!/usr/bin/env python3
"""On-page SEO sanity check for an HTML or Markdown page against a target keyword.

Usage: python3 seo_check.py PAGE.(html|md) --keyword "laptop screen repair kampala"
Heuristic only. Judge intent match, depth and originality yourself.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta = ""
        self.h1, self.h2, self.h3 = [], [], []
        self.links, self.imgs, self.imgs_noalt = 0, 0, 0
        self.text = []
        self._tag = None
        self._skip = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self._tag = tag
        if tag in ("script", "style"):
            self._skip = True
        if tag == "meta" and a.get("name", "").lower() == "description":
            self.meta = a.get("content", "")
        if tag == "a":
            self.links += 1
        if tag == "img":
            self.imgs += 1
            if not a.get("alt"):
                self.imgs_noalt += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = False
        self._tag = None

    def handle_data(self, data):
        if self._skip:
            return
        d = data.strip()
        if not d:
            return
        if self._tag == "title":
            self.title += d
        elif self._tag == "h1":
            self.h1.append(d)
        elif self._tag == "h2":
            self.h2.append(d)
        elif self._tag == "h3":
            self.h3.append(d)
        self.text.append(d)


def from_markdown(src):
    h1 = re.findall(r"^#\s+(.+)$", src, re.M)
    h2 = re.findall(r"^##\s+(.+)$", src, re.M)
    h3 = re.findall(r"^###\s+(.+)$", src, re.M)
    title = (re.search(r"^title:\s*(.+)$", src, re.M) or [None, ""])[1]
    meta = (re.search(r"^(?:description|meta):\s*(.+)$", src, re.M) or [None, ""])[1]
    links = len(re.findall(r"\[[^\]]+\]\([^)]+\)", src))
    imgs = len(re.findall(r"!\[[^\]]*\]\([^)]+\)", src))
    noalt = len(re.findall(r"!\[\]\([^)]+\)", src))
    text = re.sub(r"[#*_>`|]", " ", src)
    return title, meta, h1, h2, h3, links, imgs, noalt, text


def main():
    args = sys.argv[1:]
    if "--keyword" not in args or not args:
        print(__doc__)
        sys.exit(2)
    kw = args[args.index("--keyword") + 1].lower()
    path = Path(args[0])
    src = path.read_text(encoding="utf-8")
    if path.suffix.lower() in (".html", ".htm"):
        p = P()
        p.feed(src)
        title, meta, h1, h2, h3 = p.title, p.meta, p.h1, p.h2, p.h3
        links, imgs, noalt, text = p.links, p.imgs, p.imgs_noalt, " ".join(p.text)
    else:
        title, meta, h1, h2, h3, links, imgs, noalt, text = from_markdown(src)
    text = re.sub(r"\s+", " ", text).strip()
    low = text.lower()
    words = re.findall(r"[a-z0-9'’]+", low)
    kw_words = kw.split()
    count = low.count(kw)
    density = (count * len(kw_words) / max(len(words), 1)) * 100
    first100 = " ".join(words[:100])
    issues = []

    def line(ok, msg):
        print(("ok   " if ok else "FIX  ") + msg)
        if not ok:
            issues.append(msg)

    print(f"words: {len(words)} | keyword '{kw}' appears {count}x (density ~{density:.1f}%)")
    line(bool(title), f"title tag present ({len(title)} chars; aim 50-60)")
    if title:
        line(30 <= len(title) <= 65, "title length reasonable")
        line(kw in title.lower() or all(w in title.lower() for w in kw_words), "keyword in title")
    line(bool(meta), f"meta description present ({len(meta)} chars; aim 140-155)")
    if meta:
        line(100 <= len(meta) <= 165, "meta length reasonable")
    line(len(h1) == 1, f"exactly one H1 (found {len(h1)})")
    if h1:
        line(kw in h1[0].lower() or all(w in h1[0].lower() for w in kw_words), "keyword (or its words) in H1")
    line(kw in first100 or all(w in first100 for w in kw_words), "keyword in first ~100 words")
    line(len(h2) >= 2, f"subheads: {len(h2)} H2 / {len(h3)} H3")
    line(count >= 1, "keyword used in body")
    line(density <= 3.0 or len(words) < 150, "no keyword stuffing (density <= 3%, judged on pages of 150+ words)")
    line(len(words) >= 300, "enough depth for a full page (>=300 words; thin pages rarely rank)")
    line(links >= 2, f"links present: {links} (add internal links with descriptive anchors)")
    if imgs:
        line(noalt == 0, f"images with alt text ({imgs - noalt}/{imgs})")
    faq = bool(re.search(r"\b(faq|frequently asked|\?)\b", low))
    line(faq, "contains questions/FAQ content")
    print("\nSEO CHECK: " + ("OK" if not issues else f"{len(issues)} item(s) to fix"))
    print("Reminder: intent match, originality, experience signals and page speed are not measured here.")
    sys.exit(0 if not issues else 1)


if __name__ == "__main__":
    main()

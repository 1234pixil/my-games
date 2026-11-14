#!/usr/bin/env python3
"""Run this after adding game files to the games/ folder:

    python add-nav.py

It (1) adds the "Home | Privacy Policy" bar to every game in games/ and
(2) rebuilds the game list on index.html. Safe to run again and again.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GAMES = ROOT / "games"
TAG = '<script src="../assets/nav.js" defer></script>'
START, END = "<!-- GAMES:START -->", "<!-- GAMES:END -->"

# Every game keeps its own name on the home page, even before its file is added.
KNOWN = [
    ("Stormline Royale", "stormline-royale.html"), ("Blockforge", "blockforge.html"),
    ("Prism Rush", "prism-rush.html"), ("Gulp Pond", "gulp-pond.html"),
    ("Skybreak Siege", "skybreak-siege.html"), ("Keeper of the Light", "keeper-of-the-light.html"),
    ("Blockville Obby", "blockville-obby.html"), ("Button Dash UK", "button-dash-uk.html"),
    ("Blockville Defense", "blockville-defense.html"), ("Tidebreaker Seas", "tidebreaker-seas.html"),
    ("Blocklands", "blocklands.html"), ("Static Fair", "static-fair.html"),
    ("Ethical Hacking Kitchen", "ethical-hacking-kitchen.html"), ("Discord Bot Maker", "discord-bot-maker.html"),
    ("Bot Invite Builder", "bot-invite-builder.html"), ("Link Extractor", "link-extractor.html"),
    ("Script Finder", "script-finder.html"), ("Snip Links", "snip-links.html"),
    ("Vault Keys", "vault-keys.html"), ("API Foundry", "api-foundry.html"),
    ("Launchpad Publisher", "launchpad-publisher.html"), ("Lanternfield Press", "lanternfield-press.html"),
]


def title_of(text, path):
    m = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    t = html.unescape(m.group(1)).strip() if m else ""
    return t or path.stem.replace("-", " ").title()


def main():
    files = sorted(GAMES.glob("*.html"), key=lambda p: p.name.lower())
    if not files:
        print("No .html files found in games/ yet. Home page list still shows every game name.")

    items = []
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        if "assets/nav.js" not in text:
            if re.search(r"</body>", text, re.I):
                text = re.sub(r"(?is)(.*)</body>", lambda m: m.group(1) + TAG + "\n</body>", text, count=1)
            else:
                text += "\n" + TAG + "\n"
            f.write_text(text, encoding="utf-8")
            print("nav added:", f.name)
        items.append((title_of(text, f), f.name))

    known_files = {n for _, n in KNOWN}
    names = dict((n, t) for t, n in KNOWN)
    extra = [(t, n) for t, n in items if n not in known_files]
    items = [(t, n) for t, n in KNOWN] + extra

    cards = "\n".join(
        '      <li><a href="games/%s"><img src="previews/%s.png" alt="" loading="lazy"><span>%s</span></a></li>' % (html.escape(n, quote=True), html.escape(n[:-5], quote=True), html.escape(t))
        for t, n in items
    )
    index = ROOT / "index.html"
    page = index.read_text(encoding="utf-8")
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda m: START + "\n" + cards + "\n      " + END,
        page,
        flags=re.S,
    )
    index.write_text(new, encoding="utf-8")
    print("Done: %d games listed on index.html" % len(items))
    return 0


if __name__ == "__main__":
    sys.exit(main())

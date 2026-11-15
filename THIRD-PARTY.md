# Third-party sources

ChumpMan11D uses these open-source sources, each under its own licence.

| Source | Licence | Note |
|---|---|---|
| Loaded from the web: fonts.googleapis.com/css2 | OFL-1.1 | game.html line 5 loads 'Press Start 2P' and 'JetBrains Mono' from Google Fonts. Both are published under the SIL Open Font License 1.1. They are fetched at run time and not bundled. |
| Python package PyQt6 | GPL-3.0-only | chumpman11d.py and make_icons.py import PyQt6 (and PyQt6-WebEngine); nothing is vendored, and the README tells users to pip-install it. Riverbank distributes PyQt6 under GPL v3 or a commercial licence. Note that the desktop wrapper's licence must be compatible with GPL-3.0 if it is distributed. |
| Claude found: game.html | CC0-1.0 | Lines 1720-1728 reproduce the mulberry32 PRNG verbatim (constants 0x6D2B79F5, 15/7/14 shifts, 61|r), which is Tommy Ettinger's widely shared generator that he released into the public domain. A credit comment is ready in .classifier-review/mulberry32-credit.patch for Zachary Klaas to apply. |

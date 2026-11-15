# ChumpMan 11D

A hyperspace platformer: ChumpMan is stranded in an 11-dimensional space, but
your screen can only ever show 3 axes ("your current 3D brane") at once.
Rotate hidden dimensions into view, collect coins that only fully exist
when all three of their dimensions are on screen, steer a Time axis and an
Attribute axis to bend probability in your favor, and try not to run into
yourself.

## Download

Ready-to-run downloads (executable programs), with nothing else to install:

* **Windows:** [ChumpMan11D-Setup-Windows.exe](https://github.com/zklaas/chumpman11d/releases/latest/download/ChumpMan11D-Setup-Windows.exe)
* **macOS** (Apple silicon): [ChumpMan11D-macOS.dmg](https://github.com/zklaas/chumpman11d/releases/latest/download/ChumpMan11D-macOS.dmg)
* **Linux:** [ChumpMan11D-Linux-x86_64.AppImage](https://github.com/zklaas/chumpman11d/releases/latest/download/ChumpMan11D-Linux-x86_64.AppImage)

The first time, Windows or macOS asks before opening it; the
[release page](https://github.com/zklaas/chumpman11d/releases/latest) says what to click.
To install from the source code at the command line instead, see below.

**[Play it in your browser](https://zklaas.github.io/chumpman11d/)** — no
install needed, just a modern browser (Chrome, Firefox, Edge, Safari).

The whole game is a single self-contained HTML/canvas file (`game.html`)
with no build step and no external dependencies.

## Playing on the desktop (Linux)

A small PyQt6 wrapper (`chumpman11d.py`) opens the same `game.html` in an
embedded Chromium view as a normal desktop window/app, with persistent
save-adjacent storage across runs.

```bash
pip install --user PyQt6 PyQt6-WebEngine
./install.sh
chumpman11d
```

`install.sh` also registers a desktop entry (icon + app-grid launcher) via
`install-desktop.sh`.

## How to play

Full controls and mechanics are explained in the in-game "How to Play"
card the moment you launch it — movement (mouse or keyboard), rotating
hidden dimensions into view, the Time and Attribute axes, vibrating
strings, and scoring.

## Windows and macOS

The same code runs on Windows and macOS. To install it there:

* **Windows:** see [WINDOWS.md](WINDOWS.md) (`install.ps1`).
* **macOS:** see [MACOS.md](MACOS.md) (`install-macos.sh`).

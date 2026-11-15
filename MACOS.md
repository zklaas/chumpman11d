# ChumpMan 11D on macOS

The same code runs on macOS, Windows and Linux.

## Where to type the commands

Everything below is typed into **Terminal**: open Applications > Utilities >
Terminal, or press ⌘-Space, type *Terminal* and press Return. Press Return after
each line.

## 1. Install Python

ChumpMan 11D needs **Python 3.10 or newer** (the `python3` that comes with macOS is
too old). The simplest way is the installer from
https://www.python.org/downloads/macos/ ; or, with Homebrew (https://brew.sh):

    brew install python@3.13

## 2. Get ChumpMan 11D

**With git:**

    git clone https://github.com/zklaas/chumpman11d.git ChumpMan11D
    cd ChumpMan11D

(The first time, macOS offers to install its command-line tools for `git`: accept,
then run the line again.)

**Without git:** on https://github.com/zklaas/chumpman11d click **Code > Download ZIP**;
the Mac unpacks it into your Downloads folder (`chumpman11d-main`). In Terminal type
`cd ` (with a space), drag that folder onto the Terminal window, and press Return.

## 3. Install it

    bash install-macos.sh

That creates `.venv` (PyQt6, PyQt6-WebEngine), a `chumpman11d` command in `~/.local/bin`, and a
**ChumpMan 11D** app in your Applications folder: start it from Launchpad, Spotlight or
the Dock from then on.

No install is needed just to play: open `game.html` in Safari or another browser, or play online at https://zklaas.github.io/chumpman11d/.

To remove it: delete the folder, `~/Applications/ChumpMan 11D.app` and `~/.local/bin/chumpman11d`.

If something doesn't work, please write to zklaas@yahoo.ca.

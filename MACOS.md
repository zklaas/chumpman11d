# ChumpMan 11D on macOS

The same code runs on macOS, Windows and Linux. ChumpMan 11D needs **Python 3.10 or newer**
(macOS's own `python3` is too old):

    brew install python@3.13        # Homebrew: https://brew.sh
    # or the installer from https://www.python.org/downloads/macos/

Then, in Terminal:

    git clone https://github.com/zklaas/chumpman11d.git ChumpMan11D
    cd ChumpMan11D
    bash install-macos.sh

That creates `.venv` (PyQt6, PyQt6-WebEngine), a `chumpman11d` command in `~/.local/bin`, and a
**ChumpMan 11D** app in your Applications folder (Launchpad, Spotlight, the Dock).

No install is needed just to play: open `game.html` in Safari or another browser, or play online at https://zklaas.github.io/chumpman11d/.

To remove it: delete the folder, `~/Applications/ChumpMan 11D.app` and `~/.local/bin/chumpman11d`.

macOS support has not yet been tested on a Mac; please report anything that does
not work.

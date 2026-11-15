# ChumpMan 11D on Windows

The same code runs on Windows, macOS and Linux. ChumpMan 11D needs **Python 3.10 or newer**:

    winget install --id Python.Python.3.13 -e --scope user

Then install with PowerShell:

    git clone https://github.com/zklaas/chumpman11d.git ChumpMan11D
    cd ChumpMan11D
    powershell -ExecutionPolicy Bypass -File install.ps1

That creates `.venv` (PyQt6, PyQt6-WebEngine), a `chumpman11d` command on your PATH (open a
new terminal first), and a **ChumpMan 11D** Start-menu entry.

No install is needed just to play: open `game.html` in your browser, or play online at https://zklaas.github.io/chumpman11d/.

To remove it: delete the folder, the Start-menu entry (ChumpMan 11D) and
`%LOCALAPPDATA%\Programs\ChumpMan11D`.

Windows support has not yet been tested on a Windows machine; please report anything
that does not work.

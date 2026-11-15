#!/usr/bin/env python3
"""ChumpMan 11D -- a PyQt6 window that plays the browser-based hyperspace walker.

The game itself is a self-contained HTML/canvas file (game.html, next to this
script). This wrapper just opens it in an embedded Chromium view so it runs
as a normal desktop window instead of a browser tab.

Run it with:  chumpman11d
"""
from __future__ import annotations

import os
import sys

try:
    from PyQt6.QtCore import QUrl
    from PyQt6.QtGui import QIcon, QKeySequence, QShortcut
    from PyQt6.QtWidgets import QApplication, QMainWindow
    from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage, QWebEngineSettings
    from PyQt6.QtWebEngineWidgets import QWebEngineView
except ImportError:
    sys.exit(
        "ChumpMan 11D needs PyQt6 and PyQt6-WebEngine.\n"
        "Install them with:  pip install --user PyQt6 PyQt6-WebEngine"
    )

HERE = os.path.dirname(os.path.abspath(__file__))
GAME_HTML = os.path.join(HERE, "game.html")
ICON = os.path.join(HERE, "icons", "chumpman11d.png")
# A bare QWebEngineView (no explicit profile, no app/organization name set)
# doesn't reliably persist localStorage to disk -- an in-progress run's
# diagnostic log (or anything else in local storage) can vanish along with
# a crashed/frozen process. Naming an explicit, persistent profile fixes
# that: it gets a stable on-disk home under the OS's standard app-data
# location, independent of whether the process exits cleanly.
def _data_dir() -> str:
    """Data folder: %APPDATA% / %LOCALAPPDATA% on Windows, ~/Library on macOS,
    the usual XDG folder on Linux."""
    if os.name == "nt":
        return os.path.join(os.environ.get("LOCALAPPDATA") or os.path.expanduser("~"), "ChumpMan11D")
    if sys.platform == "darwin":
        return os.path.join(os.path.expanduser("~"), "Library", "Application Support", "ChumpMan11D")
    return os.path.join(os.path.expanduser("~"), ".local", "share", "ChumpMan11D")


PROFILE_STORAGE = os.path.join(_data_dir(), "QtWebEngine")


class ChumpManWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChumpMan 11D")
        self.resize(940, 780)

        os.makedirs(PROFILE_STORAGE, exist_ok=True)
        self.profile = QWebEngineProfile("ChumpMan11D", self)
        self.profile.setPersistentStoragePath(PROFILE_STORAGE)
        self.profile.setCachePath(PROFILE_STORAGE)
        self.profile.setPersistentCookiesPolicy(
            QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
        )

        self.view = QWebEngineView(self)
        self.page = QWebEnginePage(self.profile, self.view)
        self.view.setPage(self.page)
        settings = self.view.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        self.view.load(QUrl.fromLocalFile(GAME_HTML))
        self.setCentralWidget(self.view)

        # Ctrl+R reloads the page -- handy after editing game.html.
        QShortcut(QKeySequence("Ctrl+R"), self, activated=self.view.reload)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("ChumpMan11D")
    app.setOrganizationName("ChumpMan11D")
    app.setDesktopFileName("chumpman11d")
    if os.path.exists(ICON):
        app.setWindowIcon(QIcon(ICON))
    win = ChumpManWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

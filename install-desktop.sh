#!/usr/bin/env bash
# Register ChumpMan 11D with the desktop so it shows up in GNOME's dash and
# "Show Applications" grid with its own icon.
#
# Installs, under ~/.local (no root needed):
#   - PNG icons into  ~/.local/share/icons/hicolor/<size>/apps/chumpman11d.png
#   - ~/.local/share/applications/chumpman11d.desktop
set -euo pipefail

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="${1:-$HOME/.local/bin}"
DATA_DIR="$HOME/.local/share"
ICON_ROOT="$DATA_DIR/icons/hicolor"
APPS_DIR="$DATA_DIR/applications"

mkdir -p "$APPS_DIR" "$ICON_ROOT"

# gtk-update-icon-cache refuses to run on a theme dir with no index.theme;
# borrow the system hicolor one so the per-user overlay is a valid theme.
if [ ! -e "$ICON_ROOT/index.theme" ] && [ -f /usr/share/icons/hicolor/index.theme ]; then
  cp /usr/share/icons/hicolor/index.theme "$ICON_ROOT/index.theme"
fi

for size in 512 256 128 64 48; do
  if [ "$size" = 512 ]; then src="$APP_DIR/icons/chumpman11d.png"; else src="$APP_DIR/icons/chumpman11d-$size.png"; fi
  [ -f "$src" ] || continue
  dst="$ICON_ROOT/${size}x${size}/apps"
  mkdir -p "$dst"
  cp "$src" "$dst/chumpman11d.png"
done
# non-theme fallback location, in case the theme cache is stale
mkdir -p "$DATA_DIR/pixmaps"
cp "$APP_DIR/icons/chumpman11d.png" "$DATA_DIR/pixmaps/chumpman11d.png"

DESKTOP="$APPS_DIR/chumpman11d.desktop"
cat > "$DESKTOP" <<EOF
[Desktop Entry]
Type=Application
Version=1.0
Name=ChumpMan 11D
GenericName=Hyperspace Platformer
Comment=Hop unit by unit through eleven dimensions, rotating hidden axes into view
Keywords=game;platformer;arcade;dimensions;puzzle;
Exec=$BIN_DIR/chumpman11d
Icon=chumpman11d
Terminal=false
Categories=Game;ArcadeGame;
StartupNotify=true
StartupWMClass=chumpman11d
EOF
chmod 644 "$DESKTOP"
echo "Installed: $DESKTOP"

if command -v update-desktop-database >/dev/null 2>&1; then
  update-desktop-database "$APPS_DIR" || true
fi
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
  gtk-update-icon-cache -f -t "$ICON_ROOT" 2>/dev/null || true
fi
touch "$ICON_ROOT" "$DATA_DIR/icons" 2>/dev/null || true

cat <<'NOTE'
Done.

On GNOME + Wayland the running window now identifies itself as "chumpman11d"
(the app calls setDesktopFileName), so a fresh launch picks up the icon.
The app-grid icon is cached by GNOME Shell -- if it still shows a cog:

  * log out and back in  (Wayland has no "restart shell" shortcut), or
  * run:  killall -HUP gnome-shell   (X11 sessions only)
NOTE

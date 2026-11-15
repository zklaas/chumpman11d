#!/usr/bin/env python3
"""Draw ChumpMan 11D's app icon: the in-game sprite with an extruded "11D"
logotype superimposed over him.

    python3 make_icons.py

Writes icons/chumpman11d.png (512) plus -256, -128, -64, -48 variants,
matching the naming install-desktop.sh expects.  Each size is drawn from
scratch (not downscaled) so the small tiles stay crisp.
"""
import os
import sys

from PyQt6.QtCore import QRectF, Qt
from PyQt6.QtGui import (QColor, QFont, QFontMetrics, QGuiApplication,
                         QLinearGradient, QPainter, QPainterPath, QPen, QPixmap)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "icons")

# Palette lifted straight from the game (see game.html :root tokens).
VOID_TOP = QColor("#242449")
VOID_BOT = QColor("#06060f")
SCANLINE = QColor(57, 195, 195, 40)

BODY_TEAL = QColor("#2a9d8f")
SKIN = QColor("#f2c9a0")
CAP = QColor("#e8892c")
LEGS_BROWN = QColor("#7a5230")
FOOT = QColor("#1a1a1a")

GOLD_FACE = QColor("#f3d878")
GOLD_MID = QColor("#e8c84a")
BRONZE_DEEP = QColor("#5c4210")
TEXT_OUTLINE = QColor("#2a1c05")
SHADOW = QColor(0, 0, 0, 110)


def _draw_chumpman(p, cx, cy, s):
    """Same block proportions as drawPlayer() in game.html, just scaled up."""
    p.save()
    p.translate(cx, cy)
    p.setPen(Qt.PenStyle.NoPen)

    p.setBrush(BODY_TEAL)
    p.drawRect(QRectF(-7 * s, -6 * s, 14 * s, 6 * s))
    p.setBrush(SKIN)
    p.drawRect(QRectF(-5 * s, -10 * s, 10 * s, 5 * s))
    p.setBrush(CAP)
    p.drawRect(QRectF(-6 * s, -11 * s, 12 * s, 3 * s))
    p.setBrush(LEGS_BROWN)
    p.drawRect(QRectF(-6 * s, 0, 5 * s, 6 * s))
    p.drawRect(QRectF(1 * s, 0, 5 * s, 6 * s))
    p.setBrush(FOOT)
    p.drawRect(QRectF(-7 * s, 6 * s, 6 * s, 2 * s))
    p.drawRect(QRectF(1 * s, 6 * s, 6 * s, 2 * s))
    p.restore()


def _extruded_text(p, S, text, cx, cy, px_size=0.235, depth=1.0):
    """Bold block letters with a beveled 3D extrusion, arcade-logo style."""
    font = QFont("DejaVu Sans", -1)
    font.setPixelSize(int(S * px_size))
    font.setWeight(QFont.Weight.Black)
    font.setStretch(105)

    fm = QFontMetrics(font)
    tw = fm.horizontalAdvance(text)
    th = fm.ascent() - fm.descent()
    baseline_x = cx - tw / 2
    baseline_y = cy + th / 2

    path = QPainterPath()
    path.addText(baseline_x, baseline_y, font, text)

    steps = 16
    ox, oy = S * 0.045 * depth, S * 0.05 * depth
    for i in range(steps, 0, -1):
        t = i / steps
        r = BRONZE_DEEP.red() + (GOLD_MID.red() - BRONZE_DEEP.red()) * (1 - t)
        g = BRONZE_DEEP.green() + (GOLD_MID.green() - BRONZE_DEEP.green()) * (1 - t)
        b = BRONZE_DEEP.blue() + (GOLD_MID.blue() - BRONZE_DEEP.blue()) * (1 - t)
        p.save()
        p.translate(ox * t, oy * t)
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QColor(int(r), int(g), int(b)))
        p.drawPath(path)
        p.restore()

    # Front face.
    p.save()
    p.setPen(QPen(TEXT_OUTLINE, max(1.2, S / 220)))
    p.setBrush(GOLD_FACE)
    p.drawPath(path)
    p.restore()

    # Thin top-left highlight sliver for a beveled catch-light.
    p.save()
    p.translate(-S * 0.006, -S * 0.006)
    p.setPen(QPen(QColor(255, 255, 240, 130), max(1.0, S / 260)))
    p.setBrush(Qt.BrushStyle.NoBrush)
    p.drawPath(path)
    p.restore()


def _coin_badge(p, S, cx, cy, text):
    """Rounded chip styled like the in-game nearest-coin badge, with the
    logotype set small and lightly extruded inside it."""
    w, h = S * 0.40, S * 0.215
    rect = QRectF(cx - w / 2, cy - h / 2, w, h)

    p.save()
    p.setPen(QPen(QColor("#e8c84a"), max(1.4, S / 200)))
    p.setBrush(QColor(14, 14, 34, 225))
    p.drawRoundedRect(rect, S * 0.03, S * 0.03)
    p.restore()

    _extruded_text(p, S, text, cx, cy + S * 0.006, px_size=0.135, depth=0.55)


def render(size: int) -> QPixmap:
    S = size
    pm = QPixmap(S, S)
    pm.fill(Qt.GlobalColor.transparent)
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    p.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

    # --- rounded-square arcade-cabinet card -----------------------------
    grad = QLinearGradient(0, S * 0.03, 0, S * 0.97)
    grad.setColorAt(0.0, VOID_TOP)
    grad.setColorAt(1.0, VOID_BOT)
    p.setBrush(grad)
    p.setPen(Qt.PenStyle.NoPen)
    rad = S * 0.16
    card = QRectF(S * 0.03, S * 0.03, S * 0.94, S * 0.94)
    p.drawRoundedRect(card, rad, rad)

    p.save()
    clip = QPainterPath()
    clip.addRoundedRect(card, rad, rad)
    p.setClipPath(clip)

    # faint CRT scanlines for texture
    p.setPen(QPen(SCANLINE, max(1.0, S / 340)))
    step = max(3, int(S / 48))
    for y in range(int(S * 0.05), int(S * 0.95), step):
        p.drawLine(0, y, S, y)

    # contact shadow under the character
    p.setPen(Qt.PenStyle.NoPen)
    p.setBrush(SHADOW)
    p.drawEllipse(QRectF(S * 0.20, S * 0.925, S * 0.40, S * 0.045))

    # --- chumpman standing at a natural scale, with a "11D" readout chip
    # floating by his head -- same layout language as the in-game nearest
    # -coin badge that hovers over his shoulder.
    _draw_chumpman(p, S * 0.38, S * 0.66, S * 0.036)
    _coin_badge(p, S, S * 0.745, S * 0.235, "11D")

    p.restore()
    p.end()
    return pm


def main():
    app = QGuiApplication(sys.argv)  # noqa: F841 - keep the instance alive
    os.makedirs(OUT, exist_ok=True)
    for size in (512, 256, 128, 64, 48):
        name = "chumpman11d.png" if size == 512 else f"chumpman11d-{size}.png"
        path = os.path.join(OUT, name)
        render(size).save(path, "PNG")
        print("wrote", path)


if __name__ == "__main__":
    main()

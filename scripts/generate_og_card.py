# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=10"]
# ///
"""Generate the 1200x630 Open Graph card into public/img/og-card.png.

Run with:  uv run scripts/generate_og_card.py

Fonts are downloaded once into a local cache (OFL-licensed).
"""

import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "img" / "og-card.png"
CACHE = ROOT / "scripts" / ".fontcache"

FONTS = {
    "mono": "https://github.com/JetBrains/JetBrainsMono/raw/master/fonts/ttf/JetBrainsMono-Bold.ttf",
    "mono_reg": "https://github.com/JetBrains/JetBrainsMono/raw/master/fonts/ttf/JetBrainsMono-Regular.ttf",
    "disp": "https://github.com/google/fonts/raw/main/ofl/spacegrotesk/SpaceGrotesk%5Bwght%5D.ttf",
}

PAPER = (12, 45, 77)
PAPER_DEEP = (9, 34, 58)
INK = (216, 233, 249)
DIM = (143, 179, 209)
ACCENT = (111, 211, 255)
STAMP = (255, 107, 107)
GRID = (216, 233, 249, 20)
GRID_MAJOR = (216, 233, 249, 40)

W, H = 1200, 630


def font_path(key: str) -> Path:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{key}.ttf"
    if not path.exists():
        urllib.request.urlretrieve(FONTS[key], path)
    return path


def load(key: str, size: int, bold_variable: bool = False) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(font_path(key)), size)
    if bold_variable:
        try:
            f.set_variation_by_name("Bold")
        except Exception:
            pass
    return f


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    # grid
    for x in range(0, W, 24):
        d.line([(x, 0), (x, H)], fill=GRID_MAJOR if x % 120 == 0 else GRID, width=1)
    for y in range(0, H, 24):
        d.line([(0, y), (W, y)], fill=GRID_MAJOR if y % 120 == 0 else GRID, width=1)
    img = Image.alpha_composite(img.convert("RGBA"), overlay)
    d = ImageDraw.Draw(img)

    # sheet frame
    m = 28
    d.rectangle([m, m, W - m, H - m], outline=INK, width=3)
    d.rectangle([m - 10, m - 10, W - m + 10, H - m + 10], outline=(*DIM, 120), width=1)

    mono_s = load("mono_reg", 19)
    mono_m = load("mono", 24)
    disp_xl = load("disp", 118, bold_variable=True)

    # header strip
    d.line([m, m + 56, W - m, m + 56], fill=INK, width=2)
    d.text((m + 26, m + 17), "DOC NO. MP-2026-001", font=mono_s, fill=DIM)
    d.text((W // 2, m + 17), "PERSONNEL SPECIFICATION", font=mono_s, fill=ACCENT, anchor="ma")
    d.text((W - m - 26, m + 17), "SCALE 1:1", font=mono_s, fill=DIM, anchor="ra")

    # fig label
    d.text((m + 46, 150), "FIG. 001 — THE CONSULTANT", font=mono_m, fill=ACCENT)

    # name
    d.text((m + 42, 195), "MISJA", font=disp_xl, fill=INK)
    d.text((m + 42, 305), "PRONK", font=disp_xl, fill=INK)

    # title + spec
    d.text((m + 46, 445), "DATA & PLATFORM ENGINEERING CONSULTANT", font=mono_m, fill=ACCENT)
    d.text(
        (m + 46, 490),
        "AZURE · DATABRICKS · dbt · TERRAFORM · TERRAGRUNT · OPEN SOURCE",
        font=mono_s,
        fill=DIM,
    )

    # stamp (rotated)
    stamp = Image.new("RGBA", (430, 120), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rectangle([4, 4, 426, 116], outline=STAMP, width=4)
    sd.rectangle([14, 14, 416, 106], outline=STAMP, width=2)
    sd.text((215, 34), "APPROVED", font=load("mono", 40), fill=STAMP, anchor="ma")
    sd.text((215, 82), "FOR PRODUCTION", font=load("mono_reg", 17), fill=STAMP, anchor="ma")
    stamp = stamp.rotate(9, expand=True, resample=Image.BICUBIC)
    img.paste(stamp, (W - 520, 130), stamp)

    # footer strip
    d.line([m, H - m - 52, W - m, H - m - 52], fill=INK, width=2)
    d.text((m + 26, H - m - 36), "MEASURE TWICE · BUILD ONCE", font=mono_s, fill=DIM)
    d.text((W - m - 26, H - m - 36), "misja-pronk.github.io/resume", font=mono_s, fill=ACCENT, anchor="ra")

    # registration marks
    for cx, cy in [(14, 14), (W - 14, 14), (14, H - 14), (W - 14, H - 14)]:
        d.line([(cx - 8, cy), (cx + 8, cy)], fill=ACCENT, width=2)
        d.line([(cx, cy - 8), (cx, cy + 8)], fill=ACCENT, width=2)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

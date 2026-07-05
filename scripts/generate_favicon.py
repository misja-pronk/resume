# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=10"]
# ///
"""Generate the favicon set into public/ — blueprint MP monogram.

Run with:  uv run scripts/generate_favicon.py

Writes favicon.svg (vector), favicon.ico (16/32/48), apple-touch-icon.png
(180) and icon-512.png. Matches the nav brand: navy field, cyan border,
cyan MP.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
FONT = ROOT / "scripts" / ".fontcache" / "mono.ttf"  # JetBrains Mono Bold

NAVY = (12, 45, 77)
CYAN = (111, 211, 255)

SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#0c2d4d"/>
  <rect x="6.5" y="6.5" width="51" height="51" rx="8" fill="none" stroke="#6fd3ff" stroke-width="2.5"/>
  <text x="32" y="41.5" font-family="'JetBrains Mono', ui-monospace, monospace"
        font-size="25" font-weight="700" fill="#6fd3ff" text-anchor="middle"
        letter-spacing="1">MP</text>
</svg>
"""


def render(size: int) -> Image.Image:
    # Supersample for crisp edges, then downscale.
    s = size * 8
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = round(s * 0.19)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=r, fill=NAVY)
    inset = round(s * 0.1)
    d.rounded_rectangle(
        [inset, inset, s - inset - 1, s - inset - 1],
        radius=round(r * 0.7),
        outline=CYAN,
        width=max(2, round(s * 0.035)),
    )
    try:
        f = ImageFont.truetype(str(FONT), round(s * 0.42))
    except Exception:
        f = ImageFont.load_default(round(s * 0.42))
    tb = d.textbbox((0, 0), "MP", font=f)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    d.text(((s - tw) / 2 - tb[0], (s - th) / 2 - tb[1]), "MP", font=f, fill=CYAN)
    return img.resize((size, size), Image.LANCZOS)


def main() -> None:
    (PUB / "favicon.svg").write_text(SVG)

    render(180).save(PUB / "apple-touch-icon.png", "PNG", optimize=True)
    render(512).save(PUB / "icon-512.png", "PNG", optimize=True)

    ico = render(256)
    ico.save(PUB / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    print("wrote favicon.svg, favicon.ico, apple-touch-icon.png, icon-512.png")


if __name__ == "__main__":
    main()

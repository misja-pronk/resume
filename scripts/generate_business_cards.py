# /// script
# requires-python = ">=3.11"
# dependencies = ["reportlab>=4.0"]
# ///
"""Generate ProRex business cards (85x55 mm, front + back) into brand/.

Run with:  uv run scripts/generate_business_cards.py

Print-ready at standard NL card size; no bleed — ask the print shop
for a 3 mm bleed version if needed. Output is NOT committed (brand/
is gitignored) — it is encrypted into public/vault/.
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

OUT = Path(__file__).resolve().parent.parent / "brand"
OUT.mkdir(exist_ok=True)

W, H = 85 * mm, 55 * mm

NAVY = colors.HexColor("#0c2d4d")
NAVY_DEEP = colors.HexColor("#123a5f")
ICE = colors.HexColor("#d8e9f9")
DIM = colors.HexColor("#8fb3d1")
ACCENT = colors.HexColor("#6fd3ff")
PAPER = colors.HexColor("#f7f5ee")
INK = colors.HexColor("#16324f")
DIM_LIGHT = colors.HexColor("#7a8ea3")
ACCENT_LIGHT = colors.HexColor("#0d6fb8")


def grid(c, color, step=6 * mm, weight=0.3):
    c.setStrokeColor(color)
    c.setLineWidth(weight)
    x = 0.0
    while x < W:
        c.line(x, 0, x, H)
        x += step
    y = 0.0
    while y < H:
        c.line(0, y, W, y)
        y += step


def regmarks(c, color):
    c.setStrokeColor(color)
    c.setLineWidth(0.8)
    for cx, cy in [(4 * mm, 4 * mm), (W - 4 * mm, 4 * mm), (4 * mm, H - 4 * mm), (W - 4 * mm, H - 4 * mm)]:
        c.line(cx - 1.6 * mm, cy, cx + 1.6 * mm, cy)
        c.line(cx, cy - 1.6 * mm, cx, cy + 1.6 * mm)


def main() -> None:
    path = OUT / "prorex-business-card.pdf"
    c = canvas.Canvas(str(path), pagesize=(W, H))
    c.setTitle("ProRex Consultancy — business card")

    # ---------- front (navy blueprint)
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    grid(c, NAVY_DEEP)
    c.setStrokeColor(ICE)
    c.setLineWidth(1.2)
    c.rect(3 * mm, 3 * mm, W - 6 * mm, H - 6 * mm, stroke=1, fill=0)
    regmarks(c, ACCENT)

    # MP mark
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.0)
    c.rect(8 * mm, H - 17 * mm, 9 * mm, 9 * mm, stroke=1, fill=0)
    c.setFillColor(ACCENT)
    c.setFont("Courier-Bold", 10.5)
    c.drawCentredString(12.5 * mm, H - 13.6 * mm, "MP")

    c.setFillColor(ICE)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(21 * mm, H - 12.2 * mm, "MISJA PRONK")
    c.setFillColor(ACCENT)
    c.setFont("Courier-Bold", 6.6)
    c.drawString(21 * mm, H - 16.2 * mm, "DATA & PLATFORM ENGINEERING CONSULTANT")

    c.setFillColor(DIM)
    c.setFont("Courier", 7)
    lines = [
        "misja@prorexconsultancy.nl",
        "prorexconsultancy.nl",
        "linkedin.com/in/misja-pronk",
    ]
    for i, line in enumerate(lines):
        c.drawString(8 * mm, 19.5 * mm - i * 4.4 * mm, line)

    c.setFillColor(DIM)
    c.setFont("Courier", 5.4)
    c.drawRightString(W - 8 * mm, 7.4 * mm, "BUILD FAST · FAIL FAST · KEEP IT SIMPLE")
    c.showPage()

    # ---------- back (drafting paper)
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    grid(c, colors.HexColor("#e9e5d8"))
    c.setStrokeColor(INK)
    c.setLineWidth(1.2)
    c.rect(3 * mm, 3 * mm, W - 6 * mm, H - 6 * mm, stroke=1, fill=0)
    regmarks(c, ACCENT_LIGHT)

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(W / 2, H - 17 * mm, "PROREX CONSULTANCY")
    c.setFillColor(ACCENT_LIGHT)
    c.setFont("Courier-Bold", 6.4)
    c.drawCentredString(W / 2, H - 21.5 * mm, "DATA PLATFORMS · DATABRICKS · PLATFORM ENGINEERING")

    # title block strip
    c.setStrokeColor(INK)
    c.setLineWidth(0.9)
    c.line(8 * mm, 17 * mm, W - 8 * mm, 17 * mm)
    c.setFillColor(DIM_LIGHT)
    c.setFont("Courier", 5.6)
    c.drawString(8 * mm, 12.8 * mm, "KVK 85369624")
    c.drawCentredString(W / 2, 12.8 * mm, "WOMMELS · FRIESLAND")
    c.drawRightString(W - 8 * mm, 12.8 * mm, "EST. 2022")
    c.setFillColor(ACCENT_LIGHT)
    c.setFont("Courier-Bold", 6.2)
    c.drawCentredString(W / 2, 7.6 * mm, "BUILD FAST · FAIL FAST · KEEP IT SIMPLE")
    c.showPage()

    c.save()
    print(f"wrote {path}")


if __name__ == "__main__":
    main()

# /// script
# requires-python = ">=3.11"
# ///
"""Generate the ProRex HTML deck template into brand/.

Run with:  uv run scripts/generate_html_deck.py

A single self-contained HTML file: open in any browser, navigate with
arrow keys / space / click, print to PDF for handouts. Edit the slide
content directly in the HTML. Encrypted into the vault like the other
brand assets.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "brand"
OUT.mkdir(exist_ok=True)

HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ProRex — presentation</title>
<style>
  :root {
    --navy: #0c2d4d; --navy-deep: #0a2540; --ink: #d8e9f9; --dim: #8fb3d1;
    --accent: #6fd3ff; --stamp: #ff6b6b; --paper: #f7f5ee; --ink-d: #16324f;
    --dim-d: #7a8ea3; --accent-d: #0d6fb8; --line-d: #c4cfda;
    --mono: 'JetBrains Mono', 'Courier New', monospace;
    --sans: 'Space Grotesk', 'Arial', sans-serif;
  }
  * { box-sizing: border-box; margin: 0; }
  body { font-family: var(--sans); background: #06121f; }
  .slide {
    width: 100vw; height: 100vh; display: none; position: relative;
    padding: 5.5rem 5rem 4.5rem; overflow: hidden;
  }
  .slide.active { display: block; }
  .slide.dark {
    background:
      repeating-linear-gradient(0deg, transparent, transparent 23px, rgba(216,233,249,.06) 23px, rgba(216,233,249,.06) 24px),
      repeating-linear-gradient(90deg, transparent, transparent 23px, rgba(216,233,249,.06) 23px, rgba(216,233,249,.06) 24px),
      var(--navy);
    color: var(--ink);
  }
  .slide.light {
    background:
      repeating-linear-gradient(0deg, transparent, transparent 23px, rgba(22,50,79,.07) 23px, rgba(22,50,79,.07) 24px),
      repeating-linear-gradient(90deg, transparent, transparent 23px, rgba(22,50,79,.07) 23px, rgba(22,50,79,.07) 24px),
      var(--paper);
    color: var(--ink-d);
  }
  .frame { position: absolute; inset: 1.4rem; border: 2px solid currentColor; pointer-events: none; }
  .hdr, .ftr {
    position: absolute; left: 1.4rem; right: 1.4rem; display: flex;
    justify-content: space-between; padding: .55rem 1.2rem;
    font-family: var(--mono); font-size: .62rem; letter-spacing: .16em;
  }
  .hdr { top: 1.4rem; border-bottom: 1px solid currentColor; }
  .ftr { bottom: 1.4rem; border-top: 1px solid currentColor; }
  .dark .hdr, .dark .ftr { color: var(--dim); }
  .light .hdr, .light .ftr { color: var(--dim-d); }
  .hdr b { font-weight: 700; }
  .dark .hdr b, .dark .ftr b { color: var(--accent); }
  .light .hdr b, .light .ftr b { color: var(--accent-d); }
  .fig { font-family: var(--mono); font-size: .85rem; letter-spacing: .3em; margin-bottom: 1.4rem; }
  .dark .fig { color: var(--accent); } .light .fig { color: var(--accent-d); }
  h1 { font-size: 4.2rem; line-height: 1.02; letter-spacing: .02em; }
  h2 { font-size: 2.6rem; margin-bottom: 2rem; }
  .sub { font-size: 1.25rem; margin-top: 1rem; }
  .dark .sub { color: var(--dim); } .light .sub { color: var(--dim-d); }
  .meta { font-family: var(--mono); font-size: .85rem; letter-spacing: .14em; margin-top: 3rem; line-height: 2; }
  .agenda { list-style: none; display: flex; flex-direction: column; gap: 1.1rem; font-size: 1.3rem; }
  .agenda li { display: flex; gap: 1.2rem; align-items: baseline; }
  .agenda .no { font-family: var(--mono); color: var(--stamp); font-weight: 700; font-size: 1rem; }
  .light .agenda .no { color: #d43d3d; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: start; }
  .cols p { font-size: 1.1rem; line-height: 1.7; margin-bottom: 1rem; }
  .lead { font-weight: 700; }
  .dark .lead { color: var(--accent); } .light .lead { color: var(--accent-d); }
  .panel { border: 1.5px solid currentColor; min-height: 46vh; display: grid; place-items: center;
    font-family: var(--mono); font-size: .8rem; letter-spacing: .2em; opacity: .65; }
  .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 1rem; }
  .stat { border: 1px solid currentColor; padding: 2.2rem 1rem; text-align: center; }
  .stat b { display: block; font-size: 4rem; }
  .dark .stat b { color: var(--accent); } .light .stat b { color: var(--accent-d); }
  .stat span { font-family: var(--mono); font-size: .68rem; letter-spacing: .2em; opacity: .7; }
  .pipeline { display: flex; align-items: center; gap: 1rem; margin-top: 4rem; }
  .node { flex: 1; border: 1.5px solid currentColor; padding: 1.4rem .6rem; text-align: center; }
  .node b { font-family: var(--mono); letter-spacing: .18em; font-size: 1rem; display: block; }
  .node span { font-family: var(--mono); font-size: .6rem; letter-spacing: .1em; opacity: .65; }
  .wire { font-family: var(--mono); } .dark .wire { color: var(--accent); } .light .wire { color: var(--accent-d); }
  .counter { position: fixed; bottom: 2.2rem; right: 2.9rem; font-family: var(--mono);
    font-size: .62rem; letter-spacing: .2em; color: var(--dim); z-index: 5; pointer-events: none; }
  @media print {
    .slide { display: block; page-break-after: always; width: 297mm; height: 167mm; }
    .counter { display: none; }
  }
</style>
</head>
<body>

<section class="slide dark active">
  <div class="frame"></div>
  <div class="hdr"><span>DOC NO. PRX-____ · REV ____</span><b>PRESENTATION — TITLE SHEET</b><span>SHT 01</span></div>
  <div class="fig">FIG. 001 — WORKING SESSION</div>
  <h1>PRESENTATION<br>TITLE</h1>
  <p class="sub">Subtitle or client name goes here</p>
  <p class="meta"><b style="color:var(--ink)">MISJA PRONK · PROREX CONSULTANCY</b><br>DATE: __________ · AUDIENCE: __________</p>
  <div class="ftr"><span>PROREX CONSULTANCY — DATA &amp; PLATFORM ENGINEERING</span><b>BUILD FAST · FAIL FAST · KEEP IT SIMPLE</b></div>
</section>

<section class="slide light">
  <div class="frame"></div>
  <div class="hdr"><span>DOC NO. PRX-____</span><b>DRAWING SET — CONTENTS</b><span>SHT 02</span></div>
  <h2>Agenda</h2>
  <ul class="agenda">
    <li><span class="no">01</span> Context &amp; goal</li>
    <li><span class="no">02</span> Current situation</li>
    <li><span class="no">03</span> Proposed approach</li>
    <li><span class="no">04</span> Architecture</li>
    <li><span class="no">05</span> Planning &amp; next steps</li>
  </ul>
  <div class="ftr"><span>PROREX CONSULTANCY</span><b>BUILD FAST · FAIL FAST · KEEP IT SIMPLE</b></div>
</section>

<section class="slide dark">
  <div class="frame"></div>
  <div class="hdr"><span>DOC NO. PRX-____</span><b>SECTION DIVIDER</b><span>SHT 03</span></div>
  <div style="margin-top:14vh">
    <h1><span style="color:var(--stamp);font-family:var(--mono)">01</span> SECTION TITLE</h1>
    <p class="sub">One line on what this section covers</p>
  </div>
  <div class="ftr"><span>PROREX CONSULTANCY</span><b>BUILD FAST · FAIL FAST · KEEP IT SIMPLE</b></div>
</section>

<section class="slide light">
  <div class="frame"></div>
  <div class="hdr"><span>DOC NO. PRX-____</span><b>DETAIL — CONTENT</b><span>SHT 04</span></div>
  <h2>Content slide title</h2>
  <div class="cols">
    <div>
      <p class="lead">The point in one sentence.</p>
      <p>Supporting paragraph: keep it short and concrete. Replace this text with the actual argument, evidence or story.</p>
      <p>— First supporting point<br>— Second supporting point<br>— Third supporting point</p>
    </div>
    <div class="panel">[ DIAGRAM / SCREENSHOT / CHART ]</div>
  </div>
  <div class="ftr"><span>PROREX CONSULTANCY</span><b>BUILD FAST · FAIL FAST · KEEP IT SIMPLE</b></div>
</section>

<section class="slide light">
  <div class="frame"></div>
  <div class="hdr"><span>DOC NO. PRX-____</span><b>SCHEDULE OF QUANTITIES</b><span>SHT 05</span></div>
  <h2>The numbers</h2>
  <div class="stats">
    <div class="stat"><b>42%</b><span>METRIC ONE</span></div>
    <div class="stat"><b>3×</b><span>METRIC TWO</span></div>
    <div class="stat"><b>€ 1.2M</b><span>METRIC THREE</span></div>
  </div>
  <p class="sub" style="margin-top:2.5rem">One sentence interpreting the numbers for the audience.</p>
  <div class="ftr"><span>PROREX CONSULTANCY</span><b>BUILD FAST · FAIL FAST · KEEP IT SIMPLE</b></div>
</section>

<section class="slide light">
  <div class="frame"></div>
  <div class="hdr"><span>DOC NO. PRX-____</span><b>TYPICAL DEPLOYMENT</b><span>SHT 06</span></div>
  <h2>Architecture</h2>
  <div class="pipeline">
    <div class="node"><b>SOURCES</b><span>APIs · DBs · FILES</span></div><span class="wire">──▶</span>
    <div class="node"><b>INGEST</b><span>DATA FACTORY</span></div><span class="wire">──▶</span>
    <div class="node"><b>TRANSFORM</b><span>DATABRICKS · dbt</span></div><span class="wire">──▶</span>
    <div class="node"><b>SERVE</b><span>LAKEHOUSE · BI</span></div>
  </div>
  <div class="ftr"><span>PROREX CONSULTANCY</span><b>BUILD FAST · FAIL FAST · KEEP IT SIMPLE</b></div>
</section>

<section class="slide dark">
  <div class="frame"></div>
  <div class="hdr"><span>DOC NO. PRX-____</span><b>CLOSING — SIGN-OFF</b><span>SHT 07</span></div>
  <div style="margin-top:12vh">
    <h1>Questions &amp; next steps</h1>
    <p class="meta"><b style="color:var(--accent)">MISJA PRONK — PROREX CONSULTANCY</b><br>
    misja@prorexconsultancy.nl · prorexconsultancy.nl · linkedin.com/in/misja-pronk<br>KVK 85369624</p>
  </div>
  <div class="ftr"><span>PROREX CONSULTANCY</span><b>BUILD FAST · FAIL FAST · KEEP IT SIMPLE</b></div>
</section>

<div class="counter" id="counter">SHT 01 / 07</div>

<script>
  const slides = [...document.querySelectorAll('.slide')];
  const counter = document.getElementById('counter');
  let i = 0;
  const show = (n) => {
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((s, j) => s.classList.toggle('active', j === i));
    counter.textContent = `SHT ${String(i + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
  };
  addEventListener('keydown', (e) => {
    if (['ArrowRight', ' ', 'PageDown'].includes(e.key)) show(i + 1);
    if (['ArrowLeft', 'PageUp'].includes(e.key)) show(i - 1);
    if (e.key === 'Home') show(0);
  });
  addEventListener('click', (e) => show(e.clientX > innerWidth / 2 ? i + 1 : i - 1));
</script>
</body>
</html>
"""


def main() -> None:
    path = OUT / "prorex-deck-template.html"
    path.write_text(HTML)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()

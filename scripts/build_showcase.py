#!/usr/bin/env python3
"""
Build the GitHub Astrolab showcase page — a standalone HTML overview of the app's
features with every screenshot inlined as a data URI (no external requests, so
it survives a strict CSP and works offline).

Run: python3 scripts/build_showcase.py
"""
import base64
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, "docs/screenshots")
OUT = os.path.join(ROOT, "docs/astrolab.html")

FEATURES = [
    ("01-map.jpg", "Map", "The corpus as a sky",
     "Every starred repo is a node, placed by a force simulation that runs at build "
     "time rather than in your browser. Colour encodes the community Louvain found; "
     "size combines stars with PageRank, so structurally central projects read as "
     "bright regardless of popularity.",
     "1,596 nodes · 5,170 edges · 31 communities"),
    ("02-topics.jpg", "Topics", "What the stars are about",
     "A co-occurrence graph of tags across the whole corpus. Where the Map shows which "
     "projects relate, this shows which *subjects* do — the shape of an interest rather "
     "than its instances.",
     "co-occurrence across every tag in the set"),
    ("03-insights.jpg", "Insights", "Questions, already asked",
     "Named analytical queries over the dataset: where developers actually work, measured "
     "by unique authors active in the last 90 days; the classic core; bus-factor risks; "
     "declining projects worth replacing; PageRank-central cluster leaders. Every view "
     "exports to JSON or CSV.",
     "6 standing queries · JSON + CSV export"),
    ("04-risk.jpg", "Risk", "What is quietly dying",
     "Lifecycle stage, health score, bus factor and top-author concentration in one view. "
     "A dependency with one maintainer and no pushes in a year looks identical to a "
     "healthy one on a star count — this is where the difference shows.",
     "lifecycle · health · bus factor · author share"),
    ("05-browse.jpg", "Browse", "The whole corpus, filtered",
     "Search and sort across every metric the pipeline computes: stars, forks, language, "
     "lifecycle, health, activity. The unglamorous view that answers most questions.",
     "45 metadata fields per repo"),
    ("06-compare.jpg", "Compare", "Two projects, and what joins them",
     "Side-by-side metrics, plus the shortest path between the two through the graph — "
     "the shared topics, authors, or intermediate projects that connect them. The "
     "comparison most tools can't make, because they have no edges.",
     "metric diff + shortest graph path"),
    ("07-reports.jpg", "Reports", "Twenty-three curated landscapes",
     "The largest feature, and the most deliberate: each report is a deterministic Python "
     "generator over the local dataset. Hand-curated taxonomies, master comparison tables, "
     "per-task rankings, graph analysis, maintenance risk. No model writes them, no API is "
     "called at generation time — so they rebuild identically, for free, on every refresh.",
     "23 reports · 13 categories · fully reproducible"),
    ("08-ask-ai.jpg", "Ask AI", "Natural language, grounded",
     "Questions answered against the graph's own community summary as context, through any "
     "OpenAI-compatible endpoint. Deliberately the last feature rather than the first: "
     "everything above works without a key, and the model reads the graph rather than "
     "replacing it.",
     "provider-agnostic · optional"),
]


def data_uri(path):
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()


def main():
    cl = json.load(open(os.path.join(ROOT, "data/classified.json")))
    gr = json.load(open(os.path.join(ROOT, "public/data/graph.json")))
    idx = json.load(open(os.path.join(ROOT, "public/reports/index.json")))
    reports = idx if isinstance(idx, list) else idx.get("reports", idx)

    stats = [
        (f"{cl['total']:,}", "repositories mapped"),
        (f"{len(gr['links']):,}", "similarity edges"),
        (str(len(gr["communities"])), "communities"),
        (str(len(reports)), "landscape reports"),
    ]

    # The hero star field is the *real* corpus, not decoration: take the most
    # structurally central nodes and ship their frozen simulation coordinates.
    top = sorted(gr["nodes"], key=lambda n: -(n.get("pagerank") or 0))[:900]
    xs = [n["x"] for n in top]
    ys = [n["y"] for n in top]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    span = max(max(xs) - min(xs), max(ys) - min(ys)) or 1
    stars = [
        [round((n["x"] - cx) / span, 4),          # normalised −0.5…0.5
         round((n["y"] - cy) / span, 4),
         round(min(n.get("val") or 1, 9), 2),     # radius driver
         n.get("color") or "#888"]
        for n in top
    ]
    star_json = json.dumps(stars, separators=(",", ":"))

    def build_sections(inline):
        out = []
        for img, tab, head, body, meta in FEATURES:
            p = os.path.join(SHOTS, img)
            if not os.path.exists(p):
                continue
            src = data_uri(p) if inline else f"/screenshots/{img}"
            out.append(f"""
<section class="feat">
  <div class="feat-txt">
    <p class="tab">{tab}</p>
    <h2>{head}</h2>
    <p>{body}</p>
    <p class="meta">{meta}</p>
  </div>
  <figure class="shot"><img src="{src}" alt="{tab} — {head}" loading="lazy"></figure>
</section>""")
        return out

    sections = build_sections(inline=True)

    stat_html = "".join(
        f'<div><b>{v}</b><span>{k}</span></div>' for v, k in stats)

    html = f"""<title>GitHub Astrolab</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{{
  --night:#f6f5f1; --plate:#ffffff; --rule:#ddd8cc; --hair:#eae6dc;
  --ink:#191713; --ink-2:#544f45; --ink-3:#837c6e;
  --brass:#8a6a12; --brass-lit:#a8830f; --glow:rgba(168,131,15,.10);
  --display:"Hoefler Text","Iowan Old Style",Palatino,Georgia,serif;
  --body:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}}
@media (prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    --night:#0b0e17; --plate:#131826; --rule:#2a3145; --hair:#1d2333;
    --ink:#f2eee4; --ink-2:#bdb5a4; --ink-3:#8c8574;
    --brass:#d9b04a; --brass-lit:#e8c66a; --glow:rgba(217,176,74,.13);
  }}
}}
:root[data-theme="dark"]{{
  --night:#0b0e17; --plate:#131826; --rule:#2a3145; --hair:#1d2333;
  --ink:#f2eee4; --ink-2:#bdb5a4; --ink-3:#8c8574;
  --brass:#d9b04a; --brass-lit:#e8c66a; --glow:rgba(217,176,74,.13);
}}
*{{box-sizing:border-box}}
body{{
  margin:0;background:var(--night);color:var(--ink);
  font-family:var(--body);font-size:16.5px;line-height:1.68;
  overflow-x:hidden;
}}
.wrap{{max-width:1120px;margin:0 auto;padding:0 26px 110px;position:relative;z-index:1}}

/* ── the sky: the real corpus, rotating behind the plate ──────────── */
.sky{{
  position:absolute;top:0;left:0;right:0;height:940px;z-index:0;
  pointer-events:none;overflow:hidden;
  /* fade the field out before it reaches the first feature */
  -webkit-mask-image:radial-gradient(ellipse 62% 54% at 50% 34%,#000 30%,transparent 78%);
  mask-image:radial-gradient(ellipse 62% 54% at 50% 34%,#000 30%,transparent 78%);
}}
.sky canvas{{display:block;width:100%;height:100%}}

/* ── hero: the rete, an astrolabe's rotating star-map ─────────────── */
.hero{{position:relative;padding:104px 0 60px;text-align:center}}
.rete{{
  position:absolute;top:-130px;left:50%;transform:translateX(-50%);
  width:760px;height:760px;pointer-events:none;opacity:.5;z-index:0;
}}
.rete circle,.rete line{{fill:none;stroke:var(--brass);stroke-width:.7;opacity:.5}}
.rete .faint{{opacity:.22}}
.hero > *{{position:relative;z-index:1}}
.eyebrow{{
  font-family:var(--mono);font-size:11px;letter-spacing:.30em;text-transform:uppercase;
  color:var(--brass);margin:0 0 26px
}}
h1{{
  font-family:var(--display);font-weight:400;
  font-size:clamp(3.3rem,11.5vw,8rem);line-height:.92;letter-spacing:-.035em;
  margin:0 0 22px;
}}
h1 .pre{{
  display:block;font-family:var(--mono);font-size:clamp(.72rem,1.7vw,1rem);
  letter-spacing:.42em;text-transform:uppercase;color:var(--ink-3);
  margin-bottom:14px;text-indent:.42em
}}
.lede{{
  font-family:var(--display);font-style:italic;color:var(--ink-2);
  font-size:clamp(1.15rem,2.6vw,1.65rem);line-height:1.5;
  max-width:33ch;margin:0 auto 14px;text-wrap:balance
}}
.sub{{color:var(--ink-3);font-size:14.5px;max-width:56ch;margin:0 auto}}
.cta-row{{margin:38px 0 0}}
.cta{{
  display:inline-block;font-family:var(--mono);font-size:12px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--night);background:var(--brass);
  padding:15px 34px;border-radius:2px;border:0;
  transition:transform .2s ease,box-shadow .2s ease,background .2s ease
}}
.cta:hover{{background:var(--brass-lit);transform:translateY(-2px);
  box-shadow:0 12px 30px -12px var(--brass);border-bottom-color:transparent}}
.stats{{
  display:flex;flex-wrap:wrap;justify-content:center;gap:26px 60px;
  margin:52px 0 0;padding:30px 0 0;border-top:1px solid var(--rule)
}}
.stats div{{display:flex;flex-direction:column;gap:3px}}
.stats b{{
  font-family:var(--display);font-size:2.5rem;font-weight:400;line-height:1;
  font-variant-numeric:tabular-nums;color:var(--brass)
}}
.stats span{{
  font-family:var(--mono);font-size:10px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--ink-3)
}}

/* ── features: alternating plate + engraving ──────────────────────── */
.feat{{
  display:grid;grid-template-columns:minmax(0,.82fr) minmax(0,1.18fr);
  gap:52px;align-items:center;padding:70px 0;border-top:1px solid var(--hair)
}}
.feat:nth-child(even) .feat-txt{{order:2}}
.tab{{
  font-family:var(--mono);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;
  color:var(--brass);margin:0 0 12px
}}
.feat h2{{
  font-family:var(--display);font-weight:400;font-size:clamp(1.7rem,3.4vw,2.5rem);
  line-height:1.14;letter-spacing:-.02em;margin:0 0 16px;text-wrap:balance
}}
.feat p{{margin:0 0 14px;color:var(--ink-2);max-width:46ch}}
.meta{{
  font-family:var(--mono)!important;font-size:11px!important;color:var(--ink-3)!important;
  letter-spacing:.03em;padding-top:12px;border-top:1px solid var(--hair);margin-bottom:0!important
}}
.shot{{margin:0;border-radius:9px;overflow:hidden;border:1px solid var(--rule);
  background:var(--plate);box-shadow:0 18px 44px -22px var(--glow)}}
.shot img{{display:block;width:100%;height:auto}}

/* ── closing ──────────────────────────────────────────────────────── */
.end{{
  margin-top:78px;padding-top:44px;border-top:1px solid var(--rule);text-align:center
}}
.end h2{{
  font-family:var(--display);font-weight:400;font-size:clamp(1.5rem,3vw,2.1rem);
  margin:0 0 14px;letter-spacing:-.015em
}}
.end p{{color:var(--ink-2);max-width:56ch;margin:0 auto 12px}}
.end code{{
  font-family:var(--mono);font-size:.85em;background:var(--hair);
  color:var(--ink);padding:.16em .42em;border-radius:3px
}}
a{{color:var(--brass-lit);text-decoration:none;border-bottom:1px solid transparent}}
a:hover{{border-bottom-color:var(--brass-lit)}}
a:focus-visible{{outline:2px solid var(--brass-lit);outline-offset:3px;border-radius:2px}}
.fine{{
  font-family:var(--mono);font-size:11px;color:var(--ink-3);
  margin-top:40px;text-align:center;letter-spacing:.03em
}}
@media (max-width:820px){{
  .feat{{grid-template-columns:1fr;gap:26px;padding:52px 0}}
  .feat:nth-child(even) .feat-txt{{order:0}}
  .rete{{width:520px;height:520px;top:-70px}}
  .hero{{padding:64px 0 42px}}
}}
/* scroll reveal — subtle, one gesture, not scattered effects */
.feat,.end{{opacity:0;transform:translateY(18px);transition:opacity .7s ease,transform .7s ease}}
.feat.in,.end.in{{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){{
  *{{animation:none!important;transition:none!important}}
  .feat,.end{{opacity:1;transform:none}}
}}
</style>

<div class="sky" aria-hidden="true"><canvas id="sky"></canvas></div>
<div class="wrap">
<header class="hero">
  <svg class="rete" viewBox="0 0 400 400" aria-hidden="true">
    <circle cx="200" cy="200" r="196"/><circle cx="200" cy="200" r="163" class="faint"/>
    <circle cx="200" cy="200" r="127"/><circle cx="200" cy="200" r="92" class="faint"/>
    <circle cx="200" cy="200" r="56"/><circle cx="200" cy="200" r="21" class="faint"/>
    <line x1="4" y1="200" x2="396" y2="200"/><line x1="200" y1="4" x2="200" y2="396"/>
    <line x1="61" y1="61" x2="339" y2="339" class="faint"/>
    <line x1="339" y1="61" x2="61" y2="339" class="faint"/>
    <circle cx="200" cy="200" r="127" transform="rotate(28 200 200) translate(38 0)" class="faint"/>
    <circle cx="200" cy="200" r="92" transform="rotate(-14 200 200) translate(-52 0)" class="faint"/>
  </svg>
  <p class="eyebrow">An instrument for your stars</p>
  <h1><span class="pre">GitHub</span>Astrolab</h1>
  <p class="lede">A thousand stars is not a library. It is a pile.</p>
  <p class="sub">This turns a GitHub star list into something you can navigate — a knowledge
  graph with communities and lifecycle scoring, twenty-three curated landscape reports,
  and search that understands the shape of what you saved.</p>
  <p class="cta-row"><a class="cta" href="/lab?tab=map">Enter the map<span aria-hidden="true"> →</span></a></p>
  <div class="stats">{stat_html}</div>
</header>
{"".join(sections)}
<section class="end">
  <h2>Everything expensive happens before you open it</h2>
  <p>The graph is built, clustered, ranked and force-simulated by the pipeline, then frozen
  into a static file. The browser loads coordinates and draws them — no graph maths at
  runtime, no model in the hot path, no API call needed to read a report.</p>
  <p>Refresh the data with <code>npm run refresh</code>, rebuild every report with
  <code>npm run reports</code>. Both are reproducible and cost nothing.</p>
  <p class="fine">github-stars-analyzer · MIT · data vintage {cl.get('generatedAt','')[:10]}</p>
</section>
</div>

<script>
// The hero field is this project's actual graph: 900 highest-PageRank repos at
// their frozen simulation coordinates, rotating the way a sky does under a
// fixed astrolabe plate.
(function(){{
  var STARS = {star_json};
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cv = document.getElementById('sky'), ctx = cv.getContext('2d');
  var w = 0, h = 0, dpr = Math.min(devicePixelRatio || 1, 2);

  function size(){{
    var r = cv.parentElement.getBoundingClientRect();
    w = r.width; h = r.height;
    cv.width = w * dpr; cv.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }}
  size();
  addEventListener('resize', size);

  function draw(t){{
    ctx.clearRect(0, 0, w, h);
    var cx = w / 2, cy = h * 0.34;
    var scale = Math.min(w, h * 1.5) * 1.18;
    var a = reduced ? 0 : t * 0.000035;          // one turn ≈ 50 minutes
    var ca = Math.cos(a), sa = Math.sin(a);
    for (var i = 0; i < STARS.length; i++){{
      var s = STARS[i], x = s[0], y = s[1];
      var px = cx + (x * ca - y * sa) * scale;
      var py = cy + (x * sa + y * ca) * scale;
      if (px < -20 || px > w + 20 || py < -20 || py > h + 20) continue;
      // slow, per-star breathing so the field reads as alive, not static
      var tw = reduced ? 1 : 0.72 + 0.28 * Math.sin(t * 0.0007 + i * 1.7);
      ctx.globalAlpha = 0.30 * tw;
      ctx.fillStyle = s[3];
      ctx.beginPath();
      ctx.arc(px, py, Math.max(0.7, s[2] * 0.34), 0, 6.2832);
      ctx.fill();
    }}
    ctx.globalAlpha = 1;
    if (!reduced) requestAnimationFrame(draw);
  }}
  requestAnimationFrame(draw);

  // reveal on scroll
  var io = new IntersectionObserver(function(es){{
    es.forEach(function(e){{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }});
  }}, {{ rootMargin: '0px 0px -12% 0px' }});
  document.querySelectorAll('.feat,.end').forEach(function(el){{ io.observe(el); }});
}})();
</script>
"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {OUT}  ({len(html) / 1_000_000:.2f} MB, {len(sections)} features)")

    # Site variant: same page, but pointing at the served image files instead of
    # inlining 2 MB of data URIs — this one is the deployed landing page.
    site = html.replace("".join(sections), "".join(build_sections(inline=False)))
    site_out = os.path.join(ROOT, "public/landing.html")
    with open(site_out, "w", encoding="utf-8") as f:
        f.write(site)
    print(f"Wrote {site_out}  ({len(site) / 1000:.0f} KB, images served separately)")

    # Screenshots must be reachable at /screenshots/* for the site variant.
    import shutil
    pub_shots = os.path.join(ROOT, "public/screenshots")
    os.makedirs(pub_shots, exist_ok=True)
    for f_ in os.listdir(SHOTS):
        if f_.endswith(".jpg"):
            shutil.copy2(os.path.join(SHOTS, f_), os.path.join(pub_shots, f_))
    print(f"Copied {len(os.listdir(pub_shots))} screenshots to public/screenshots/")


if __name__ == "__main__":
    main()

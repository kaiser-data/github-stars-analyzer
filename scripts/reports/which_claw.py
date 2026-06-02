#!/usr/bin/env python3
"""
Decision report: "Which claw should I use?" — ranks the standalone OpenClaw-family
agents / runtimes / agent-OSes in the starred-repos dataset on a transparent
composite score, then routes by use-case.

Scope: the "claws" you'd actually *run as your assistant/runtime* — not the
accessory ecosystem (skills, routers, memory, observability, dashboards), which
the OpenClaw Ecosystem report already covers.

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/which-claw.md   (+ reports/which-claw.meta.json)

Run: python3 scripts/reports/which_claw.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "which-claw"
TITLE = "Which Claw Should I Use? — A Decision Report"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# The standalone "claw" agents / runtimes / agent-OSes you'd pick *between*.
# Accessories (skills, routers, memory, dashboards, specialized agents) are
# intentionally excluded — they complement a claw, they aren't a claw choice.
# `kind`: general = full personal-assistant; secure = security-hardened runtime;
#         coding = coding-focused agent.
CANDIDATES = {
    "openclaw/openclaw":        {"kind": "general", "note": "the reference claw; biggest ecosystem"},
    "ultraworkers/claw-code":   {"kind": "coding",  "note": "coding-focused claw (Rust)"},
    "zeroclaw-labs/zeroclaw":   {"kind": "general", "note": "fastest/smallest, fully autonomous (Rust)"},
    "sipeed/picoclaw":          {"kind": "general", "note": "tiny footprint, runs on edge/SBCs (Go)"},
    "nanocoai/nanoclaw":        {"kind": "secure",  "note": "containerized, chat-connector secure alt (TS)"},
    "NVIDIA/NemoClaw":          {"kind": "secure",  "note": "runs in NVIDIA OpenShell, managed inference"},
    "nearai/ironclaw":          {"kind": "secure",  "note": "privacy/security agent-OS, WASM/CodeAct (Rust)"},
    "RightNow-AI/openfang":     {"kind": "general", "note": "MCP-native open 'Agent OS' (Rust)"},
    "nullclaw/nullclaw":        {"kind": "general", "note": "minimal claw written in Zig"},
}

KIND_LABEL = {
    "general": "General assistant",
    "secure":  "Secure runtime",
    "coding":  "Coding agent",
}

# ---- Load --------------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)

by_name = {r["full_name"]: r for r in cl["repos"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}
nodes_by_id = {n["id"]: n for n in gr["nodes"]}

# ---- Helpers -----------------------------------------------------------------
def fmt_int(n):
    try:
        return f"{int(n):,}"
    except Exception:
        return str(n)

def days_to_human(d):
    if d is None:
        return "?"
    d = int(d)
    if d < 30:
        return f"{d}d"
    if d < 365:
        return f"{d // 30}mo"
    return f"{d / 365:.1f}y"

def mom(r):
    return (r.get("momentum") or {}).get("estimated_stars_30d")

def activity_label(r):
    dsp = r.get("days_since_push")
    c90 = r.get("commits_90d") or 0
    if dsp is None:
        return "unknown"
    if dsp <= 30 and c90 >= 20:
        return "very active"
    if dsp <= 60:
        return "active"
    if dsp <= 180:
        return "slowing"
    return "stale"

import math

def freshness(r):
    """0..1 from days_since_push: 0d→1.0, decays to ~0 by ~120d."""
    dsp = r.get("days_since_push")
    if dsp is None:
        return 0.0
    return max(0.0, 1.0 - (dsp / 120.0))

# ---- Scoring -----------------------------------------------------------------
present = [n for n in CANDIDATES if n in by_name]
missing = [n for n in CANDIDATES if n not in by_name]

max_stars = max(by_name[n]["stars"] for n in present) or 1
max_mom = max((mom(by_name[n]) or 0) for n in present) or 1
max_bus = max((by_name[n].get("bus_factor") or 0) for n in present) or 1

WEIGHTS = {
    "health":    0.30,   # maintained, healthy
    "freshness": 0.20,   # recent activity
    "momentum":  0.20,   # growth right now
    "busfactor": 0.15,   # resilience to a maintainer leaving
    "adoption":  0.15,   # battle-tested by a large base (log-scaled)
}

def score_components(r):
    health = (r.get("health_score") or 0) / 100.0
    fresh = freshness(r)
    m = (mom(r) or 0) / max_mom
    bus = (r.get("bus_factor") or 0) / max_bus
    adopt = math.log10((r.get("stars") or 1) + 1) / math.log10(max_stars + 1)
    return {
        "health": health, "freshness": fresh, "momentum": m,
        "busfactor": bus, "adoption": adopt,
    }

def composite(r):
    c = score_components(r)
    return sum(WEIGHTS[k] * c[k] for k in WEIGHTS)

ranked = sorted(present, key=lambda n: -composite(by_name[n]))

# ---- Build -------------------------------------------------------------------
gen = cl.get("generatedAt", "")
user = cl.get("username", "")
lines = []
P = lines.append

P(f"# {TITLE}")
P("")
P(f"> Derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`), cross-referenced with the repo-similarity graph.")
P(">")
P(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/which_claw.py` (regenerate any time — no API cost).")
P("")
P("> **Scope.** This ranks the standalone **claws** — agents/runtimes you'd run *as* your "
  "assistant. The accessory ecosystem (skills, routers, memory, observability, dashboards) is "
  "covered separately in the **OpenClaw Ecosystem** report; those *complement* a claw rather "
  "than replace it.")
P("")

# ---- Verdict
HUB = "openclaw/openclaw"   # the ecosystem anchor — accessories all target this
top = ranked[0]
runner = ranked[1] if len(ranked) > 1 else None
healthiest = max(present, key=lambda n: by_name[n].get("health_score") or 0)
hub_rank = ranked.index(HUB) + 1 if HUB in ranked else None
secure_ranked = [n for n in ranked if CANDIDATES[n]["kind"] == "secure"]
coding_ranked = [n for n in ranked if CANDIDATES[n]["kind"] == "coding"]
P("## TL;DR — two honest answers")
P("")
P(f"**On raw metrics, [`{top}`]({by_name[top]['url']}) wins** (composite "
  f"{composite(by_name[top]):.3f}): health {by_name[top].get('health_score')}, bus factor "
  f"{by_name[top].get('bus_factor')}, very active. If you want the cleanest, most resilient "
  f"standalone claw and don't care about the surrounding tooling, take it.")
P("")
if HUB in by_name:
    P(f"**As a pragmatic default, [`{HUB}`]({by_name[HUB]['url']}) (composite "
      f"{composite(by_name[HUB]):.3f}, #{hub_rank}).** The score above *deliberately excludes the "
      f"ecosystem network effect* — and that's OpenClaw's real edge: every accessory you've "
      f"already starred (`clawhub`, `ClawRouter`, `clawmetry`, `opik-openclaw`, "
      f"`openclaw-supermemory`, `NemoClaw`, `moltworker`) targets OpenClaw, not zeroclaw. That's "
      f"a genuine switching cost in its favour.")
    P("")
    P(f"- **TypeScript + crypto fit → OpenClaw.** It's TS (so is most of its accessory line), and "
      f"the ecosystem leans on-chain — e.g. `ClawRouter` does on-chain payments / agent-native "
      f"settlement. If you live in the TS and crypto world, that's another argument for the hub.")
P(f"- **Maximum stability/quality →** [`{healthiest}`]({by_name[healthiest]['url']}) "
  f"(health {by_name[healthiest].get('health_score')}).")
if secure_ranked:
    s = secure_ranked[0]
    P(f"- **Running untrusted tools / need isolation →** [`{s}`]({by_name[s]['url']}) — "
      f"security-hardened runtime.")
if coding_ranked:
    c = coding_ranked[0]
    P(f"- **Mostly coding →** [`{c}`]({by_name[c]['url']}) is the coding-focused claw.")
P(f"- **Tiny/edge footprint →** `sipeed/picoclaw` and `nullclaw/nullclaw` (minimal builds).")
P("")

# ---- Ranking table
P("## The ranking")
P("")
P("Composite = "
  + " + ".join(f"{int(w*100)}% {k}" for k, w in WEIGHTS.items())
  + ". All inputs are precomputed dataset metrics; adoption is log-scaled so a 10× star lead "
  "doesn't swamp everything else.")
P("")
P("| # | Claw | Type | Score | ★ Stars | Health | Momentum (★/30d) | Last push | Bus factor | Lang |")
P("|---|---|---|---|---|---|---|---|---|---|")
for i, n in enumerate(ranked, 1):
    r = by_name[n]
    medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, str(i))
    P(f"| {medal} | [{n}]({r['url']}) | {KIND_LABEL[CANDIDATES[n]['kind']]} | "
      f"**{composite(r):.3f}** | {fmt_int(r['stars'])} | {r.get('health_score','—')} | "
      f"{fmt_int(mom(r)) if mom(r) is not None else '—'} | "
      f"{days_to_human(r.get('days_since_push'))} ago | {r.get('bus_factor','—')} | "
      f"{r.get('primary_language') or '—'} |")
P("")

# ---- Score breakdown for the top few
P("### How the top picks score (component view)")
P("")
P("Each column is 0–1 (higher = better); the bar shows the weighted composite.")
P("")
P("| Claw | Health | Fresh | Momentum | Bus | Adoption | Composite |")
P("|---|---|---|---|---|---|---|")
for n in ranked[:5]:
    r = by_name[n]
    c = score_components(r)
    P(f"| {n} | {c['health']:.2f} | {c['freshness']:.2f} | {c['momentum']:.2f} | "
      f"{c['busfactor']:.2f} | {c['adoption']:.2f} | **{composite(r):.3f}** |")
P("")

# ---- The one thing the score can't measure
P("## The one thing the score can't measure: network effect")
P("")
if HUB in by_name and top != HUB:
    P(f"`{top}` edges out `{HUB}` on the composite mostly on **health "
      f"({by_name[top].get('health_score')} vs {by_name[HUB].get('health_score')})** and "
      f"**bus factor ({by_name[top].get('bus_factor')} vs {by_name[HUB].get('bus_factor')})** — "
      f"both real, both in zeroclaw's favour. But the composite scores each claw *in isolation*. "
      f"It can't see that:")
    P("")
    P(f"- Your starred ecosystem is built **around OpenClaw** — `clawhub` (skills), `ClawRouter` "
      f"(routing, on-chain payments), `clawmetry` / `opik-openclaw` (observability), "
      f"`openclaw-supermemory` (memory), `NemoClaw` / `moltworker` (hosting). None of that plugs "
      f"into zeroclaw out of the box.")
    P(f"- OpenClaw is **TypeScript** end-to-end, which matches the rest of that tooling — and the "
      f"crypto/on-chain bent of the ecosystem (agent-native settlement) is a plus if that's your "
      f"world.")
    P(f"- zeroclaw is **Rust**: leaner and (per the metrics) cleaner, but you'd be re-building or "
      f"forgoing the accessory layer.")
    P("")
    P(f"**Net:** pick `{top}` if you want a single, self-contained, high-quality claw. Pick "
      f"`{HUB}` if you want a *platform* — the ecosystem lock-in is the feature, not the bug.")
    P("")

# ---- Decision routing
P("## Pick by what you care about")
P("")
P("| If your priority is… | Use | Why |")
P("|---|---|---|")
def pick(metric_fn, kind=None, reverse=True):
    pool = [n for n in present if kind is None or CANDIDATES[n]["kind"] == kind]
    return sorted(pool, key=lambda n: metric_fn(by_name[n]), reverse=reverse)[0]

p_health = pick(lambda r: r.get("health_score") or 0)
p_adopt = pick(lambda r: r.get("stars") or 0)
p_mom = pick(lambda r: mom(r) or 0)
p_bus = pick(lambda r: r.get("bus_factor") or 0)
P(f"| **Best on raw metrics** | [`{top}`]({by_name[top]['url']}) | tops the composite "
  f"(health/resilience/freshness) |")
P(f"| **Largest ecosystem & accessory support** | [`{HUB}`]({by_name[HUB]['url']}) | the hub "
  f"every skill/router/memory tool you've starred targets; TS + crypto-friendly |")
P(f"| **Code quality / least bus-factor risk** | [`{p_bus}`]({by_name[p_bus]['url']}) | highest "
  f"bus factor ({by_name[p_bus].get('bus_factor')}) — most resilient to a maintainer leaving |")
P(f"| **Best health score** | [`{p_health}`]({by_name[p_health]['url']}) | health "
  f"{by_name[p_health].get('health_score')} — cleanest maintenance signals |")
P(f"| **Fastest-growing right now** | [`{p_mom}`]({by_name[p_mom]['url']}) | "
  f"~{fmt_int(mom(by_name[p_mom]))} est. stars/30d |")
if secure_ranked:
    P(f"| **Security / sandboxed execution** | [`{secure_ranked[0]}`]"
      f"({by_name[secure_ranked[0]]['url']}) | hardened/containerized runtime |")
if coding_ranked:
    P(f"| **Coding agent** | [`{coding_ranked[0]}`]({by_name[coding_ranked[0]]['url']}) | "
      f"purpose-built for code |")
P(f"| **Tiny / edge / self-host cheap** | `sipeed/picoclaw` · `nullclaw/nullclaw` | minimal "
  f"footprints (Go / Zig) |")
P(f"| **Most-adopted / most battle-tested** | [`{p_adopt}`]({by_name[p_adopt]['url']}) | "
  f"{fmt_int(by_name[p_adopt]['stars'])}★ |")
P("")

# ---- Watch-outs
P("## Watch-outs")
P("")
flagged = False
for n in ranked:
    r = by_name[n]
    issues = []
    if (r.get("health_score") or 100) < 60:
        issues.append(f"health {r.get('health_score')}")
    if (r.get("days_since_push") or 0) > 45:
        issues.append(f"{r.get('days_since_push')}d since last push")
    if (r.get("bus_factor") or 0) <= 1:
        issues.append(f"bus factor {r.get('bus_factor')} (single-maintainer risk)")
    if issues:
        flagged = True
        P(f"- **{n}** — {'; '.join(issues)}.")
if not flagged:
    P("- No major red flags among the ranked claws at this snapshot.")
P("")
P("> Heads-up: `openagen/zeroclaw` (1.9k★, ~79d stale) is an **older, different** project from "
  "the healthy **`zeroclaw-labs/zeroclaw`** ranked above — don't confuse them.")
P("")

# ---- Methodology
P("## Methodology & caveats")
P("")
P("- **Source:** `public/data/classified.json` + `public/data/graph.json`. No external calls; "
  "fully reproducible.")
P("- **Candidate set:** standalone claw agents/runtimes/agent-OSes only. Accessories (skills, "
  "routers, memory, observability, dashboards, specialized one-task agents) are excluded by "
  "design — see the OpenClaw Ecosystem report for those.")
P(f"- **Composite weights:** "
  + ", ".join(f"{k} {int(w*100)}%" for k, w in WEIGHTS.items())
  + ". Adoption is log-scaled. Freshness decays linearly to ~0 by 120 days since last push.")
P("- **Snapshot-bound.** Claws move weekly; momentum especially can flip fast. Re-run after a "
  "fresh `npm run refresh`.")
if missing:
    P(f"- **Not in dataset (skipped):** {', '.join('`'+m+'`' for m in missing)}.")
P("")
P(f"<sub>Claws ranked: {len(present)} · Snapshot: {gen} · "
  f"regenerate via scripts/reports/which_claw.py</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# ---- Sidecar meta ------------------------------------------------------------
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Comparison",
    "summary": (f"Decision report ranking {len(present)} standalone OpenClaw-family claws "
                f"(agents/runtimes) on a transparent composite (health, freshness, momentum, "
                f"resilience, adoption). Winner: {top}. Includes use-case routing "
                f"(security, coding, edge, stability)."),
    "tool_count": len(present),
    "total_stars": sum(by_name[n]["stars"] for n in present),
    "categories": {KIND_LABEL[k]: sum(1 for n in present if CANDIDATES[n]["kind"] == k)
                   for k in KIND_LABEL},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in ranked[:5]],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/which_claw.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  ranked: {len(present)} / {len(CANDIDATES)}  | winner: {top}")
if missing:
    print("  WARNING missing:", missing)

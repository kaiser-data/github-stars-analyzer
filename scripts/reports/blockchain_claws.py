#!/usr/bin/env python3
"""
Decision report: which claw is best for the **blockchain / web3 / DeFi** world,
and which **skills/tools** (on-chain data, valuation, trading, payments, MCP
infra, security) are superb for which purpose.

A claw doesn't analyze chains by itself — it orchestrates on-chain tooling. So
this report has two halves: (1) rate the claws on blockchain-fitness, (2) map
the skills/tools in the stars to the job each is best at, then assemble stacks.

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/blockchain-claws.md  (+ reports/blockchain-claws.meta.json)

Run: python3 scripts/reports/blockchain_claws.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "blockchain-claws"
TITLE = "Which Claw for the Blockchain World? — Claws & Skills for On-Chain / DeFi"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Claws rated on blockchain-fitness (signals from each repo's own topics/desc) ----
# fit: High / Medium / Low.  Each flag is a concrete, checkable attribute.
CLAWS = {
    "elizaOS/eliza": {
        "fit": "High", "crypto_native": True, "mcp": True, "onchain_pay": False,
        "why": "The **only crypto-native claw** — `crypto`/web3 topics, wallet & chain plugins, "
               "autonomous on-chain agents. Best when the agent should *act* on-chain, not just read."},
    "openclaw/openclaw": {
        "fit": "High", "crypto_native": False, "mcp": True, "onchain_pay": True,
        "why": "Not crypto-native itself, but **MCP-native + on-chain-settled ecosystem**: wire in a "
               "blockscout MCP for reads, and `ClawRouter` already does USDC payments on Base & Solana "
               "(x402). The pragmatic DeFi *analysis* hub, and it's TypeScript."},
    "RightNow-AI/openfang": {
        "fit": "Medium", "crypto_native": False, "mcp": True, "onchain_pay": False,
        "why": "**MCP-native Agent-OS** (Rust) — a clean backbone for plugging chain-data MCP servers, "
               "if you don't need crypto-specific plugins out of the box."},
    "nearai/ironclaw": {
        "fit": "Medium", "crypto_native": False, "mcp": True, "onchain_pay": False,
        "why": "Privacy/security agent-OS with **WASM-sandboxed CodeAct** — valuable when the agent "
               "executes untrusted contract code or keys must stay isolated."},
    "nanocoai/nanoclaw": {
        "fit": "Medium", "crypto_native": False, "mcp": True, "onchain_pay": False,
        "why": "Containerised + chat connectors — good for a **sandboxed wallet/alert bot** on "
               "Telegram/Discord that watches positions and pings you."},
    "NousResearch/hermes-agent": {
        "fit": "Low", "crypto_native": False, "mcp": True, "onchain_pay": False,
        "why": "General Python agent; no crypto specialisation, but the strongest functional claw if "
               "you'd build the chain integration yourself in Python."},
    "zeroclaw-labs/zeroclaw": {
        "fit": "Low", "crypto_native": False, "mcp": False, "onchain_pay": False,
        "why": "Highest-quality general claw, but no crypto/MCP affordances — you'd wire everything "
               "by hand."},
}

# ---- Skills / tools by purpose (all present in the starred dataset) ----------
# Each entry: repo, the purpose it's superb at, and a one-line why.
SKILLS = {
    "On-chain data & explorer": [
        ("blockscout/blockscout",
         "Read positions, txs, token balances across EVM chains; exposes an MCP server → plugs "
         "straight into a claw."),
    ],
    "Valuation, market data & quant": [
        ("OpenBB-finance/OpenBB",
         "Financial data platform explicitly 'for analysts, quants and **AI agents**' — crypto + "
         "derivatives coverage to price and value positions."),
    ],
    "Autonomous trading agents": [
        ("TauricResearch/TradingAgents",
         "Multi-agent LLM trading framework — orchestrate it *from* a claw for strategy/execution."),
        ("HKUDS/AI-Trader",
         "Fully-automated agent-native trading loop."),
        ("ValueCell-ai/valuecell",
         "Community multi-agent platform for finance (crypto + equity); MCP-enabled."),
    ],
    "Agentic payments & settlement": [
        ("BlockRunAI/ClawRouter",
         "Agent-native LLM router with **USDC payments on Base & Solana via x402** — settle agent "
         "spend on-chain. Built for OpenClaw."),
        ("Merit-Systems/x402scan",
         "x402 ecosystem explorer — inspect agentic stablecoin payment flows."),
    ],
    "MCP infrastructure (wire any chain in)": [
        ("modelcontextprotocol/servers",
         "Official MCP server collection — the integration layer for chain-data tools."),
        ("punkpeye/awesome-mcp-servers",
         "Directory of MCP servers (incl. blockchain/explorer servers)."),
        ("ComposioHQ/awesome-claude-skills",
         "Curated Claude skills — reusable capabilities to bolt onto a claw."),
    ],
    "Security & crypto primitives": [
        ("sobolevn/awesome-cryptography",
         "Reference for cryptography primitives — key handling, signing, hashing."),
    ],
}

# ---- Recommended stacks ------------------------------------------------------
STACKS = [
    ("Analyze / monitor DeFi positions (read & reason)",
     ["openclaw/openclaw", "blockscout/blockscout", "OpenBB-finance/OpenBB"],
     "Read-and-reason job. openclaw (MCP) pulls on-chain state via a blockscout MCP, OpenBB values "
     "it. Add `ClawRouter` if you want agent spend settled in USDC."),
    ("Crypto-native agent that acts on-chain",
     ["elizaOS/eliza", "blockscout/blockscout"],
     "eliza is purpose-built for web3 — wallet/chain plugins to execute, blockscout to verify."),
    ("Autonomous trading on positions",
     ["openclaw/openclaw", "TauricResearch/TradingAgents", "OpenBB-finance/OpenBB"],
     "Claw orchestrates a dedicated trading framework; OpenBB supplies market/quant data."),
    ("Agentic payments / x402 settlement",
     ["openclaw/openclaw", "BlockRunAI/ClawRouter", "Merit-Systems/x402scan"],
     "USDC settlement on Base/Solana via x402, with x402scan for flow inspection."),
]

# ---- Load --------------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
by_name = {r["full_name"]: r for r in cl["repos"]}

def fmt_int(n):
    try:
        return f"{int(n):,}"
    except Exception:
        return str(n)

def meta_bits(n):
    r = by_name.get(n)
    if not r:
        return "—", "—", "—", "—"
    return (fmt_int(r["stars"]), r.get("primary_language") or "—",
            r.get("health_score", "—"), r.get("bus_factor", "—"))

FIT_BADGE = {"High": "🟢 High", "Medium": "🟡 Medium", "Low": "⚪ Low"}
FIT_ORDER = {"High": 0, "Medium": 1, "Low": 2}

# ---- Build -------------------------------------------------------------------
gen = cl.get("generatedAt", "")
user = cl.get("username", "")
lines = []
P = lines.append

P(f"# {TITLE}")
P("")
P(f"> Derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`).")
P(">")
P(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/blockchain_claws.py` (regenerate any time — no API cost).")
P("")
P("> **Key idea.** No claw analyzes chains by itself — a claw is the *orchestrator*; it needs "
  "on-chain **skills/tools** wired in. So this report has two halves: which **claw** to run, and "
  "which **skills** are superb for which purpose. Both are drawn only from tools already in your "
  "stars.")
P("")

# --- Verdict
P("## Verdict")
P("")
P("- **Analyzing / monitoring DeFi positions (read & reason)** → **`openclaw`**. It's MCP-native "
  "(plug a blockscout MCP for on-chain reads + OpenBB for valuation) and its ecosystem already "
  "settles on-chain (`ClawRouter`, USDC on Base & Solana via x402). TypeScript — fits a web3 stack.")
P("- **A crypto-native agent that *acts* on-chain** → **`elizaOS/eliza`**. The only claw built for "
  "web3 (wallet/chain plugins, autonomous on-chain agents).")
P("- **Everything else is the skills layer** — blockscout (data), OpenBB (valuation), "
  "TradingAgents/AI-Trader (trading), ClawRouter/x402scan (payments) — orchestrated *by* the claw.")
P("")

# --- Claw blockchain-fitness table
P("## Claws rated for blockchain-fitness")
P("")
P("Flags are concrete, checkable attributes — *crypto-native* (built-in web3 plugins), "
  "*MCP* (can plug chain-data MCP servers), *on-chain pay* (settles in stablecoin).")
P("")
P("| Claw | Fit | Crypto-native | MCP | On-chain pay | ★ | Lang | Health | Why |")
P("|---|---|---|---|---|---|---|---|---|")
def yn(b):
    return "✅" if b else "—"
for n in sorted(CLAWS, key=lambda n: (FIT_ORDER[CLAWS[n]["fit"]], -(by_name.get(n, {}).get("stars") or 0))):
    c = CLAWS[n]
    stars, lang, health, bus = meta_bits(n)
    r = by_name.get(n, {})
    P(f"| [{n.split('/')[-1]}]({r.get('url','#')}) | {FIT_BADGE[c['fit']]} | {yn(c['crypto_native'])} | "
      f"{yn(c['mcp'])} | {yn(c['onchain_pay'])} | {stars} | {lang} | {health} | {c['why']} |")
P("")

# --- Skills by purpose
P("## Skills & tools — superb for which purpose")
P("")
P("The capability layer a claw orchestrates. Pick per job; most stacks combine 2–3.")
P("")
for purpose, items in SKILLS.items():
    P(f"### {purpose}")
    P("")
    for n, why in items:
        stars, lang, health, bus = meta_bits(n)
        r = by_name.get(n, {})
        tag = "" if n in by_name else " _(not in stars)_"
        P(f"- **[{n.split('/')[-1]}]({r.get('url','https://github.com/'+n)})**{tag} · {stars}★ · "
          f"{lang} · health {health} — {why}")
    P("")

# --- Recommended stacks
P("## Recommended stacks")
P("")
P("Claw + skills, assembled by goal:")
P("")
for title, parts, why in STACKS:
    chain = " + ".join(f"`{p.split('/')[-1]}`" for p in parts)
    P(f"- **{title}**  ")
    P(f"  {chain}  ")
    P(f"  {why}")
P("")

# --- Caveats
P("## Caveats")
P("")
P("- **Snapshot-bound** to the May-2026 dataset; crypto tooling moves weekly. Re-verify before "
  "wiring anything that touches funds.")
P("- **Skills ≠ audited.** `awesome-*` lists and MCP servers are starting points, not vetted "
  "dependencies — review any tool that signs transactions or holds keys.")
P("- **A claw orchestrates; it doesn't custody.** Keep signing/keys in a sandboxed, least-"
  "privilege layer (see ironclaw/nanoclaw) — never hand raw keys to a general assistant.")
P("- Fit ratings are editorial (based on each repo's own topics/description); stars/health/bus "
  "factor are precomputed dataset metrics.")
P("")
P(f"<sub>Snapshot: {gen} · regenerate via scripts/reports/blockchain_claws.py</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# ---- Sidecar meta ------------------------------------------------------------
skill_repos = [n for items in SKILLS.values() for n, _ in items if n in by_name]
present_claws = [n for n in CLAWS if n in by_name]
covered = present_claws + skill_repos
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Comparison",
    "summary": ("Which claw is best for blockchain/web3/DeFi (eliza = crypto-native; openclaw = "
                "MCP + on-chain-payments analysis hub) plus a skills-by-purpose map — on-chain data "
                "(blockscout), valuation (OpenBB), trading (TradingAgents), payments "
                "(ClawRouter/x402) — and ready-made stacks for analyzing DeFi positions."),
    "tool_count": len(set(covered)),
    "total_stars": sum(by_name[n]["stars"] for n in set(covered)),
    "categories": {p: len(items) for p, items in SKILLS.items()},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]}
                  for n in sorted(set(covered), key=lambda x: -by_name[x]["stars"])[:5]],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/blockchain_claws.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  claws: {len(present_claws)}/{len(CLAWS)} | skill repos: {len(skill_repos)}")
missing = [n for n in list(CLAWS) + [s for items in SKILLS.values() for s, _ in items]
           if n not in by_name]
if missing:
    print("  NOTE not in stars:", missing)

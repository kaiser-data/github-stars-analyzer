#!/usr/bin/env python3
"""
"Blockchain Repos You Need to Know" — a dataset-derived field guide to the
essential blockchain / web3 / DeFi repositories in the starred-repos dataset,
organized by layer, with live metrics, a hottest-trends section, and a
where-to-start learning path.

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/blockchain-essentials.md  (+ reports/blockchain-essentials.meta.json)

Run: python3 scripts/reports/blockchain_essentials.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "blockchain-essentials"
TITLE = "Blockchain Repos You Need to Know — A Field Guide"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# Layered map of the essential repos. Keys are dataset full_names (post-redirect);
# `ext` entries are referenced but not in the dataset (e.g. archived). Each tuple:
# (full_name, one-line role).
LAYERS = [
    ("Languages & compilers", "What you write contracts in.", [
        ("argotorg/solidity", "The Solidity compiler & language (ex ethereum/solidity)."),
        ("vyperlang/vyper", "Pythonic contract language; security-minded alternative."),
    ]),
    ("Dev toolkits", "Build, test, fuzz, deploy.", [
        ("foundry-rs/foundry", "Forge/Cast/Anvil — the dominant Rust-based Solidity toolchain."),
        ("NomicFoundation/hardhat", "The established JS/TS dev environment."),
    ]),
    ("Contract libraries & standards", "Don't reinvent ERC-20/721; reuse audited code.", [
        ("OpenZeppelin/openzeppelin-contracts", "The standard audited token/access/proxy library."),
        ("Vectorized/solady", "Gas-optimized Solidity building blocks."),
        ("transmissions11/solmate", "Minimalist, modern contract primitives."),
    ]),
    ("Security & analysis", "Catch bugs before mainnet.", [
        ("crytic/slither", "The go-to static analyzer for contract vulnerabilities."),
        ("crytic/echidna", "Property-based fuzzer for smart contracts."),
    ]),
    ("Client libraries (TS/JS)", "Talk to chains from apps.", [
        ("wevm/viem", "Modern, type-safe Ethereum client — default for new TS apps."),
        ("wevm/wagmi", "React hooks for Ethereum (pairs with viem)."),
        ("ethers-io/ethers.js", "The long-time standard JS/TS library."),
        ("rainbow-me/rainbowkit", "Drop-in wallet-connection UX for dApps."),
    ]),
    ("Execution clients (nodes)", "The chain itself.", [
        ("ethereum/go-ethereum", "geth — the reference Ethereum node (Go)."),
        ("paradigmxyz/reth", "Modern, fast Rust client (rising alternative)."),
        ("NethermindEth/nethermind", "High-perf .NET client, strong on tooling."),
    ]),
    ("Oracles, AA & wallets", "Price feeds, smart accounts, custody.", [
        ("smartcontractkit/chainlink", "Price feeds you need to value positions."),
        ("eth-infinitism/account-abstraction", "Reference ERC-4337 account-abstraction."),
        ("safe-fndn/safe-smart-account", "Safe multisig — treasury/custody standard."),
    ]),
    ("Indexing & on-chain data", "Turn raw chain state into queries.", [
        ("graphprotocol/graph-node", "The Graph — index chains into queryable subgraphs."),
        ("blockscout/blockscout", "Open EVM explorer; exposes an MCP server for agents."),
    ]),
    ("DeFi protocol references", "Read the canonical contracts.", [
        ("Uniswap/v4-core", "Latest AMM/DEX core (hooks)."),
        ("Uniswap/v3-core", "The concentrated-liquidity AMM still everywhere."),
        ("compound-finance/comet", "Compound III lending."),
    ]),
    ("Solana", "The largest non-EVM L1.", [
        ("otter-sec/anchor", "The standard Solana smart-contract framework."),
        ("anza-xyz/agave", "The Solana validator client."),
        ("solana-foundation/solana-web3.js", "JS SDK for Solana."),
    ]),
    ("Zero-knowledge", "Proofs, privacy, scaling.", [
        ("succinctlabs/sp1", "Performant RISC-V zkVM."),
        ("risc0/risc0", "General-purpose zkVM."),
        ("iden3/circom", "Circuit compiler for zk-SNARKs."),
    ]),
    ("🔥 Agentic payments (x402)", "AI agents settling on-chain — the breakout trend.", [
        ("coinbase/x402", "The payments-over-HTTP protocol everyone's building on."),
        ("BlockRunAI/ClawRouter", "Agent LLM router with USDC payments on Base & Solana via x402."),
        ("Merit-Systems/x402scan", "x402 ecosystem explorer."),
    ]),
    ("🔥 AI × finance / trading", "Where crypto meets the agent stack.", [
        ("TauricResearch/TradingAgents", "Multi-agent LLM trading framework."),
        ("HKUDS/AI-Trader", "Fully-automated agent-native trading."),
        ("elizaOS/eliza", "Crypto-native agent OS (wallet/chain plugins)."),
        ("OpenBB-finance/OpenBB", "Financial data platform 'for analysts, quants & AI agents'."),
    ]),
]

# Referenced-but-not-in-dataset (e.g. archived). Shown as honest footnotes.
EXTERNAL = {
    "aave/aave-v3-core": "Leading lending protocol — but the v3-core repo is **archived** "
                         "upstream (active dev moved on), so it's not in the live dataset. Still "
                         "the canonical reference for lending/health-factor logic.",
}

# ---- Load --------------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)
by_name = {r["full_name"]: r for r in cl["repos"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}
nodes_by_id = {n["id"]: n for n in gr["nodes"]}

def fmt_int(n):
    try:
        return f"{int(n):,}"
    except Exception:
        return str(n)

def mom(r):
    return (r.get("momentum") or {}).get("estimated_stars_30d") or 0

def hotness(r):
    s = mom(r) / 1000.0
    s += (r.get("commits_90d") or 0) / 50.0
    s += {"Hot": 30, "Rising": 25, "Mature": 8, "Classic": 5,
          "Declining": -5, "Abandoned": -20}.get(r.get("lifecycle_stage"), 0)
    s += max(0, 30 - (r.get("days_since_push") or 99))
    return s

def life_badge(r):
    return {"Hot": "🔥 Hot", "Rising": "📈 Rising", "Mature": "🟢 Mature",
            "Classic": "🔵 Classic", "Declining": "🟠 Declining",
            "Abandoned": "⚫ Abandoned"}.get(r.get("lifecycle_stage"), r.get("lifecycle_stage") or "—")

# all repos referenced in the layer map that exist in the dataset
all_repos = [n for _, _, items in LAYERS for n, _ in items if n in by_name]

# ---- Build -------------------------------------------------------------------
gen = cl.get("generatedAt", "")
user = cl.get("username", "")
lines = []
P = lines.append

P(f"# {TITLE}")
P("")
P(f"> Derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`), cross-referenced with the repo-similarity graph "
  f"({fmt_int(len(gr['nodes']))} nodes / {fmt_int(len(gr['links']))} edges).")
P(">")
P(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/blockchain_essentials.py` (regenerate any time — no API cost).")
P("")
P("> **What this is.** The essential blockchain/web3/DeFi repos worth knowing, organized by "
  "**layer** (language → toolchain → libraries → clients → protocols → ZK → the AI×crypto edge), "
  "with live metrics. Start at the top of each layer and work down.")
P("")

# --- Hottest trends (lead with it)
P("## 🔥 What's hot right now")
P("")
P("Ranked by a composite of momentum, 90-day commit velocity, lifecycle stage and recency. The "
  "heat in blockchain today is **AI agents transacting on-chain**, not the (mature, stable) base "
  "toolchain.")
P("")
hot_sorted = sorted(all_repos, key=lambda n: -hotness(by_name[n]))[:8]
P("| Repo | Layer-fit | ★ | Lifecycle | Momentum (★/30d) | Commits (90d) |")
P("|---|---|---|---|---|---|")
# map repo -> layer label for context
repo_layer = {n: lab for lab, _, items in LAYERS for n, _ in items}
for n in hot_sorted:
    r = by_name[n]
    P(f"| [{n.split('/')[-1]}]({r['url']}) | {repo_layer.get(n,'')} | {fmt_int(r['stars'])} | "
      f"{life_badge(r)} | {fmt_int(mom(r))} | {fmt_int(r.get('commits_90d'))} |")
P("")
P("**Two trends to watch:**")
P("")
P("1. **Agentic payments (x402).** `coinbase/x402` (payments over HTTP) + `ClawRouter` (USDC on "
  "Base & Solana) + `x402scan` — agent-to-agent stablecoin settlement, brand-new and "
  "accelerating. The most genuinely *novel* movement here.")
P("2. **Autonomous AI trading.** `TauricResearch/TradingAgents` (82k★) and `HKUDS/AI-Trader` are "
  "high-momentum, and `elizaOS/eliza` ships at enormous velocity "
  f"({fmt_int(by_name['elizaOS/eliza'].get('commits_90d')) if 'elizaOS/eliza' in by_name else '—'} "
  "commits/90d).")
P("")
P("**Quiet but foundational:** Rust is taking over the client/tooling layer — `agave`, `reth`, "
  "`foundry` all show very high 90-day commit counts despite mature/low momentum. High build "
  "activity, not hype.")
P("")

# --- Layer-by-layer field guide
P("## The field guide, by layer")
P("")
for label, blurb, items in LAYERS:
    present = [(n, role) for n, role in items if n in by_name]
    if not present:
        continue
    P(f"### {label}")
    P(f"_{blurb}_")
    P("")
    P("| Repo | ★ | Lifecycle | Health | Lang | Role |")
    P("|---|---|---|---|---|---|")
    for n, role in sorted(present, key=lambda x: -by_name[x[0]]["stars"]):
        r = by_name[n]
        P(f"| [{n.split('/')[-1]}]({r['url']}) | {fmt_int(r['stars'])} | {life_badge(r)} | "
          f"{r.get('health_score','—')} | {r.get('primary_language') or '—'} | {role} |")
    P("")

# --- External / archived footnotes
if EXTERNAL:
    P("### Referenced but not in the live dataset")
    P("")
    for n, note in EXTERNAL.items():
        P(f"- **[{n}](https://github.com/{n})** — {note}")
    P("")

# --- Where to start
P("## Where to start (a learning path)")
P("")
P("If you're ramping on EVM/DeFi development, in order:")
P("")
P("1. **Language** → `solidity` (read the docs, write a token).")
P("2. **Toolchain** → `foundry` (Forge for build/test/fuzz; Anvil for a local node).")
P("3. **Stand on giants** → `openzeppelin-contracts` (inherit audited standards).")
P("4. **Make it safe** → `slither` + `echidna` (static analysis + fuzzing) before you ship.")
P("5. **Build the app** → `viem` + `wagmi` (+ `rainbowkit` for wallet UX).")
P("6. **Read real DeFi** → `Uniswap/v4-core`, `compound/comet` to see production patterns.")
P("7. **Get the data** → `graph-node` (subgraphs) + `blockscout` (explorer/MCP) to analyze "
  "positions.")
P("8. **The frontier** → `coinbase/x402` + `ClawRouter` if you're wiring agents to move value.")
P("")
P("> For **analyzing DeFi positions specifically**, the practical stack is "
  "`openclaw + blockscout (MCP reads) + OpenBB (valuation)` — see the **Blockchain Claws** "
  "report. For **what's still missing**, see **Recommended to Star — Blockchain / DeFi Gaps**.")
P("")

# --- Caveats
P("## Caveats")
P("")
P("- **Snapshot-bound** to the dataset; crypto moves weekly. Metrics (stars, lifecycle, health, "
  "momentum) are precomputed by the analyzer pipeline.")
P("- **Curation is editorial** — the layer map is hand-built; inclusion means 'worth knowing', "
  "not 'exhaustive'. Repo names reflect post-redirect owners (e.g. `argotorg/solidity`, "
  "`otter-sec/anchor`, `safe-fndn/...`).")
P("- **Stars ≠ endorsement to run in production**, especially anything touching funds — audit "
  "first.")
P("")
P(f"<sub>Essential repos mapped: {len(all_repos)} across {sum(1 for l in LAYERS if any(n in by_name for n,_ in l[2]))} "
  f"layers · Snapshot: {gen} · regenerate via scripts/reports/blockchain_essentials.py</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# ---- Sidecar meta ------------------------------------------------------------
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Comparison",
    "summary": (f"A layered field guide to the {len(all_repos)} essential blockchain/web3/DeFi "
                "repos in the dataset — languages, toolchains, libraries, clients, DeFi protocols, "
                "ZK, Solana — plus the hottest AI×crypto trends (x402 agentic payments, autonomous "
                "trading) and a where-to-start learning path."),
    "tool_count": len(all_repos),
    "total_stars": sum(by_name[n]["stars"] for n in all_repos),
    "categories": {label: sum(1 for n, _ in items if n in by_name)
                   for label, _, items in LAYERS if any(n in by_name for n, _ in items)},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]}
                  for n in sorted(all_repos, key=lambda x: -by_name[x]["stars"])[:5]],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/blockchain_essentials.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  essential repos mapped: {len(all_repos)}")
missing = [n for _, _, items in LAYERS for n, _ in items if n not in by_name]
if missing:
    print("  NOTE not in dataset:", missing)

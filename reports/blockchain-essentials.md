# Blockchain Repos You Need to Know — A Field Guide

> Derived from **kaiser-data**'s 2,159 starred repos (snapshot `2026-09-14T11:08:08.535Z`), cross-referenced with the repo-similarity graph (2,159 nodes / 7,086 edges).
>
> Generated 2026-09-14 by `scripts/reports/blockchain_essentials.py` (regenerate any time — no API cost).

![Top tools by stars](assets/blockchain-essentials-top-tools.svg)

![Tools per category](assets/blockchain-essentials-categories.svg)


> **What this is.** The essential blockchain/web3/DeFi repos worth knowing, organized by **layer** (language → toolchain → libraries → clients → protocols → ZK → the AI×crypto edge), with live metrics. Start at the top of each layer and work down.

## 🔥 What's hot right now

Ranked by a composite of momentum, 90-day commit velocity, lifecycle stage and recency. The heat in blockchain today is **AI agents transacting on-chain**, not the (mature, stable) base toolchain.

| Repo | Layer-fit | ★ | Lifecycle | Momentum (★/30d) | Commits (90d) |
|---|---|---|---|---|---|
| [eliza](https://github.com/elizaOS/eliza) | 🔥 AI × finance / trading | 19,332 | 🟢 Mature | 1,273 | 22,110 |
| [x402scan](https://github.com/Merit-Systems/x402scan) | 🔥 Agentic payments (x402) | 388 | 🔥 Hot | 82 | 110 |
| [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 🔥 AI × finance / trading | 105,629 | 🟢 Mature | 10,769 | 61 |
| [viem](https://github.com/wevm/viem) | Client libraries (TS/JS) | 3,554 | 🔵 Classic | 88 | 225 |
| [sp1](https://github.com/succinctlabs/sp1) | Zero-knowledge | 1,733 | 🟢 Mature | 90 | 52 |
| [ClawRouter](https://github.com/BlockRunAI/ClawRouter) | 🔥 Agentic payments (x402) | 6,597 | 🔥 Hot | 2,221 | 183 |
| [blockscout](https://github.com/blockscout/blockscout) | Indexing & on-chain data | 4,684 | 🔵 Classic | 55 | 175 |
| [anchor](https://github.com/otter-sec/anchor) | Solana | 5,132 | 🔵 Classic | 92 | 85 |

**Two trends to watch:**

1. **Agentic payments (x402).** `coinbase/x402` (payments over HTTP) + `ClawRouter` (USDC on Base & Solana) + `x402scan` — agent-to-agent stablecoin settlement, brand-new and accelerating. The most genuinely *novel* movement here.
2. **Autonomous AI trading.** `TauricResearch/TradingAgents` (82k★) and `HKUDS/AI-Trader` are high-momentum, and `elizaOS/eliza` ships at enormous velocity (22,110 commits/90d).

**Quiet but foundational:** Rust is taking over the client/tooling layer — `agave`, `reth`, `foundry` all show very high 90-day commit counts despite mature/low momentum. High build activity, not hype.

## The field guide, by layer

### Languages & compilers
_What you write contracts in._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [solidity](https://github.com/argotorg/solidity) | 25,737 (▲15) | 🔵 Classic | 84 | C++ | The Solidity compiler & language (ex ethereum/solidity). |
| [vyper](https://github.com/vyperlang/vyper) | 5,181 | 🔵 Classic | 72 | Python | Pythonic contract language; security-minded alternative. |

### Dev toolkits
_Build, test, fuzz, deploy._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [foundry](https://github.com/foundry-rs/foundry) | 10,598 (▲19) | 🔵 Classic | 85 | Rust | Forge/Cast/Anvil — the dominant Rust-based Solidity toolchain. |
| [hardhat](https://github.com/NomicFoundation/hardhat) | 8,505 (▲1) | 🔵 Classic | 78 | TypeScript | The established JS/TS dev environment. |

### Contract libraries & standards
_Don't reinvent ERC-20/721; reuse audited code._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | 27,240 (▲9) | 🔵 Classic | 82 | Solidity | The standard audited token/access/proxy library. |
| [solmate](https://github.com/transmissions11/solmate) | 4,284 (▼1) | ⚫ Abandoned | 6 | Solidity | Minimalist, modern contract primitives. |
| [solady](https://github.com/Vectorized/solady) | 3,372 (▲3) | 🟢 Mature | 51 | Solidity | Gas-optimized Solidity building blocks. |

### Security & analysis
_Catch bugs before mainnet._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [slither](https://github.com/crytic/slither) | 6,361 (▲5) | 🔵 Classic | 61 | Python | The go-to static analyzer for contract vulnerabilities. |
| [echidna](https://github.com/crytic/echidna) | 3,176 (▲3) | 🔵 Classic | 70 | Haskell | Property-based fuzzer for smart contracts. |

### Client libraries (TS/JS)
_Talk to chains from apps._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [ethers.js](https://github.com/ethers-io/ethers.js) | 8,716 (▲2) | 🟢 Mature | 46 | TypeScript | The long-time standard JS/TS library. |
| [wagmi](https://github.com/wevm/wagmi) | 6,747 (▲3) | 🔵 Classic | 74 | TypeScript | React hooks for Ethereum (pairs with viem). |
| [viem](https://github.com/wevm/viem) | 3,554 (▲5) | 🔵 Classic | 85 | TypeScript | Modern, type-safe Ethereum client — default for new TS apps. |
| [rainbowkit](https://github.com/rainbow-me/rainbowkit) | 2,835 (▼1) | 🟢 Mature | 44 | MDX | Drop-in wallet-connection UX for dApps. |

### Execution clients (nodes)
_The chain itself._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [go-ethereum](https://github.com/ethereum/go-ethereum) | 51,343 (▲14) | 🔵 Classic | 95 | Go | geth — the reference Ethereum node (Go). |
| [reth](https://github.com/paradigmxyz/reth) | 5,772 (▲7) | 🔵 Classic | 80 | Rust | Modern, fast Rust client (rising alternative). |
| [nethermind](https://github.com/NethermindEth/nethermind) | 1,596 (▲4) | 🔵 Classic | 84 | C# | High-perf .NET client, strong on tooling. |

### Oracles, AA & wallets
_Price feeds, smart accounts, custody._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [chainlink](https://github.com/smartcontractkit/chainlink) | 8,244 (▲5) | 🔵 Classic | 98 | Go | Price feeds you need to value positions. |
| [safe-smart-account](https://github.com/safe-fndn/safe-smart-account) | 2,178 (▲1) | 🟢 Mature | 47 | TypeScript | Safe multisig — treasury/custody standard. |
| [account-abstraction](https://github.com/eth-infinitism/account-abstraction) | 1,938 (▲1) | 🟠 Declining | 22 | TypeScript | Reference ERC-4337 account-abstraction. |

### Indexing & on-chain data
_Turn raw chain state into queries._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [blockscout](https://github.com/blockscout/blockscout) | 4,684 (▲16) | 🔵 Classic | 85 | Elixir | Open EVM explorer; exposes an MCP server for agents. |
| [graph-node](https://github.com/graphprotocol/graph-node) | 3,147 (▲2) | 🔵 Classic | 70 | Rust | The Graph — index chains into queryable subgraphs. |

### DeFi protocol references
_Read the canonical contracts._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [v3-core](https://github.com/Uniswap/v3-core) | 5,022 (▲2) | 🟢 Mature | 34 | TypeScript | The concentrated-liquidity AMM still everywhere. |
| [v4-core](https://github.com/Uniswap/v4-core) | 2,529 (▲3) | 🟢 Mature | 28 | Solidity | Latest AMM/DEX core (hooks). |
| [comet](https://github.com/compound-finance/comet) | 312 | 🟢 Mature | 37 | TypeScript | Compound III lending. |

### Solana
_The largest non-EVM L1._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [anchor](https://github.com/otter-sec/anchor) | 5,132 (▲5) | 🔵 Classic | 82 | Rust | The standard Solana smart-contract framework. |
| [solana-web3.js](https://github.com/solana-foundation/solana-web3.js) | 2,756 (▲3) | 🟢 Mature | 61 | TypeScript | JS SDK for Solana. |
| [agave](https://github.com/anza-xyz/agave) | 1,911 (▲7) | 🟢 Mature | 97 | Rust | The Solana validator client. |

### Zero-knowledge
_Proofs, privacy, scaling._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [risc0](https://github.com/risc0/risc0) | 2,188 | 🟢 Mature | 54 | C++ | General-purpose zkVM. |
| [sp1](https://github.com/succinctlabs/sp1) | 1,733 (▼1) | 🟢 Mature | 79 | Rust | Performant RISC-V zkVM. |
| [circom](https://github.com/iden3/circom) | 1,691 (▲1) | 🟢 Mature | 37 | WebAssembly | Circuit compiler for zk-SNARKs. |

### 🔥 Agentic payments (x402)
_AI agents settling on-chain — the breakout trend._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [ClawRouter](https://github.com/BlockRunAI/ClawRouter) | 6,597 (▲16) | 🔥 Hot | 80 | TypeScript | Agent LLM router with USDC payments on Base & Solana via x402. |
| [x402scan](https://github.com/Merit-Systems/x402scan) | 388 (▲3) | 🔥 Hot | 79 | TypeScript | x402 ecosystem explorer. |
| [x402](https://github.com/coinbase/x402) | 153 (▲3) | 🟠 Declining | 34 | TypeScript | The payments-over-HTTP protocol everyone's building on. |

### 🔥 AI × finance / trading
_Where crypto meets the agent stack._

| Repo | ★ | Lifecycle | Health | Lang | Role |
|---|---|---|---|---|---|
| [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 105,629 (▲2,980) | 🟢 Mature | 72 | Python | Multi-agent LLM trading framework. |
| [OpenBB](https://github.com/OpenBB-finance/OpenBB) | 72,981 (▲274) | 🔵 Classic | 68 | Python | Financial data platform 'for analysts, quants & AI agents'. |
| [AI-Trader](https://github.com/HKUDS/AI-Trader) | 22,317 (▲139) | 🟠 Declining | 29 | Python | Fully-automated agent-native trading. |
| [eliza](https://github.com/elizaOS/eliza) | 19,332 (▲71) | 🟢 Mature | 79 | TypeScript | Crypto-native agent OS (wallet/chain plugins). |

### Referenced but not in the live dataset

- **[aave/aave-v3-core](https://github.com/aave/aave-v3-core)** — Leading lending protocol — but the v3-core repo is **archived** upstream (active dev moved on), so it's not in the live dataset. Still the canonical reference for lending/health-factor logic.

## Where to start (a learning path)

If you're ramping on EVM/DeFi development, in order:

1. **Language** → `solidity` (read the docs, write a token).
2. **Toolchain** → `foundry` (Forge for build/test/fuzz; Anvil for a local node).
3. **Stand on giants** → `openzeppelin-contracts` (inherit audited standards).
4. **Make it safe** → `slither` + `echidna` (static analysis + fuzzing) before you ship.
5. **Build the app** → `viem` + `wagmi` (+ `rainbowkit` for wallet UX).
6. **Read real DeFi** → `Uniswap/v4-core`, `compound/comet` to see production patterns.
7. **Get the data** → `graph-node` (subgraphs) + `blockscout` (explorer/MCP) to analyze positions.
8. **The frontier** → `coinbase/x402` + `ClawRouter` if you're wiring agents to move value.

> For **analyzing DeFi positions specifically**, the practical stack is `openclaw + blockscout (MCP reads) + OpenBB (valuation)` — see the **Blockchain Claws** report. For **what's still missing**, see **Recommended to Star — Blockchain / DeFi Gaps**.

## Caveats

- **Snapshot-bound** to the dataset; crypto moves weekly. Metrics (stars, lifecycle, health, momentum) are precomputed by the analyzer pipeline.
- **Curation is editorial** — the layer map is hand-built; inclusion means 'worth knowing', not 'exhaustive'. Repo names reflect post-redirect owners (e.g. `argotorg/solidity`, `otter-sec/anchor`, `safe-fndn/...`).
- **Stars ≠ endorsement to run in production**, especially anything touching funds — audit first.

<sub>Essential repos mapped: 37 across 13 layers · Snapshot: 2026-09-14T11:08:08.535Z · regenerate via scripts/reports/blockchain_essentials.py</sub>

# Recommended to Star — Blockchain / DeFi Gaps

> **Status (live-checked via `gh api` against `kaiser-data` on 2026-06-03):** of 31 canonical
> blockchain/DeFi developer repos checked, **0 are starred**. Your on-chain coverage today is the
> *agent/data* layer only (`blockscout`, `OpenBB`, `TradingAgents`, `ClawRouter`, `x402scan`) —
> you hold **none of the core EVM/Solana developer toolchain**. For a DeFi-focused stack
> (silverblock.finance) that's the biggest single gap in the collection.
>
> ⚠️ This list leans on external knowledge (training cutoff early 2026), unlike the
> dataset-derived in-app reports. Absence is live-verified; "leader" claims are editorial.

## 🔴 Tier 1 — can't do serious EVM/DeFi work without these

- [ ] [foundry-rs/foundry](https://github.com/foundry-rs/foundry) — **Dev toolkit** — Forge/Cast/Anvil; the dominant Solidity build/test/fuzz toolchain (Rust).
- [ ] [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) — **Contract library** — the standard audited ERC-20/721/1155, access control, proxies.
- [ ] [wevm/viem](https://github.com/wevm/viem) — **TS library** — modern, type-safe Ethereum client; the default for new TS/web3 apps.
- [ ] [ethers-io/ethers.js](https://github.com/ethers-io/ethers.js) — **TS library** — the long-time standard JS/TS Ethereum library.
- [ ] [ethereum/solidity](https://github.com/ethereum/solidity) — **Compiler** — the Solidity language & compiler itself.
- [ ] [crytic/slither](https://github.com/crytic/slither) — **Security** — the go-to static analyzer for smart-contract vulnerabilities.
- [ ] [ethereum/go-ethereum](https://github.com/ethereum/go-ethereum) — **Execution client** — geth; reference Ethereum node.

```
foundry-rs/foundry
OpenZeppelin/openzeppelin-contracts
wevm/viem
ethers-io/ethers.js
ethereum/solidity
crytic/slither
ethereum/go-ethereum
```

## 🟠 Tier 2 — DeFi protocol references, data & infra (high value for analysis)

- [ ] [graphprotocol/graph-node](https://github.com/graphprotocol/graph-node) — **Indexing** — The Graph; index on-chain data into queryable subgraphs (core for position analysis).
- [ ] [Uniswap/v4-core](https://github.com/Uniswap/v4-core) — **DeFi reference** — the canonical AMM/DEX contracts (v3-core also worth it).
- [ ] [aave/aave-v3-core](https://github.com/aave/aave-v3-core) — **DeFi reference** — leading lending protocol; essential for position/health-factor logic.
- [ ] [smartcontractkit/chainlink](https://github.com/smartcontractkit/chainlink) — **Oracles** — price feeds you'll need to value positions.
- [ ] [eth-infinitism/account-abstraction](https://github.com/eth-infinitism/account-abstraction) — **AA / ERC-4337** — reference account-abstraction contracts.
- [ ] [safe-global/safe-smart-account](https://github.com/safe-global/safe-smart-account) — **Wallets** — Safe (multisig) contracts; treasury/custody standard.
- [ ] [wevm/wagmi](https://github.com/wevm/wagmi) — **Frontend** — React hooks for Ethereum (pairs with viem).
- [ ] [Vectorized/solady](https://github.com/Vectorized/solady) — **Contracts** — gas-optimized Solidity building blocks.

## 🟡 Tier 3 — Solana, ZK & specialized (star if in scope)

- [ ] [coral-xyz/anchor](https://github.com/coral-xyz/anchor) — **Solana** — the standard Solana smart-contract framework.
- [ ] [anza-xyz/agave](https://github.com/anza-xyz/agave) — **Solana** — the Solana validator client (ex solana-labs/solana).
- [ ] [solana-labs/solana-web3.js](https://github.com/solana-labs/solana-web3.js) — **Solana** — JS SDK for Solana.
- [ ] [succinctlabs/sp1](https://github.com/succinctlabs/sp1) — **ZK** — performant zkVM (RISC-V); forward-looking for proofs.
- [ ] [risc0/risc0](https://github.com/risc0/risc0) — **ZK** — general-purpose zkVM.
- [ ] [iden3/circom](https://github.com/iden3/circom) — **ZK** — circuit compiler for zk-SNARKs.
- [ ] [paradigmxyz/reth](https://github.com/paradigmxyz/reth) — **Execution client** — modern Rust Ethereum client (fast-rising alt to geth).
- [ ] [NomicFoundation/hardhat](https://github.com/NomicFoundation/hardhat) — **Dev toolkit** — JS/TS dev env (alternative/complement to Foundry).

## Coverage snapshot

| Category | In your stars | Missing (this list) |
|---|---|---|
| Agent / data tooling | ✅ blockscout, OpenBB, TradingAgents, ClawRouter, x402scan | — |
| Smart-contract dev toolkits | ✗ | foundry, hardhat, solidity, vyper |
| Contract libraries / standards | ✗ | openzeppelin-contracts, solady, solmate, safe |
| Security / analysis | ✗ | slither, echidna |
| TS/JS libraries & wallet UX | ✗ | viem, wagmi, ethers.js, web3.js, rainbowkit |
| Execution clients | ✗ | go-ethereum, reth, nethermind |
| Oracles / AA / infra | ✗ | chainlink, account-abstraction |
| Indexing / data | ✗ | graph-node, subquery |
| Solana | ✗ | anchor, agave, solana-web3.js |
| DeFi protocol reference | ✗ | uniswap-v4, aave-v3, compound |
| ZK / privacy | ✗ | sp1, risc0, circom |

**Bottom line:** you've covered *AI agents for crypto* well, but not the *crypto* they'd operate on.
Starring Tier 1 (7 repos) closes the most critical gap; Tier 2 adds the DeFi-analysis substrate
(The Graph, Aave, Uniswap, Chainlink) that pairs directly with the `openclaw + blockscout + OpenBB`
stack from the blockchain-claws report.

<sub>Live-checked 2026-06-03 via `gh api user/starred/<repo>`. Re-run to refresh; star, then
`npm run refresh` to pull these into the in-app dataset & reports.</sub>

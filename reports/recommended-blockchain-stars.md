# Recommended to Star — Blockchain / DeFi Gaps

> **✅ RESOLVED (2026-06-03):** all **31** repos below were starred on `kaiser-data` via
> `gh api -X PUT` (31 ok / 0 failed) and verified. The original gap — *agent/data layer present,
> core EVM/Solana dev toolchain absent* — is now closed. Run `npm run refresh` to pull these into
> the in-app dataset & reports, which will populate new dataset-derived blockchain coverage.
>
> _History: when first checked, 0/31 were starred. The list is kept below as the record of what
> was added, tiered by priority._
>
> ⚠️ This list leans on external knowledge (training cutoff early 2026), unlike the
> dataset-derived in-app reports. "Leader" claims are editorial.

## 🔴 Tier 1 — can't do serious EVM/DeFi work without these

- [x] [foundry-rs/foundry](https://github.com/foundry-rs/foundry) — **Dev toolkit** — Forge/Cast/Anvil; the dominant Solidity build/test/fuzz toolchain (Rust).
- [x] [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) — **Contract library** — the standard audited ERC-20/721/1155, access control, proxies.
- [x] [wevm/viem](https://github.com/wevm/viem) — **TS library** — modern, type-safe Ethereum client; the default for new TS/web3 apps.
- [x] [ethers-io/ethers.js](https://github.com/ethers-io/ethers.js) — **TS library** — the long-time standard JS/TS Ethereum library.
- [x] [ethereum/solidity](https://github.com/ethereum/solidity) — **Compiler** — the Solidity language & compiler itself.
- [x] [crytic/slither](https://github.com/crytic/slither) — **Security** — the go-to static analyzer for smart-contract vulnerabilities.
- [x] [ethereum/go-ethereum](https://github.com/ethereum/go-ethereum) — **Execution client** — geth; reference Ethereum node.

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

- [x] [graphprotocol/graph-node](https://github.com/graphprotocol/graph-node) — **Indexing** — The Graph; index on-chain data into queryable subgraphs (core for position analysis).
- [x] [Uniswap/v4-core](https://github.com/Uniswap/v4-core) — **DeFi reference** — the canonical AMM/DEX contracts (v3-core also worth it).
- [x] [aave/aave-v3-core](https://github.com/aave/aave-v3-core) — **DeFi reference** — leading lending protocol; essential for position/health-factor logic.
- [x] [smartcontractkit/chainlink](https://github.com/smartcontractkit/chainlink) — **Oracles** — price feeds you'll need to value positions.
- [x] [eth-infinitism/account-abstraction](https://github.com/eth-infinitism/account-abstraction) — **AA / ERC-4337** — reference account-abstraction contracts.
- [x] [safe-global/safe-smart-account](https://github.com/safe-global/safe-smart-account) — **Wallets** — Safe (multisig) contracts; treasury/custody standard.
- [x] [wevm/wagmi](https://github.com/wevm/wagmi) — **Frontend** — React hooks for Ethereum (pairs with viem).
- [x] [Vectorized/solady](https://github.com/Vectorized/solady) — **Contracts** — gas-optimized Solidity building blocks.

## 🟡 Tier 3 — Solana, ZK & specialized (star if in scope)

- [x] [coral-xyz/anchor](https://github.com/coral-xyz/anchor) — **Solana** — the standard Solana smart-contract framework.
- [x] [anza-xyz/agave](https://github.com/anza-xyz/agave) — **Solana** — the Solana validator client (ex solana-labs/solana).
- [x] [solana-labs/solana-web3.js](https://github.com/solana-labs/solana-web3.js) — **Solana** — JS SDK for Solana.
- [x] [succinctlabs/sp1](https://github.com/succinctlabs/sp1) — **ZK** — performant zkVM (RISC-V); forward-looking for proofs.
- [x] [risc0/risc0](https://github.com/risc0/risc0) — **ZK** — general-purpose zkVM.
- [x] [iden3/circom](https://github.com/iden3/circom) — **ZK** — circuit compiler for zk-SNARKs.
- [x] [paradigmxyz/reth](https://github.com/paradigmxyz/reth) — **Execution client** — modern Rust Ethereum client (fast-rising alt to geth).
- [x] [NomicFoundation/hardhat](https://github.com/NomicFoundation/hardhat) — **Dev toolkit** — JS/TS dev env (alternative/complement to Foundry).

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

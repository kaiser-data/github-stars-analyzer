# Terminals for Agentic Programming — Which Terminal App, on Which OS, for How Many Sessions?

> Derived from **kaiser-data**'s 2,408 starred repos (snapshot `2026-10-24T18:18:45.023Z`), cross-referenced with the repo-similarity graph (2,408 nodes / 7,966 edges, 39 communities). The OS matrix, gap table, and scorecard are backed by external evidence gathered 2026-08-23 (GitHub API + 2026 head-to-head comparisons) — see Methodology.
>
> Generated 2026-10-24 by `scripts/reports/agentic_terminals.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agentic-terminals-top-tools.svg)

![Tools per category](assets/agentic-terminals-categories.svg)


## Executive summary

- **Two questions decide this, in order: which OS, and how many concurrent sessions.** Feature comparisons come third, and render benchmarks barely matter at all. The best tool for the job on macOS does not exist on Windows.
- **Best terminal for agentic coding, by OS:** macOS → **`cmux`** past one agent, **Ghostty** for a single session. Linux → **Ghostty** or **Kitty** as the emulator with **tmux** underneath and **`herdr`** or **`claude-squad`** for agent state. Windows → **Windows Terminal + WSL**, or **WezTerm** if you want one emulator everywhere. Remote → **tmux**, always.
- **The break point is roughly four agents.** Below it, any terminal works and panes are fine. Above it, undifferentiated panes actively hurt — you scroll to find the one that crashed — and you need per-session identity (branch, worktree, status) plus notifications that come to you.
- **One worktree per agent is the step people skip and regret.** Several agents in panes against a single working directory conflict or overwrite each other's edits. Claude Code ships `-w` / `--worktree` and `--tmux` to do exactly this — verified against the installed binary, not a blog post.
- **The agent already integrates with one terminal by name.** `claude --worktree --tmux` "uses iTerm2 native panes when available; use `--tmux=classic` for traditional tmux". On macOS that makes `iTerm2` — already in your stars — the zero-install multi-session answer, and it is a first-party signal worth more than any render benchmark in this report.
- **The structural gap this report was written about is now closed.** The terminal layer is **53 repos (1,447,281★)** against **7 relevant apps (34,747★) still missing** — where earlier editions of this report catalogued 45 absent terminal apps against 14 held. Coding *agents* were always covered exhaustively (31 tools, 1.2M★ in `ai-coding-tuis`); the terminal they live in has caught up.
- **Agent-aware terminals are represented now** (3): the category 2026 actually produced — terminals that know an agent is running and surface its state — is `warp` (65,673★), `cmux` (28,384★), `waveterm` (22,582★). This was the report's headline gap and is the one to re-check first if the gap table ever looks stale again.
- **What you do have** breaks down as:
  - **Agent-aware terminal** (3): `warp`, `cmux`, `waveterm`
  - **Emulator** (11): `terminal`, `tabby`, `alacritty`, `ghostty`, `kitty`, `wezterm`, `iTerm2`, `rio`, `tilix`, `contour`, `ghostling`
  - **Multiplexer / session** (7): `tmux`, `herdr`, `zellij`, `.tmux`, `tpm`, `sesh`, `libtmux`
  - **Parallel-agent orchestration** (6): `agent-orchestrator`, `claude-squad`, `emdash`, `omnara`, `dekit`, `nimbalyst`
  - **Remote & web sessions** (8): `xterm.js`, `mosh`, `ttyd`, `blink`, `tmate`, `wetty`, `EternalTerminal`, `gotty`
  - **Windows & shells** (2): `WSL`, `cmder`
  - **Shell & history** (10): `ohmyzsh`, `fzf`, `starship`, `nushell`, `zoxide`, `fish-shell`, `atuin`, `witr`, `x-cmd`, `dotfiles`
  - **Terminal hardening** (2): `container-use`, `tirith`
  - **Terminal capability / reference** (4): `iTerm2-Color-Schemes`, `awesome-tuis`, `chafa`, `lsix`
- **Nothing in your stars covers this layer editorially.** `tmux`, `iTerm2`, `herdr`, `chafa`, `x-cmd`, `witr`, and `awesome-tuis` appear in **no other report** in this suite — `herdr` alone is 25,579★ and Hot.

## Choosing by operating system

Platform availability eliminates more candidates than any feature does. The agent-aware terminals — the ones actually built for this — are macOS-first, and two of the three best emulators have no Windows build at all.

| OS | Emulator | Session layer | Multi-agent layer | The constraint |
|---|---|---|---|---|
| **macOS** | cmux (agent-aware) or Ghostty (fastest) | tmux, or cmux's own tabs — or iTerm2 native panes via `claude -w --tmux` | cmux, herdr, claude-squad | The richest options by a wide margin — and the only place cmux runs. Also the only place Claude Code's own `--tmux` gets native panes, since that path is iTerm2-specific. |
| **Linux** | Ghostty (GTK4/libadwaita) or Kitty | tmux or Zellij | herdr, claude-squad, agent-orchestrator | No cmux. Ghostty is native and excellent, but you build the agent-awareness layer yourself out of tmux + an orchestrator. |
| **Windows** | WezTerm, or Windows Terminal + WSL | tmux inside WSL | Warp (beta), waveterm, dekit | The weakest story. Ghostty, Kitty, and cmux have no Windows build at all. WSL is not a nicety here — most agent tooling assumes POSIX. |
| **Remote / headless box** | irrelevant — the emulator is local | tmux (+ mosh or Eternal Terminal) | herdr, claude-squad over SSH | The emulator stops mattering; persistence and reconnection are everything. This is where tmux's 2007 design is still unbeaten. |
| **Phone / away from desk** | Blink (iOS) attaching to tmux, or ttyd in a browser | tmux on the host | nimbalyst (iPhone app), omnara | Supervision, not authoring: you want to see which agent is blocked and approve or kill it in ten seconds. |

**Platform reality, stated plainly:**

- **`cmux` is macOS-only** — the single best tool for multi-agent supervision is unavailable to Linux and Windows users, with no announced plans otherwise.
- **Ghostty runs on macOS and Linux, not Windows.** Windows is planned post-1.0 with no timeline; WSL2 works but is explicitly unsupported by the maintainer. A community fork (`Codavo/ghostinthewsl`, 56★) exists precisely because of this.
- **Kitty has no Windows build.** WSL only.
- **WezTerm is the only first-tier emulator equally at home on all three** — which is why it's the right default for a mixed-OS team even though its renderer is the slowest of the GPU-accelerated set.
- **On Windows, WSL is the platform, not an accessory.** Agent tooling overwhelmingly assumes POSIX; `microsoft/WSL` (33,494★) belongs in your stars before any emulator does.
- **On a remote box the emulator stops mattering entirely.** Only persistence and reconnection do — tmux plus `mosh` or Eternal Terminal.

## Running multiple sessions — where each approach breaks

Agent count is the variable that changes the answer. Each row is where the previous setup stops working.

| Concurrent agents | What breaks | What to run |
|---|---|---|
| **1 agent** | Nothing. Any terminal works. | Ghostty (or whatever you already use). Don't over-engineer this. |
| **2–3 agents** | You start losing track of which pane finished. | `claude -w --tmux` — one worktree per session, in iTerm2 native panes on macOS or classic tmux elsewhere. Add `starship` so each pane shows its branch. |
| **4–6 agents** | Panes stop being self-describing; you scroll to find the crashed one. File collisions appear if they share a working directory. | One git worktree per agent — `claude --worktree` — plus one tmux session per worktree, managed with `sesh`. This is the step most people skip and regret. |
| **7–12 agents** | Human polling fails entirely. You need to be *told*, not to look. | An agent-aware surface: `cmux` notification rings (macOS), `herdr`, or `claude-squad`. Push notifications via `omnara`/`nimbalyst` if you leave the desk. |
| **12+ agents** | Supervision itself is the bottleneck; review capacity, not compute, is the limit. | Queue-and-review rather than watch: agents open PRs, you review asynchronously. `agent-orchestrator` handles CI fixes and merge conflicts without you. |

### The isolation question comes before the terminal question

Before choosing where sessions *appear*, decide how they're *isolated*. Four levels, cheapest first:

1. **Shared working directory, separate panes** — fine for read-only or genuinely unrelated tasks, fragile otherwise. Two agents editing the same file conflict or silently overwrite. This is the default people fall into and the source of most "parallel agents don't work" complaints.
2. **One git worktree per agent** — each session gets its own filesystem scope and branch, at near-zero cost. `claude -w` / `--worktree` creates it, and `--tmux` puts each session in its own tmux environment (iTerm2 native panes where available). **This is the right default past two agents.**
3. **One container per agent** — `container-use` (in your stars, though declining) when agents install packages or run services that would collide on ports.
4. **One machine per agent** — remote boxes, supervised over tmux + mosh. Only when the work is genuinely heavy.

A caveat worth internalising: **parallel sessions pay off for independent tasks, not for splitting one task.** Fanning a single feature across agents creates merge conflicts and coordination overhead that erases the speedup.

### Session persistence is a separate problem from session isolation

Isolation stops agents corrupting each other. Persistence stops a closed lid or a dropped connection killing an hour of work. They need different tools:

- **Detach/reattach**: tmux (or Zellij). Non-negotiable for anything long-running.
- **Network roaming**: `mosh` (UDP, survives IP changes and sleep, but has no scrollback of its own) or `EternalTerminal` (reconnecting, keeps scrollback).
- **Across a reboot**: within tmux, `tmux-resurrect` is still the well-trodden path — and it hasn't been pushed since August 2024. `herdr` claims this natively (its README promises agents survive a machine restart), which if it holds is the strongest reason in this report to prefer it over a tmux + plugin stack. Zellij's native persistence remains roadmap.
- **Away from the desk**: `nimbalyst` (agent kanban + iPhone app) or `omnara` for push notifications; `Blink` or `ttyd` if you'd rather attach to the real session.

## Master comparison — the terminal layer in your stars

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Layer | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | Shell & history | Shell | MIT | 190,144 (▲73) | Classic | 85 | very active | 0d ago | 17.2y | 55 |
| [microsoft/terminal](https://github.com/microsoft/terminal) | Emulator | C++ | MIT | 105,220 (▲35) | Classic | 82 | very active | 1d ago | 9.2y | 32 |
| [junegunn/fzf](https://github.com/junegunn/fzf) | Shell & history | Go | MIT | 83,754 (▲91) | Classic | 76 | very active | 3d ago | 13.0y | 8 |
| [Eugeny/tabby](https://github.com/Eugeny/tabby) | Emulator | TypeScript | MIT | 75,102 (▲77) | Classic | 92 | very active | 6d ago | 9.8y | 35 |
| [alacritty/alacritty](https://github.com/alacritty/alacritty) | Emulator | Rust | Apache  2.0 | 66,033 (▲35) | Mature | 61 | active | 9d ago | 10.7y | 4 |
| [warpdotdev/warp](https://github.com/warpdotdev/warp) | Agent-aware terminal | Rust | GNU Affero General Public  v3.0 | 65,673 (▲148) | Classic | 76 | very active | 1d ago | 5.3y | 17 |
| [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | Emulator | Zig | MIT | 62,566 (▲195) | Classic | 69 | very active | 1d ago | 4.6y | 8 |
| [starship/starship](https://github.com/starship/starship) | Shell & history | Rust | ISC | 60,431 (▲93) | Classic | 75 | very active | 1d ago | 7.6y | 25 |
| [tmux/tmux](https://github.com/tmux/tmux) | Multiplexer / session | C | ISC | 49,976 (▲50) | Classic | 80 | very active | 0d ago | 11.4y | 6 |
| [herdrdev/herdr](https://github.com/herdrdev/herdr) | Multiplexer / session | Rust | Apache  2.0 | 45,654 (▲916) | Hot | 83 | very active | 1d ago | 7mo | 9 |
| [nushell/nushell](https://github.com/nushell/nushell) | Shell & history | Rust | MIT | 40,720 (▲32) | Classic | 88 | very active | 0d ago | 7.5y | 33 |
| [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide) | Shell & history | Rust | MIT | 40,274 (▲81) | Classic | 66 | very active | 1d ago | 6.6y | 14 |
| [zellij-org/zellij](https://github.com/zellij-org/zellij) | Multiplexer / session | Rust | MIT | 35,821 (▲56) | Classic | 70 | very active | 1d ago | 6.1y | 31 |
| [kovidgoyal/kitty](https://github.com/kovidgoyal/kitty) | Emulator | Python | GNU General Public  v3.0 | 35,413 (▲57) | Classic | 80 | very active | 1d ago | 10.0y | 9 |
| [fish-shell/fish-shell](https://github.com/fish-shell/fish-shell) | Shell & history | Rust | Other | 34,338 (▲16) | Classic | 84 | very active | 2d ago | 14.5y | 25 |
| [microsoft/WSL](https://github.com/microsoft/WSL) | Windows & shells | C++ | MIT | 34,193 (▲57) | Classic | 79 | very active | 0d ago | 10.6y | 15 |
| [atuinsh/atuin](https://github.com/atuinsh/atuin) | Shell & history | Rust | MIT | 32,061 (▲33) | Classic | 83 | very active | 1d ago | 6.1y | 16 |
| [wezterm/wezterm](https://github.com/wezterm/wezterm) | Emulator | Rust | Other | 29,333 (▲57) | Classic | 64 | very active | 6d ago | 8.7y | 29 |
| [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | Agent-aware terminal | Swift | Other | 28,384 (▲120) | Hot | 77 | very active | 0d ago | 8mo | 7 |
| [mbadolato/iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) | Terminal capability / reference | Shell | Other | 27,283 (▲10) | Classic | 80 | very active | 1d ago | 15.6y | 9 |
| [cmderdev/cmder](https://github.com/cmderdev/cmder) | Windows & shells | PowerShell | MIT | 27,007 (▲2) | Mature | 48 | active | 1d ago | 13.3y | 2 |
| [gpakosz/.tmux](https://github.com/gpakosz/.tmux) | Multiplexer / session | Shell | MIT | 25,444 (▲4) | Classic | 64 | very active | 3d ago | 14.2y | 4 |
| [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | Shell & history | Go | Apache  2.0 | 22,782 (▲64) | Hot | 76 | very active | 2d ago | 10mo | 11 |
| [wavetermdev/waveterm](https://github.com/wavetermdev/waveterm) | Agent-aware terminal | Go | Apache  2.0 | 22,582 (▲48) | Classic | 68 | very active | 7d ago | 4.4y | 6 |
| [xtermjs/xterm.js](https://github.com/xtermjs/xterm.js) | Remote & web sessions | TypeScript | MIT | 21,292 (▲13) | Classic | 68 | very active | 11d ago | 12.6y | 15 |
| [rothgar/awesome-tuis](https://github.com/rothgar/awesome-tuis) | Terminal capability / reference | — | — | 20,981 (▲47) | Classic | 75 | very active | 13d ago | 7.6y | 53 |
| [gnachman/iTerm2](https://github.com/gnachman/iTerm2) | Emulator | Swift | GNU General Public  v2.0 | 18,214 (▲22) | Classic | 60 | very active | 0d ago | 15.6y | 3 |
| [tmux-plugins/tpm](https://github.com/tmux-plugins/tpm) | Multiplexer / session | Shell | MIT | 15,143 (▲2) | Mature | 22 | slowing | 5mo ago | 12.4y | 0 |
| [mobile-shell/mosh](https://github.com/mobile-shell/mosh) | Remote & web sessions | C++ | GNU General Public  v3.0 | 14,587 (▲10) | Declining | 20 | stale | 7mo ago | 15.8y | 0 |
| [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Parallel-agent orchestration | Go | Apache  2.0 | 13,571 (▲225) | Hot | 88 | very active | 0d ago | 8mo | 17 |
| [tsl0922/ttyd](https://github.com/tsl0922/ttyd) | Remote & web sessions | C | MIT | 12,541 (▲21) | Mature | 40 | slowing | 2mo ago | 10.1y | 2 |
| [smtg-ai/claude-squad](https://github.com/smtg-ai/claude-squad) | Parallel-agent orchestration | Go | GNU Affero General Public  v3.0 | 8,661 (▲38) | Declining | 59 | slowing | 2mo ago | 1.6y | 3 |
| [raphamorim/rio](https://github.com/raphamorim/rio) | Emulator | Rust | MIT | 7,641 (▲18) | Classic | 78 | very active | 0d ago | 4.1y | 4 |
| [blinksh/blink](https://github.com/blinksh/blink) | Remote & web sessions | Swift | GNU General Public  v3.0 | 6,989 (▲8) | Mature | 28 | slowing | 3mo ago | 10.6y | 0 |
| [tmate-io/tmate](https://github.com/tmate-io/tmate) | Remote & web sessions | C | Other | 6,135 (▼1) | Mature | 42 | active | 18d ago | 13.4y | 2 |
| [generalaction/emdash](https://github.com/generalaction/emdash) | Parallel-agent orchestration | TypeScript | Apache  2.0 | 6,070 (▲42) | Hot | 79 | very active | 1d ago | 1.2y | 10 |
| [gnunn1/tilix](https://github.com/gnunn1/tilix) | Emulator | D | Mozilla Public  2.0 | 5,739 (▲6) | Mature | 28 | slowing | 3mo ago | 10.8y | 0 |
| [butlerx/wetty](https://github.com/butlerx/wetty) | Remote & web sessions | TypeScript | MIT | 5,473 (▲4) | Classic | 76 | very active | 0d ago | 12.6y | 8 |
| [hpjansson/chafa](https://github.com/hpjansson/chafa) | Terminal capability / reference | C | GNU Lesser General Public  v3.0 | 5,349 (▲16) | Mature | 70 | very active | 5d ago | 8.5y | 1 |
| [x-cmd/x-cmd](https://github.com/x-cmd/x-cmd) | Shell & history | Awk | Apache  2.0 | 4,722 (▲6) | Classic | 72 | very active | 0d ago | 4.1y | 4 |
| [hackerb9/lsix](https://github.com/hackerb9/lsix) | Terminal capability / reference | Shell | GNU General Public  v3.0 | 4,176 | Abandoned | 5 | stale | 2.3y ago | 9.4y | 0 |
| [dagger/container-use](https://github.com/dagger/container-use) | Terminal hardening | Go | Apache  2.0 | 4,079 (▲7) | Mature | 44 | active | 1mo ago | 1.4y | 2 |
| [MisterTea/EternalTerminal](https://github.com/MisterTea/EternalTerminal) | Remote & web sessions | C++ | Apache  2.0 | 3,926 (▲6) | Classic | 65 | very active | 5d ago | 9.9y | 10 |
| [omnara-ai/omnara](https://github.com/omnara-ai/omnara) | Parallel-agent orchestration | Go | Apache  2.0 | 3,222 (▲283) | Hot | 84 | very active | 0d ago | 1.3y | 9 |
| [contour-terminal/contour](https://github.com/contour-terminal/contour) | Emulator | C++ | Apache  2.0 | 3,050 (▲5) | Classic | 71 | very active | 0d ago | 7.2y | 3 |
| [joshmedeski/sesh](https://github.com/joshmedeski/sesh) | Multiplexer / session | Go | MIT | 2,900 (▲24) | Mature | 74 | very active | 2d ago | 2.8y | 12 |
| [pvolok/dekit](https://github.com/pvolok/dekit) | Parallel-agent orchestration | Rust | MIT | 2,768 (▲8) | Classic | 73 | very active | 2d ago | 5.2y | 3 |
| [sheeki03/tirith](https://github.com/sheeki03/tirith) | Terminal hardening | Rust | GNU Affero General Public  v3.0 | 2,765 (▲8) | Rising | 79 | very active | 1d ago | 8mo | 2 |
| [sorenisanerd/gotty](https://github.com/sorenisanerd/gotty) | Remote & web sessions | Go | MIT | 2,562 (▲2) | Classic | 73 | very active | 0d ago | 5.5y | 4 |
| [nimbalyst/nimbalyst](https://github.com/nimbalyst/nimbalyst) | Parallel-agent orchestration | TypeScript | MIT | 1,970 (▲38) | Hot | 75 | very active | 1d ago | 11mo | 4 |
| [tmux-python/libtmux](https://github.com/tmux-python/libtmux) | Multiplexer / session | Python | MIT | 1,216 | Mature | 72 | very active | 0d ago | 10.4y | 1 |
| [ghostty-org/ghostling](https://github.com/ghostty-org/ghostling) | Emulator | C | MIT | 1,127 (▲2) | Declining | 37 | slowing | 2mo ago | 7mo | 2 |
| [caarlos0/dotfiles](https://github.com/caarlos0/dotfiles) | Shell & history | Shell | MIT | 224 (▲2) | Mature | 80 | very active | 4d ago | 3.6y | 1 |

**Agent-aware terminal**

- **warpdotdev/warp** (65,673★) — Markets itself as an 'agentic development environment': per-tab git/PR metadata, reusable `.toml` tab configs, unified agent notifications. Proprietary rendering engine, opinionated conventions, reported CJK IME issues.
- **manaflow-ai/cmux** (28,384★) — Purpose-built for running several coding agents in parallel: Ghostty rendering engine, vertical tabs with per-tab git branch / worktree / PR status, notification rings and unread badges per pane, session restore, embedded browser, and a Unix-socket API agents can call to drive the UI. Codex CLI's sandbox can block the socket.
- **wavetermdev/waveterm** (22,582★) — Open-source, cross-platform, AI-integrated terminal with graphical blocks — the non-proprietary answer to Warp, and the only genuinely tri-platform option in this layer.

**Emulator**

- **microsoft/terminal** (105,220★) — The default answer on Windows, where Ghostty and cmux simply don't run. Pairs with WSL for a POSIX agent environment.
- **Eugeny/tabby** (75,102★) — Cross-platform with first-class SSH/serial profile management — useful when agents live on several remote boxes and you want saved profiles per host.
- **alacritty/alacritty** (66,033★) — Long cited at ~30 MB resident against 60–100 MB for Kitty/Ghostty — the pick when the agent fleet, not the terminal, should own the RAM. That gap has closed: Ghostty 1.3.1 measures 23 MB settled on an M2 (see Methodology), so the memory argument for Alacritty no longer holds. No tabs or splits by design — which stops being a loss when paired with `herdr` or tmux, since those supply the tabs. Homebrew's cask was disabled 2026-09-01 for failing the macOS Gatekeeper check, so this is not currently installable that way.
- **ghostty-org/ghostty** (62,566★) — Fastest sustained-output rendering on macOS in published 2026 comparisons; native Shift+Enter; `macos-option-as-alt = true` needed for Alt+, / Alt+. reasoning controls. Measured here at 23 MB resident / 33 MB phys_footprint settled and idle on an M2 running 1.3.1 — roughly 3× lighter than the 60–100 MB figure earlier editions of this report carried, and lighter than Alacritty's cited ~30 MB. On Linux it's GTK4 + optional libadwaita. Windows is planned post-1.0 with no timeline; WSL2 works but is explicitly unsupported.
- **kovidgoyal/kitty** (35,413★) — The Kitty graphics protocol is the de-facto standard for inline images from agent output; built-in multiplexing; deep keyboard control. No Windows build.
- **wezterm/wezterm** (29,333★) — Broadest graphics-protocol support (Kitty + sixel + iTerm2), built-in multiplexer with its own persistence, Lua config. The only first-tier emulator that is genuinely equal on all three desktop OSes. Rendering trails Ghostty.
- **gnachman/iTerm2** (18,214★) — The long-standing macOS emulator — and the one Claude Code integrates with by name: `claude --worktree --tmux` uses iTerm2 native panes when available. Objective-C, single-maintainer, macOS only.
- **raphamorim/rio** (7,641★) — Newer GPU emulator that also targets the browser — interesting for agent sessions surfaced over the web.
- **gnunn1/tilix** (5,739★) — GTK3 tiling emulator with saved session layouts — the Linux-native way to get a fixed multi-agent pane grid without a multiplexer.
- **contour-terminal/contour** (3,050★) — Standards-focused emulator; a reference implementation for VT and sixel behaviour.
- **ghostty-org/ghostling** (1,127★) — A minimum-viable emulator demonstrating the libghostty C API — a reference consumer of Ghostty's embeddable core, not the core and not Ghostty itself.

**Multiplexer / session**

- **tmux/tmux** (49,976★) — The 2007 multiplexer that became agent infrastructure — process isolation, detach/reattach, and a stable `send-keys` API orchestrators target. Runs anywhere POSIX.
- **herdrdev/herdr** (45,654★) — A background server the terminals live inside: agents survive a closed lid, a dropped network, and a reboot, and reattach from any terminal or over SSH. Marks every pane working/blocked/idle, and its socket API is the same surface agents drive. One Rust binary, macOS/Linux with Windows in beta.
- **zellij-org/zellij** (35,821★) — Better out-of-the-box UX than tmux (floating panes, visible keybindings) but no `send-keys`-equivalent with comparable API stability, and native session persistence is still roadmap — which is why orchestrators keep targeting tmux.
- **gpakosz/.tmux** (25,444★) — The widely-used opinionated tmux config — the fastest path from bare tmux to a usable multi-agent cockpit.
- **tmux-plugins/tpm** (15,143★) — tmux plugin manager — the prerequisite for everything below.
- **joshmedeski/sesh** (2,900★) — Smart tmux session manager — one keystroke from repo to a named agent session, which is the actual bottleneck once you run one session per worktree.
- **tmux-python/libtmux** (1,216★) — Typed Python API over tmux — what you write against instead of shelling out to `send-keys` when you build your own agent supervisor.

**Parallel-agent orchestration**

- **OrchestratorInc/agent-orchestrator** (13,571★) — Agent IDE over tmux + git worktrees — plans tasks, spawns fleets, handles CI fixes and merge conflicts autonomously.
- **smtg-ai/claude-squad** (8,661★) — Manages multiple terminal agents (Claude Code, Codex, OpenCode, Amp) in isolated worktrees from one TUI — the cheapest way to get past four concurrent agents without adopting a new terminal.
- **generalaction/emdash** (6,070★) — Open-source agentic development environment (YC W26): runs many coding agents side by side, each in its own git worktree, with diff review and merge from one window.
- **omnara-ai/omnara** (3,222★) — Command-centre view over agents running elsewhere, including from a phone — the answer to 'which agent is stuck' when you're away from the machine.
- **pvolok/dekit** (2,768★) — Runs many commands in parallel with per-process panes — the generic, OS-portable version of agent multiplexing.
- **nimbalyst/nimbalyst** (1,970★) — Visual workspace for Claude Code/Codex/OpenCode: an agent kanban where each card is a task, branch, or running session showing active / blocked / awaiting-review / ready-to-merge — plus a native iPhone app for reviewing and resuming.

**Remote & web sessions**

- **xtermjs/xterm.js** (21,292★) — The terminal component inside browsers and Electron apps — what you'd build on to give an agent fleet a web UI.
- **mobile-shell/mosh** (14,587★) — UDP-based roaming shell that survives IP changes and sleep — the layer that stops a laptop lid closing from killing an SSH-attached agent run. Pair with tmux; mosh has no scrollback of its own.
- **tsl0922/ttyd** (12,541★) — Shares a terminal over the web — the simplest way to look in on a long agent run from a phone or another machine without an app.
- **blinksh/blink** (6,989★) — Mosh + SSH client for iOS with a real keyboard story — the way to attach to a tmux session full of agents from a phone or iPad.
- **tmate-io/tmate** (6,135★) — Instant shared tmux session over a relay — useful for pairing a colleague into a running agent session.
- **butlerx/wetty** (5,473★) — Terminal over HTTP/HTTPS with auth — the self-hosted variant of the same idea as ttyd.
- **MisterTea/EternalTerminal** (3,926★) — Reconnecting SSH replacement that keeps the session alive across network changes, with native scrollback (unlike mosh).
- **sorenisanerd/gotty** (2,562★) — The maintained fork of the original gotty — share a command's output as a web page.

**Windows & shells**

- **microsoft/WSL** (34,193★) — The thing that actually makes agentic coding viable on Windows — a real Linux userland for the agent's shell commands. Most agent tooling assumes POSIX.
- **cmderdev/cmder** (27,007★) — Portable console emulator bundle for Windows — the pre-WSL answer, still widely used.

**Shell & history**

- **ohmyzsh/ohmyzsh** (190,144★) — The default zsh framework; mostly ergonomics, some startup-time cost — which multiplies when you spawn a shell per agent pane.
- **junegunn/fzf** (83,754★) — Fuzzy selection is what makes 'jump to the right session/worktree/file' cheap for a human supervising agents.
- **starship/starship** (60,431★) — Cross-shell prompt; carries git/worktree/branch state that tells you which agent's pane you're looking at — genuinely useful at 6+ sessions.
- **nushell/nushell** (40,720★) — Structured-data shell — pipelines return tables, which is markedly easier for an agent to parse than ad-hoc text. Also one of the few shells equally native on Windows.
- **ajeetdsouza/zoxide** (40,274★) — Frecency-based `cd` — trivial, and saves real time across many worktrees.
- **fish-shell/fish-shell** (34,338★) — Best interactive defaults; non-POSIX, so agent-generated shell snippets can break.
- **atuinsh/atuin** (32,061★) — Searchable, synced shell history — the audit trail for what an agent actually ran, and the only practical way to reconstruct it across many machines and sessions.
- **pranshuparmar/witr** (22,782★) — 'Why is this running?' — traces any process, port, container, or file back to its origin; the triage tool for a pane you no longer recognise.
- **x-cmd/x-cmd** (4,722★) — 'Shell superpowers for AI agents' — POSIX-portable command toolkit agents can call without installing a language runtime.
- **caarlos0/dotfiles** (224★) — A maintained real-world `$HOME/.config` (fish + tmux + nix) — the reference for making a terminal reproducible across machines.

**Terminal hardening**

- **dagger/container-use** (4,079★) — Containerized dev environments so parallel agents can't collide — the isolation half of running fleets safely.
- **sheeki03/tirith** (2,765★) — Terminal security for devs and agents — intercepts homograph URLs, pipe-to-shell, ANSI injection, and exfiltration before execution.

**Terminal capability / reference**

- **mbadolato/iTerm2-Color-Schemes** (27,283★) — 450+ schemes ported across iTerm2, Kitty, Alacritty, Ghostty, Windows Terminal — the de-facto emulator compatibility matrix.
- **rothgar/awesome-tuis** (20,981★) — The canonical index of terminal user interfaces — the discovery surface for the layer this report says you're under-invested in.
- **hpjansson/chafa** (5,349★) — Terminal graphics for any emulator (sixel, Kitty, iTerm2 protocols) — how agent-generated images render where no native protocol exists.
- **hackerb9/lsix** (4,176★) — `ls` for images via sixel — the minimal proof that inline graphics work in your stack.

## The gap — terminal apps missing from your stars

7 repos, **34,747★** combined. Metrics verified against the GitHub API on **2026-08-23** and frozen into the generator — they are *not* dataset metrics and do **not** refresh when the pipeline re-runs. The **OS** column is the first filter to apply.

### Emulator — 2 missing, 748★

| Repo | ★ | OS | Lang | License | Freshness | Why it matters for agents | Verdict |
|---|---|---|---|---|---|---|---|
| [KDE/konsole](https://github.com/KDE/konsole) | 692 | Linux | C++ | NOASSERTION | pushed 2d (GitHub mirror; dev on KDE Invent) | The KDE default — split views and profiles, deeply integrated on Plasma. Low GitHub star count reflects the mirror, not adoption. | Reference only — you get it with the desktop. |
| [Codavo/ghostinthewsl](https://github.com/Codavo/ghostinthewsl) | 56 | Windows (WSL2) | Zig | MIT | pushed 2026-08-02 | A Ghostty fork that bypasses Windows terminal infrastructure and talks directly to the WSL2 VM, keeping Kitty graphics. Tiny project; the honest read is that it exists because Ghostty has no Windows support. | Reference only — evidence of the gap, not a dependency. |

### Multiplexer / session — 1 missing, 13,014★

| Repo | ★ | OS | Lang | License | Freshness | Why it matters for agents | Verdict |
|---|---|---|---|---|---|---|---|
| [tmux-plugins/tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) | 13,014 | any POSIX | Shell | MIT | ⚠ pushed 2024-08-13 — ~2y stale | Still the standard way to survive a reboot with agent panes intact, but effectively unmaintained. Neither tmux nor Zellij persists across reboots by default. | Star with eyes open; the staleness is a real risk. |

### Parallel-agent orchestration — 1 missing, 3,106★

| Repo | ★ | OS | Lang | License | Freshness | Why it matters for agents | Verdict |
|---|---|---|---|---|---|---|---|
| [stravu/crystal](https://github.com/stravu/crystal) | 3,106 | desktop | TypeScript | MIT | ⚠ pushed 2026-02-26, renamed to Nimbalyst | Parallel Codex/Claude Code sessions in git worktrees as a desktop app — but the repo has been idle ~6 months and the project moved. | **Skip** — star `nimbalyst/nimbalyst` instead. |

### Remote & web sessions — 2 missing, 8,632★

| Repo | ★ | OS | Lang | License | Freshness | Why it matters for agents | Verdict |
|---|---|---|---|---|---|---|---|
| [ekzhang/sshx](https://github.com/ekzhang/sshx) | 7,649 | any (serves to browser) | Rust | MIT | ⚠ pushed 2025-06-19 — >1y stale | Collaborative web terminal with multiplayer cursors; elegant, but the repo has been quiet for over a year. | Watch only — the staleness matters for anything you expose to a network. |
| [martanne/abduco](https://github.com/martanne/abduco) | 983 | Linux, BSD | C | ISC | ⚠ pushed 2023-01-18 — 3y stale | Session detach/attach with no multiplexing — the minimal alternative when you want persistence without tmux's surface area. | Reference only. |

### Windows & shells — 1 missing, 9,247★

| Repo | ★ | OS | Lang | License | Freshness | Why it matters for agents | Verdict |
|---|---|---|---|---|---|---|---|
| [ConEmu/ConEmu](https://github.com/ConEmu/ConEmu) | 9,247 | Windows | C++ | BSD-3-Clause | ⚠ pushed 2025-04-07 — >1y stale | The console host cmder is built on; historically important, now slowing. | Skip — Windows Terminal is the maintained path. |

**Priority shortlist.** If you only add a handful, add these 0 — each closes a structural hole rather than adding another variant of something you already have:


**Named in the evidence but not starrable** (closed source, or the public repo is only an issue tracker) — worth knowing the category is bigger than the table:

- **Otty** — agent-aware terminal; only themes/plugins are on GitHub
- **Termdock** — AI-native terminal — public repo is an issue tracker only
- **amux** — agent multiplexer with a self-healing watchdog and push notifications
- **Paseo** — mobile-first agent supervision with worktrees and voice input

## What actually matters for agentic programming

Eight criteria, ordered by how often they bite. The last column is how to test a candidate in under a minute.

| Criterion | Why it matters with agents | How to test it |
|---|---|---|
| **Sustained-output throughput** | Agents emit thousands of lines per task; a slow renderer turns a refactor into visible stutter and makes the pane unreadable while it streams. | `yes \| head -5000000` and watch for tearing; time a large `git log -p`. |
| **Agent notifications** | The scarce resource with more than one agent is your attention. The terminal must tell you when an agent finished or is blocked on input. | Check for OSC 9 / OSC 99 / OSC 777 (bell + desktop notification) and OSC 133;C/D prompt marking. |
| **Parallel-session state at a glance** | Past ~4 agents, undifferentiated panes actively hurt — you scroll to find the crashed one. Per-pane branch/worktree/status metadata is the fix. | Open 6 agents; can you name which is waiting without reading scrollback? |
| **Session persistence** | Long-running agents must survive a dropped SSH connection, a closed lid, and ideally a reboot. | Detach, kill the client, reattach. Then reboot and try again. |
| **Key & escape-sequence fidelity** | Shift+Enter for newlines, Alt+, / Alt+. for reasoning controls, OSC 52 for clipboard, OSC 8 for clickable `file:line` — all agent-facing UX. | Type a multi-line prompt; click a `path.py:42` link; copy from a remote session. |
| **Graphics protocol** | Agents increasingly return plots, diagrams, and screenshots. Without a protocol you get a file path instead of an image. | `chafa image.png` vs native Kitty/sixel rendering. |
| **Scriptable control surface** | Every orchestrator on top of a terminal needs to inject keystrokes and read pane state programmatically. | Is there a stable `send-keys` equivalent or a socket/IPC API? |
| **OS coverage** | The best tool you cannot install is worth nothing. This eliminates more candidates than any feature comparison. | Does it run on every machine you and your team actually use? |

### Scorecard

Columns follow the criteria above in order — throughput · notifications · parallel state · persistence · key fidelity · graphics · scriptability — with OS coverage broken out as its own column since it's a hard filter, not a score. ● strong · ◐ partial · ○ absent.

| Tool | OS | Thr | Notif | State | Persist | Keys | Gfx | Script | Note |
|---|---|---|---|---|---|---|---|---|---|
| **cmux (Ghostty core)** | macOS | ● | ● | ● | ● | ● | ○ | ● | Only tool designed for the parallel-agent case; macOS-only, very young. |
| **Warp** | mac/Linux/Win beta | ● | ● | ● | ● | ◐ | ○ | ◐ | Strongest notifications after cmux; proprietary engine, opinionated. |
| **waveterm** | mac/Linux/Win | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | The only open, tri-platform agent-aware option — nothing best-in-class, nothing missing. |
| **Ghostty** | macOS, Linux | ● | ○ | ○ | ○ | ● | ○ | ○ | Best raw renderer, zero agent awareness — pair with tmux. No Windows. |
| **Kitty** | macOS, Linux | ● | ○ | ◐ | ○ | ● | ● | ● | Graphics protocol leader; remote-control socket, but no detach-to-daemon so nothing survives a dropped connection. No Windows. |
| **WezTerm** | mac/Linux/Win | ◐ | ○ | ◐ | ● | ● | ● | ● | Built-in multiplexer + persistence + widest graphics; slowest of the GPU set, and the only cross-OS emulator here. |
| **iTerm2** | macOS | ◐ | ◐ | ◐ | ○ | ● | ◐ | ◐ | Mature and scriptable, but the oldest engine in the set. |
| **Alacritty** | mac/Linux/Win | ● | ○ | ○ | ○ | ◐ | ○ | ○ | Deliberately minimal — no tabs, no splits, no notifications. |
| **Windows Terminal** | Windows | ◐ | ○ | ◐ | ○ | ◐ | ○ | ◐ | The only real choice on Windows; pair with WSL. |
| **tmux** | any POSIX | ◐ | ◐ | ○ | ● | ◐ | ○ | ● | Weak UI, unbeatable persistence and the reference automation API. |
| **Zellij** | mac/Linux | ◐ | ◐ | ◐ | ◐ | ◐ | ○ | ◐ | Nicer UX than tmux; persistence and scripting API both still weaker. |
| **herdr** | mac/Linux/Win beta | ● | ◐ | ● | ● | ● | ○ | ● | Agent-native multiplexer, terminal-agnostic single Rust binary. Marks panes working/blocked/idle and survives reboot natively; desktop-push notification unconfirmed. |

Read the scorecard as a shape, not a total. `Ghostty` and `tmux` are near-opposites and are routinely used *together* — which is the real recommendation for anyone who can't or won't adopt a macOS-only agent terminal.

## Best pick per scenario

| Scenario | 🥇 First pick | 🥈 Second | 🥉 Third | Evidence / note |
|---|---|---|---|---|
| One agent, one Mac, want the best default | **Ghostty** — fastest renderer, native Shift+Enter, one-line 25M scrollback | **cmux** — same engine plus agent notifications — worth it the moment you add a second agent | **iTerm2** — already in your stars; mature, slower engine | Ghostty benchmarked ~4× iTerm2/Kitty throughput on sustained output; ~2 ms vs 3 ms input latency vs Kitty. |
| One agent on Linux | **Ghostty** — GTK4 + libadwaita, native on GNOME and KDE | **Kitty** — graphics protocol and built-in multiplexing | **Tilix** — if you want saved tiling layouts without a multiplexer | Ghostty ships a first-class Linux build; cmux does not exist here, so the agent-awareness layer must come from tmux + an orchestrator. |
| Agentic coding on Windows | **Windows Terminal + WSL** — WSL is the platform — most agent tooling assumes POSIX | **WezTerm** — the one first-tier emulator equally at home on Windows | **Warp** — agent-aware, but Windows support is still beta | Ghostty has no Windows support (planned post-1.0, no timeline; WSL2 works but is explicitly unsupported). Kitty and cmux have no Windows build at all. |
| Four or more agents in parallel on one machine | **cmux** — notification rings, per-tab branch/PR/worktree metadata, unread badges — macOS only | **herdr** — agent-native multiplexer, already in your stars, not macOS-locked | **claude-squad** — TUI over isolated worktrees on tmux you already trust | Multiple 2026 comparisons converge: past four agents the binding constraint is knowing which one needs you, not render speed. |
| Keeping many sessions from corrupting each other | **git worktree per agent** — `claude -w` / `--worktree`, built into the CLI — verified against the installed binary | **claude --worktree --tmux** — each session in its own tmux environment — iTerm2 native panes when available, `--tmux=classic` otherwise | **container-use** — in your stars — full container isolation when worktrees aren't enough | Running several agents in panes against one working directory is fragile: two sessions editing the same file conflict or overwrite. Worktrees give each session its own filesystem scope at near-zero cost. |
| Agents on a remote box, or over flaky SSH | **tmux** — detach/reattach is non-negotiable and nothing beats it | **mosh or Eternal Terminal** — survives IP changes and sleep; mosh has no scrollback, ET does | **Zellij** — same job as tmux, friendlier UI, weaker scripting | Process isolation, session persistence, real-time output, and remote attach — tmux's 2007 feature set is exactly the agent-orchestration requirement list. |
| Surviving a reboot with agent state intact | **herdr** — a background server that claims native survival of lid-close, network drop and restart — no plugin needed | **tmux + tmux-resurrect** — the well-trodden path *within tmux*, but resurrect is ~2 years stale | **cmux** — session restore built in, macOS only | Neither tmux nor Zellij persists across reboots by default; Zellij's native persistence is still roadmap. herdr's reboot claim is from its own README and is not independently verified here. |
| Supervising agents from a phone | **nimbalyst** — agent kanban — active / blocked / awaiting review / ready to merge — with a native iPhone app | **omnara** — command centre over agents running elsewhere, push notifications | **Blink + tmux, or ttyd** — the DIY route: attach to the real session from iOS or a browser | The mobile pattern is tap-notification, review, approve or reject in ~10 seconds — not authoring on a phone. Agents in 2026 are autonomous enough to work alone but not to go unsupervised. |
| Building an orchestrator on top of a terminal | **tmux** — `send-keys` is the stable reference backend orchestrators target | **libtmux** — typed Python API so you're not string-building shell commands | **cmux socket API** — if macOS-only is acceptable | Zellij lacks a `send-keys` equivalent with comparable API stability, which is why multi-agent projects keep targeting tmux. |
| Agents that return images, plots, or screenshots | **Kitty** — the graphics protocol everyone else implements | **WezTerm** — Kitty + sixel + iTerm2 protocols, the widest support | **chafa** — in your stars already — makes almost any emulator render something | Ghostty and cmux both score zero on native graphics protocols in the agent-aware terminal scorecards. |
| Letting an autonomous agent drive the shell | **tirith** — in your stars — intercepts pipe-to-shell, ANSI injection, homograph URLs | **container-use** — in your stars — container isolation per agent, though declining upstream | **Alacritty or Ghostty + tmux** — small, boring, auditable surface | Terminal-layer attacks (ANSI injection, homograph URLs, malicious skill configs) are the agent-specific threat model; `tirith` is the only tool in your stars aimed at it. |
| Auditing what an agent actually ran | **atuin** — searchable, synced shell history across machines and sessions | **witr** — in your stars — trace any process/port/container back to its origin | **OSC 133 prompt marking** — gives the terminal per-command boundaries to record | OSC 133;C/D mark command start/end, which is what lets a terminal time, notify on, and record individual agent commands. |

## Graph analysis — how the terminal layer sits in your ecosystem

**Community clustering.** These 53 tools span **11 of the graph's 39 communities** — a scatter, not a cluster, which is itself the finding: the terminal layer has no centre of gravity in your stars the way the agent layer does.

- **Community 18** (25): `x-cmd/x-cmd`, `pranshuparmar/witr`, `hpjansson/chafa`, `hackerb9/lsix`, `mbadolato/iTerm2-Color-Schemes`, `warpdotdev/warp`, `wavetermdev/waveterm`, `Eugeny/tabby`, `alacritty/alacritty`, `wezterm/wezterm`, `gnunn1/tilix`, `zellij-org/zellij`, `gpakosz/.tmux`, `joshmedeski/sesh`, `pvolok/dekit`, `xtermjs/xterm.js`, `tsl0922/ttyd`, `MisterTea/EternalTerminal`, `ohmyzsh/ohmyzsh`, `junegunn/fzf`, `starship/starship`, `nushell/nushell`, `ajeetdsouza/zoxide`, `fish-shell/fish-shell`, `atuinsh/atuin`
- **Community 6** (8): `gnachman/iTerm2`, `tmux/tmux`, `herdrdev/herdr`, `OrchestratorInc/agent-orchestrator`, `caarlos0/dotfiles`, `manaflow-ai/cmux`, `nimbalyst/nimbalyst`, `generalaction/emdash`
- **Community 8** (5): `rothgar/awesome-tuis`, `kovidgoyal/kitty`, `omnara-ai/omnara`, `sorenisanerd/gotty`, `cmderdev/cmder`
- **Community 10** (3): `ghostty-org/ghostling`, `ghostty-org/ghostty`, `tmate-io/tmate`
- **Community 11** (3): `microsoft/terminal`, `contour-terminal/contour`, `microsoft/WSL`
- **Community 5** (2): `sheeki03/tirith`, `raphamorim/rio`
- **Community 33** (2): `dagger/container-use`, `tmux-python/libtmux`
- **Community 2** (2): `smtg-ai/claude-squad`, `butlerx/wetty`

**Centrality (PageRank in the full 2,408-repo graph)** — the most hub-like terminal-layer repos you hold:

- `wavetermdev/waveterm` — PageRank 0.0009
- `warpdotdev/warp` — PageRank 0.0008
- `pvolok/dekit` — PageRank 0.0008
- `atuinsh/atuin` — PageRank 0.0007
- `sheeki03/tirith` — PageRank 0.0007
- `fish-shell/fish-shell` — PageRank 0.0007
- `herdrdev/herdr` — PageRank 0.0006
- `cmderdev/cmder` — PageRank 0.0006
- `wezterm/wezterm` — PageRank 0.0005
- `alacritty/alacritty` — PageRank 0.0005

**Direct links between these tools** (similarity edges where both endpoints are in this report):

- `ghostty-org/ghostty` ⇄ `ghostty-org/ghostling` (w=0.722) — authors: mitchellh
- `raphamorim/rio` ⇄ `sheeki03/tirith` (w=0.545) — topics: rust, terminal; authors: github-actions[bot]
- `atuinsh/atuin` ⇄ `warpdotdev/warp` (w=0.513) — topics: shell, rust, zsh, bash; authors: dependabot[bot]
- `nushell/nushell` ⇄ `fish-shell/fish-shell` (w=0.485) — topics: shell, rust; authors: intertermux-code
- `atuinsh/atuin` ⇄ `fish-shell/fish-shell` (w=0.479) — topics: shell, rust, fish
- `pvolok/dekit` ⇄ `alacritty/alacritty` (w=0.467) — topics: linux, macos, rust, terminal
- `ajeetdsouza/zoxide` ⇄ `atuinsh/atuin` (w=0.431) — topics: rust, zsh, bash, shell; authors: dependabot[bot], ump45nose
- `pvolok/dekit` ⇄ `warpdotdev/warp` (w=0.414) — topics: linux, macos, rust, terminal
- `wavetermdev/waveterm` ⇄ `cmderdev/cmder` (w=0.403) — topics: command-line, windows; authors: dependabot[bot]
- `starship/starship` ⇄ `atuinsh/atuin` (w=0.386) — topics: rust, zsh, fish, bash; authors: ump45nose
- `wavetermdev/waveterm` ⇄ `alacritty/alacritty` (w=0.385) — topics: linux, macos, terminal, windows
- `fish-shell/fish-shell` ⇄ `warpdotdev/warp` (w=0.383) — topics: shell, terminal, rust
- `atuinsh/atuin` ⇄ `nushell/nushell` (w=0.377) — topics: shell, rust; authors: dependabot[bot]
- `wezterm/wezterm` ⇄ `Eugeny/tabby` (w=0.375) — topics: terminal-emulators, terminal, serial
- `wezterm/wezterm` ⇄ `fish-shell/fish-shell` (w=0.338) — topics: rust, terminal; authors: GhostCoder6969
- …and 46 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| Eugeny/tabby | 92 | Classic | very active | 5 | 18% | 212 |
| OrchestratorInc/agent-orchestrator | 88 | Hot | very active | 3 | 23% | 294 |
| nushell/nushell | 88 | Classic | very active | 3 | 32% | 127 |
| ohmyzsh/ohmyzsh | 85 | Classic | very active | 8 | 28% | 0 |
| omnara-ai/omnara | 84 | Hot | very active | 2 | 29% | 111 |
| fish-shell/fish-shell | 84 | Classic | very active | 2 | 47% | 71 |
| herdrdev/herdr | 83 | Hot | very active | 2 | 39% | 98 |
| atuinsh/atuin | 83 | Classic | very active | 2 | 45% | 98 |
| microsoft/terminal | 82 | Classic | very active | 2 | 34% | 159 |
| tmux/tmux | 80 | Classic | very active | 1 | 81% | 45 |
| caarlos0/dotfiles | 80 | Mature | very active | 1 | 100% | 43 |
| mbadolato/iTerm2-Color-Schemes | 80 | Classic | very active | 1 | 85% | 32 |
| kovidgoyal/kitty | 80 | Classic | very active | 1 | 76% | 146 |
| sheeki03/tirith | 79 | Rising | very active | 1 | 58% | 90 |
| generalaction/emdash | 79 | Hot | very active | 1 | 72% | 173 |
| microsoft/WSL | 79 | Classic | very active | 1 | 54% | 120 |
| raphamorim/rio | 78 | Classic | very active | 1 | 96% | 143 |
| manaflow-ai/cmux | 77 | Hot | very active | 1 | 77% | 121 |
| pranshuparmar/witr | 76 | Hot | very active | 1 | 75% | 22 |
| warpdotdev/warp | 76 | Classic | very active | 1 | 53% | 55 |
| butlerx/wetty | 76 | Classic | very active | 1 | 73% | 41 |
| junegunn/fzf | 76 | Classic | very active | 1 | 73% | 86 |
| rothgar/awesome-tuis | 75 | Classic | very active | 24 | 5% | 0 |
| nimbalyst/nimbalyst | 75 | Hot | very active | 1 | 87% | 126 |
| starship/starship | 75 | Classic | very active | 1 | 62% | 142 |
| joshmedeski/sesh | 74 | Mature | very active | 1 | 75% | 84 |
| pvolok/dekit | 73 | Classic | very active | 1 | 97% | 34 |
| sorenisanerd/gotty | 73 | Classic | very active | 1 | 82% | 13 |
| x-cmd/x-cmd | 72 | Classic | very active | 1 | 89% | 151 |
| tmux-python/libtmux | 72 | Mature | very active | 1 | 100% | 141 |
| contour-terminal/contour | 71 | Classic | very active | 1 | 75% | 40 |
| hpjansson/chafa | 70 | Mature | very active | 1 | 100% | 34 |
| zellij-org/zellij | 70 | Classic | very active | 1 | 59% | 71 |
| ghostty-org/ghostty | 69 | Classic | very active | 2 | 39% | 1 |
| wavetermdev/waveterm | 68 | Classic | very active | 1 | 72% | 163 |
| xtermjs/xterm.js | 68 | Classic | very active | 2 | 48% | 89 |
| ajeetdsouza/zoxide | 66 | Classic | very active | 2 | 33% | 38 |
| MisterTea/EternalTerminal | 65 | Classic | very active | 1 | 52% | 75 |
| wezterm/wezterm | 64 | Classic | very active | 2 | 32% | 64 |
| gpakosz/.tmux | 64 | Classic | very active | 1 | 97% | 0 |
| alacritty/alacritty | 61 | Mature | active | 2 | 33% | 108 |
| gnachman/iTerm2 | 60 | Classic | very active | 1 | 98% | 0 |
| smtg-ai/claude-squad | 59 | Declining | slowing | 2 | 33% | 20 |
| cmderdev/cmder | 48 | Mature | active | 1 | 67% | 34 |
| dagger/container-use | 44 | Mature | active | 1 | 86% | 14 |
| tmate-io/tmate | 42 | Mature | active | 1 | 50% | 5 |
| tsl0922/ttyd | 40 | Mature | slowing | 1 | 50% | 29 |
| ghostty-org/ghostling | 37 | Declining | slowing | 1 | 50% | 0 |
| gnunn1/tilix | 28 | Mature | slowing | 0 | 0% | 72 |
| blinksh/blink | 28 | Mature | slowing | 0 | 0% | 0 |
| tmux-plugins/tpm | 22 | Mature | slowing | 0 | 0% | 0 |
| mobile-shell/mosh | 20 | Declining | stale | 0 | 0% | 13 |
| hackerb9/lsix | 5 | Abandoned | stale | 0 | 0% | 10 |

Watch items:

- **`ghostty-org/ghostling`** is Declining (78d since push, 4 commits in 90d, bus factor 1) — it is a libghostty demo, not a terminal to depend on. The project you want starred is `ghostty-org/ghostty`.
- **`dagger/container-use`** is Declining (60d since push, 1 commit in 90d) despite being the isolation story for parallel agents — there is no maintained replacement in your stars.
- **`gnachman/iTerm2`** and **`tmux/tmux`** are both healthy but bus-factor 1, with top-author shares of 93% and 67%. Decade-old projects with one hand on the wheel.
- **`herdrdev/herdr`** is the interesting risk: 25,579★ in 137 days, 994 commits in 90d, 26 contributors — but bus factor 1 and a category (agent multiplexers) with a dozen competitors. High upside, high churn. Its scorecard marks here come from its own README (background server, pane state marking, socket API, Windows beta), not from hands-on testing or a third-party review — the weakest evidence base of any headline recommendation in this report.
- **Outside the dataset**, four load-bearing pieces are stale: `tmux-plugins/tmux-resurrect` (~2y, and it's the reboot-persistence story), `ekzhang/sshx` (>1y, and it's network-exposed), `ConEmu/ConEmu` (>1y), and `martanne/abduco` (3y). `stravu/crystal` has gone idle and moved to `nimbalyst/nimbalyst`.

## Which one should you use?

```
1. What OS?
   ├─ Windows ──► Windows Terminal + WSL   (or WezTerm for one emulator everywhere)
   │              cmux, Ghostty and Kitty do not run here.
   ├─ Linux ────► Ghostty or Kitty + tmux
   │              No cmux; get agent-awareness from herdr or claude-squad.
   └─ macOS ────► continue to 2.

2. How many agents at once?
   ├─ 1 ────────► Ghostty. Stop here; don't over-engineer.
   ├─ 2–3 ──────► Ghostty + tmux panes + starship (per-pane branch identity).
   ├─ 4–12 ─────► cmux — notification rings, per-tab branch/PR/worktree state.
   │              One git worktree per agent (claude --worktree).
   └─ 12+ ──────► Stop watching. agent-orchestrator + PR review queue,
                  nimbalyst or omnara for push notifications.

3. Is any of it remote, or do you leave the desk?
   ├─ Remote ───► tmux is mandatory. Add mosh or EternalTerminal.
   └─ Mobile ───► nimbalyst (iPhone) or omnara; Blink/ttyd for the raw session.
```

**The pragmatic stack if you change nothing else:** keep `tmux` as the substrate (persistence + scriptability, and it's the one layer that works identically on every OS), add `Ghostty` as the emulator on macOS or Linux — `WezTerm` if Windows is in the mix — and add exactly one state-aware layer on top: `herdr` if you want it terminal-agnostic and already in your stars, `cmux` if you're macOS-only and want notifications from the terminal itself. Run one git worktree per agent. Add `atuin` so you can reconstruct what the agents actually ran.

**What not to do:** don't pick on render benchmarks. Every GPU-accelerated terminal here is fast enough that the difference is imperceptible in normal use; the throughput column only matters when an agent dumps a very large diff. And don't run four agents in one working directory — isolation is a bigger win than any terminal feature in this report.

## Adjacent (deliberately not counted as terminal-layer tools)

- **anthropics/claude-code** (153,265★) — The agent, not the terminal — see the `ai-coding-tuis` report.
- **openai/codex** (130,791★) — Same: agent layer. This report is about what it runs inside.
- **OrchestratorInc/agent-orchestrator** (13,571★) — Also covered by `agent-orchestration` and `agent-harnesses`; listed here for its tmux dependency.
- **sheeki03/tirith** (2,765★) — Also in `ai-coding-tuis` as a safety tool; kept here because the attack surface is the terminal itself.
- **BloopAI/vibe-kanban** (28,444★) — Parallel-agent management, but a web UI rather than a terminal surface.
- **getagentseal/codeburn** (11,569★) — Token/cost tracking — `token-savings` and `ai-coding-tuis` cover it.
- **charmbracelet/bubbletea** (45,494★) — How TUIs are built, not where agents run — `ai-coding-tuis`.
- **zed-industries/zed** (92,140★) — Has a terminal, but it's an editor; out of scope.
- **gravitational/teleport** (21,018★) — Access control for infrastructure — relevant to remote agents, but an infra product, not a terminal.

## Methodology & caveats

- **In-dataset metrics**: `data/classified.json` + `public/data/graph.json`. No API calls at generation time; fully reproducible.
- **Selection**: keyword scan over `full_name + description + topics` for terminal / emulator / multiplexer / tmux / shell / pty / tui, plus the specific names of every major terminal app across macOS, Linux and Windows, then manual curation. Agent TUIs themselves were routed to `ai-coding-tuis`; fleet orchestrators with web UIs to `agent-orchestration`.
- **Gap analysis**: 7 candidate repos were checked by exact `owner/name` against the dataset and confirmed absent, then their stars, language, license, and last-push date were read from the GitHub API on 2026-08-23. Three identity problems surfaced in that check and are reflected above: `pvolok/mprocs` → `pvolok/dekit`, `stravu/crystal` → `nimbalyst/nimbalyst`, and `KDE/konsole` being a read-only mirror whose star count understates adoption. Products with no starrable repo (Otty, Termdock, amux, Paseo) are listed separately rather than fabricated into the table.
- **OS claims** come from the projects' own platform support: Ghostty on macOS + Linux with Windows planned post-1.0 and WSL2 unsupported ([discussion](https://github.com/ghostty-org/ghostty/discussions/2563)); cmux macOS-only; Kitty with no Windows build; WezTerm and waveterm tri-platform.
- **Multi-session claims are first-party.** `-w, --worktree [name]` and `--tmux` ("Create a tmux session for the worktree (requires --worktree). Uses iTerm2 native panes when available; use --tmux=classic for traditional tmux.") were read from `claude --help` on the installed binary, **v2.1.241**, on 2026-08-23. Secondary write-ups date the feature to v2.1.49 (February 2026); that date is *not* verified here and is omitted from the body.
- **Scorecard and rankings** are judgement calls informed by external evidence gathered 2026-08-23: agent-aware terminal comparisons ([codex.danielvaughan.com](https://codex.danielvaughan.com/2026/04/29/agent-aware-terminals-codex-cli-warp-cmux-ghostty-choosing-terminal-emulator/), [agentsroom.dev](https://agentsroom.dev/blog/best-terminal-for-agentic-coding)), emulator benchmarks and multiplexer head-to-heads ([dasroot.net](https://dasroot.net/posts/2026/03/linux-terminal-emulators-alacritty-kitty-wezterm/), [pistack.xyz](https://www.pistack.xyz/posts/2026-08-10-ghostty-vs-alacritty-vs-wezterm-terminal-emulator-guide/), [commandinline.com](https://www.commandinline.com/tmux-vs-zellij-comparison/)), and OSC-sequence documentation for agent notifications ([cmux docs](https://manaflow-ai-cmux.mintlify.app/features/notifications)).
- **Several sources have a commercial stake in their own conclusions.** `agentsroom.dev` ranks its own product first for multi-machine use; `amux.io` publishes the multiplexer ranking it appears in; `termdock.com` authors tmux comparisons. Their factual claims (platform support, feature presence) were cross-checked against the GitHub API and project docs where they mattered; their *verdicts* were not adopted wholesale. The recurring framing that survives across unrelated sources — attention management beats render speed past ~4 agents — is the one this report leans on.
- **Numbers are point-in-time and partly third-party.** Render-throughput and latency figures ("~4× iTerm2", "2 ms vs 3 ms") come from published 2026 comparisons, not from measurements taken here; treat them as directional. **One figure is first-party:** Ghostty's memory use was measured locally on 2026-09-06 (M2, macOS 15, Ghostty 1.3.1, idle with one window) at 23 MB resident / 33 MB phys_footprint. It replaced a third-party "60–100 MB" claim that was wrong by roughly 3× — a reminder that borrowed benchmarks rot faster than star counts, and that this class of number is worth re-measuring rather than re-citing. Independent sources also disagree on how much any of it matters in practice, and this report sides with the view that it mostly doesn't.
- **The gap table does not refresh.** Re-running the pipeline updates every in-dataset metric; the missing-repo stars and the frozen citations need a manual pass. Re-verify after any major terminal release.
- **`cmux` is very young** (created 2026-01-28; 1,751 open issues and 2,668 open PRs at check time — GitHub's `open_issues_count` of 4,419 conflates the two, and several published write-ups repeat it as an issue count). It is the top recommendation for the parallel-agent case on merit, not on stability — weigh that if you'd rather not be an early adopter.

<sub>In-dataset tools: 53 · Missing tools catalogued: 7 · Snapshot: 2026-10-24T18:18:45.023Z</sub>

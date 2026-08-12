#!/usr/bin/env python3
"""
Generate a landscape report on agent memory and conversational knowledge graphs
found in the starred-repos dataset — graph-native memory, vector-first memory,
the stores underneath them, extraction/ontology tooling, chat-workspace
connectors, meeting capture, and memory evaluation.

Beyond the usual landscape, this report carries two analyses:

  1. A PRIMITIVE COVERAGE MATRIX — which chat primitives each tool actually
     consumes, with the three reaction columns (presence / identity / timing)
     kept deliberately separate.
  2. THE UNBUILT COLUMN — the primitives no tool in the set consumes, ranked by
     how *overlooked* (rather than hard or pointless) each one is.

Matrix evidence was gathered by web search and GitHub code search on 2026-08-12
and is frozen as literal data below (the document_extraction.py TASK_RANKINGS
pattern), so generation stays deterministic and offline. Every cell carries a
basis marker distinguishing documented/code-verified findings from inference —
see PRIMITIVE_EVIDENCE and the Methodology section.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/agent-memory.md   (+ reports/agent-memory.meta.json)

Run: python3 scripts/reports/agent_memory.py
"""
import json
import os
from datetime import datetime, timezone

from lib import (fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human,
                 activity_label, make_node_for)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "agent-memory"
TITLE = "Agent Memory & Conversational Knowledge Graphs"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# Date the external evidence below was gathered. Bump when the matrix is revisited.
EVIDENCE_DATE = "2026-08-12"

# ---- Curated taxonomy --------------------------------------------------------
GRAPH_NATIVE = "Graph-native memory"
VECTOR_MEM = "Vector-first memory"
STORES = "Vector & graph stores"
EXTRACTION = "Extraction & ontology"
CONNECTORS = "Chat & workspace connectors"
CAPTURE = "Meeting & transcript capture"
EVAL = "Memory evaluation"

ORDER = [GRAPH_NATIVE, VECTOR_MEM, STORES, EXTRACTION, CONNECTORS, CAPTURE, EVAL]

TAXONOMY = {
    # Graph-native memory — the structure-first bet
    "topoteretes/cognee": (GRAPH_NATIVE, "ECL pipelines (extract → cognify → load) turning documents and chats into a queryable graph+vector memory; 30+ connectors, custom ontologies, permission controls."),
    "getzep/graphiti": (GRAPH_NATIVE, "Zep's bi-temporal knowledge graph — episodes carry both event time and ingestion time, so the graph can answer 'what did we believe, when'. The strongest temporal model in the set."),
    "MemMachine/MemMachine": (GRAPH_NATIVE, "Universal memory layer with graph-backed storage and profile memory; positions on interoperability across agent frameworks."),
    "trustgraph-ai/trustgraph": (GRAPH_NATIVE, "Deterministic context engineering — ontology-driven context graphs rather than similarity search, aimed at auditability."),
    "semantica-agi/semantica": (GRAPH_NATIVE, "Graph-native infrastructure for context and accountable AI; ontology-first, provenance as a first-class concern."),
    "shaneholloman/mcp-knowledge-graph": (GRAPH_NATIVE, "Persistent memory for MCP clients as a local knowledge graph — the minimal, hackable end of graph memory."),
    "HKUDS/MGP": (GRAPH_NATIVE, "Memory Governance Protocol — early work on *rules* for memory (what is retained, promoted, forgotten) rather than storage."),

    # Vector-first memory — the recall-first bet
    "mem0ai/mem0": (VECTOR_MEM, "The most deployed memory layer: message lists in, extracted facts out, with add/search/update/delete semantics over a vector store."),
    "MemPalace/mempalace": (VECTOR_MEM, "Benchmark-led open memory system — competes explicitly on published memory-benchmark scores."),
    "letta-ai/letta": (VECTOR_MEM, "The MemGPT lineage: stateful agents with self-editing memory blocks and an explicit context-window manager."),
    "vectorize-io/hindsight": (VECTOR_MEM, "Agent memory framed as *learning* — distilling repeated experience into reusable guidance rather than storing transcripts."),
    "TencentCloud/TencentDB-Agent-Memory": (VECTOR_MEM, "Team-level memory hub turning conversations, docs and code into reusable memory types — one of the few explicitly org-scoped rather than user-scoped."),
    "memvid/memvid": (VECTOR_MEM, "Serverless single-file memory layer — trades pipeline complexity for a portable artifact."),
    "MemoriLabs/Memori": (VECTOR_MEM, "LLM-agnostic memory infrastructure that turns agent execution and conversation into structured, queryable state."),
    "plastic-labs/honcho": (VECTOR_MEM, "Memory as *user modelling* — builds a theory-of-mind representation of each peer from dialogue, not just a fact store."),
    "zilliztech/memsearch": (VECTOR_MEM, "Unified memory across coding agents, backed by Markdown + Milvus — plain-text substrate, vector recall."),

    # Stores — the substrate both bets run on
    "qdrant/qdrant": (STORES, "High-performance vector database with rich payload filtering — the default self-hosted choice when metadata filters matter as much as similarity."),
    "milvus-io/milvus": (STORES, "Cloud-native vector database built for scale; the heavyweight of the category."),
    "weaviate/weaviate": (STORES, "Vector database storing objects *and* vectors, with hybrid search and a schema/class model."),
    "pgvector/pgvector": (STORES, "Vector similarity inside Postgres — the pragmatic pick when the relational data already lives there."),
    "lancedb/lancedb": (STORES, "Embedded, developer-friendly multimodal retrieval library — no server to operate."),
    "FalkorDB/FalkorDB": (STORES, "Sparse-matrix (GraphBLAS) graph database marketed directly at GraphRAG workloads."),
    "HelixDB/helix-db": (STORES, "OLTP graph *and* vector database in one engine — the architectural bet that the graph/vector split is an artifact, not a requirement."),

    # Extraction & ontology — how unstructured chat becomes structure
    "microsoft/graphrag": (EXTRACTION, "The reference graph-RAG implementation: entity/relationship extraction plus community summarisation over a corpus."),
    "HKUDS/LightRAG": (EXTRACTION, "Simple, fast graph-augmented retrieval — the lightweight answer to GraphRAG's indexing cost."),
    "FalkorDB/GraphRAG-SDK": (EXTRACTION, "Ontology-driven GraphRAG toolkit — schema first, extraction second."),
    "cocoindex-io/cocoindex": (EXTRACTION, "Incremental indexing engine — recomputes only what changed, which is the right shape for continuously-arriving chat."),
    "fabio-rovai/open-ontologies": (EXTRACTION, "Rust MCP server for building, validating and reasoning over RDF/OWL ontologies — formal semantics as agent tooling."),

    # Chat & workspace connectors — the tier that actually touches Slack
    "onyx-dot-app/onyx": (CONNECTORS, "Enterprise search over 40+ sources with a mature Slack connector — notably syncs Slack *permissions*, not just content."),
    "airweave-ai/airweave": (CONNECTORS, "Context retrieval layer with typed per-source entity schemas; the only tool in the set whose message entities carry reaction payloads (Teams, ClickUp)."),
    "nanocoai/nanoclaw": (CONNECTORS, "Containerised personal agent that connects to WhatsApp, Telegram, Slack and Discord — chat as the agent's primary surface."),
    "elizaOS/eliza": (CONNECTORS, "Agent OS with first-class Discord/Slack/Telegram clients — built to *live in* chat rather than index it."),
    "cyrusagents/cyrus": (CONNECTORS, "Background coding agent driven from Linear/Slack/GitHub threads — chat as the task queue."),

    # Meeting & transcript capture — the other conversational substrate
    "Zackriya-Solutions/meetily": (CAPTURE, "Privacy-first meeting assistant: live Parakeet/Whisper transcription with speaker diarization, fully local."),
    "Vexa-ai/vexa": (CAPTURE, "Meeting transcription API with auto-join bots for Meet/Teams/Zoom and real-time WebSocket streams."),
    "screenpipe/screenpipe": (CAPTURE, "24/7 screen and audio capture piped into agents — captures conversation as *pixels*, sidestepping every platform API."),

    # Evaluation
    "promptfoo/promptfoo": (EVAL, "Prompt/agent/RAG testing and red-teaming — the closest thing here to a harness for regression-testing recall."),
    "comet-ml/opik": (EVAL, "Tracing and evaluation for LLM and agentic workflows, including RAG-quality metrics."),
}

# Adjacent but deliberately excluded, with honest reasons.
ADJACENT = [
    ("vllm-project/vllm", "'memory-efficient' inference — a pure keyword collision, nothing to do with agent memory"),
    ("redis/redis", "a general datastore frequently used *as* a memory backend, but not itself a memory system"),
    ("Memento-Teams/Memento", "'teams' here means agent teams, not Microsoft Teams — collision"),
    ("infiniflow/ragflow", "general-purpose RAG engine — covered by the RAG tooling report"),
    ("deepset-ai/haystack", "orchestration framework; memory is one component among many — see RAG tooling"),
    ("run-llama/llama_index", "document/RAG platform rather than a conversational memory layer"),
    ("thedotmack/claude-mem", "coding-agent *session* memory — see the Memory Frameworks report"),
    ("gastownhall/beads", "coding-agent memory upgrade, not conversational"),
    ("ctxrs/ctx", "searches local coding-agent history — adjacent, but the corpus is agent transcripts, not human chat"),
    ("colbymchenry/codegraph", "code knowledge graph — same technique, entirely different corpus"),
    ("vitali87/code-graph-rag", "GraphRAG over monorepos, not conversations"),
    ("DeusData/codebase-memory-mcp", "codebase intelligence graph, not chat"),
    ("Graphify-Labs/graphify", "codebase → knowledge graph (and the tooling this very repo is indexed with)"),
    ("usememos/memos", "human note-taking, no agent memory API"),
    ("eugeniughelbur/obsidian-second-brain", "PKM-backed agent memory over an Obsidian vault — close, but the substrate is notes, not conversation"),
    ("agentscope-ai/ReMe", "memory management kit; overlaps the vector-first tier without adding a distinct conversational angle"),
    ("mudler/LocalRecall", "local memory/knowledge base for agents — generic document recall rather than chat-native"),
    ("HKUDS/CatchMe", "agent personalisation; memory is implicit rather than the product"),
    ("matrixorigin/Memoria", "secure memory management — security framing, thin conversational story"),
    ("supermemoryai/openclaw-supermemory", "long-term memory for one specific agent harness"),
    ("rishikanthc/Scriberr", "self-hosted transcription — see the Meeting Transcription report"),
    ("gleanwork/glean-agent-toolkit", "client toolkit for the closed-source Glean platform — the platform itself is off-dataset (see Competitors)"),
]

# ---- Primitive coverage matrix ----------------------------------------------
# Frozen findings from web + GitHub code search on EVIDENCE_DATE. Values:
#   "y" documented / verified in source   "p" partial   "n" no   "?" unknown
# Each row carries a `basis`: "code" (read in the project's source or schema),
# "docs" (stated in official documentation), "arch" (inferred from the tool's
# architecture — an inference, not a fact) or a mix.
PRIMITIVES = [
    ("txt",     "message text",              "The message body itself."),
    ("who",     "author identity",           "Which human said it, as a stable id."),
    ("ts",      "timestamp",                 "When it was said."),
    ("thr",     "thread / reply structure",  "Parent-child nesting (Slack `thread_ts`)."),
    ("→who",    "who-replies-to-whom",       "The directed interaction graph between people."),
    ("lat",     "response latency",          "How long a reply took to arrive."),
    ("edit",    "edits & deletions",         "Message revisions and retractions."),
    ("rx",      "reaction presence/count",   "That a message was reacted to, and how often."),
    ("rx-who",  "REACTION IDENTITY",         "*Which* person added each reaction."),
    ("rx-when", "REACTION ORDER & TIMING",   "The sequence and timing in which reactions accumulated."),
    ("@",       "@-mention type",            "User vs group vs @here/@channel."),
    ("acl",     "channel membership / ACL",  "Who can see the channel; permission sync."),
    ("j/l",     "joins & leaves",            "Membership changes over time."),
    ("pin",     "pins & saved",              "Human-curated importance markers."),
    ("link",    "shared links",              "URLs and attachments as first-class objects."),
    ("call",    "huddles & calls",           "Voice/huddle events and their participants."),
    ("bot",     "bot & workflow events",     "Non-human messages and workflow triggers."),
]
PRIM_KEYS = [p[0] for p in PRIMITIVES]

# name -> (basis, {primitive: value}, note)
PRIMITIVE_EVIDENCE = {
    "topoteretes/cognee": ("docs+arch", {
        "txt": "y", "who": "p", "ts": "y", "thr": "?", "→who": "n", "lat": "n", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "?", "acl": "y", "j/l": "n",
        "pin": "n", "link": "?", "call": "n", "bot": "n",
    }, "Slack is one of 30+ connectors; the pipeline is batch extract→cognify→load with "
       "custom ontologies and permission controls. Batch ingestion is the load-bearing "
       "detail: Slack's history API cannot supply reaction timing at all (see below)."),

    "getzep/graphiti": ("code+docs", {
        "txt": "y", "who": "y", "ts": "y", "thr": "n", "→who": "n", "lat": "n", "edit": "p",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "p", "j/l": "n",
        "pin": "n", "link": "n", "call": "n", "bot": "n",
    }, "Bi-temporal by design — episodes carry event time *and* ingestion time, and edges are "
       "invalidated rather than deleted, which is why `edit` scores partial. Caution: its "
       "extraction prompt praises 'reactions' in the *psychological* sense (a person's reaction "
       "to news), not emoji reactions — an easy false positive when grepping."),

    "mem0ai/mem0": ("code+docs", {
        "txt": "y", "who": "y", "ts": "y", "thr": "n", "→who": "n", "lat": "n", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "n", "j/l": "n",
        "pin": "n", "link": "n", "call": "n", "bot": "n",
    }, "Consumes `{role, content}` message lists plus a user id. Its triage prompts explicitly "
       "*discard* 'acknowledgments and emotional reactions' as low-value — the one place "
       "reactions appear, they are filtered out."),

    "letta-ai/letta": ("docs+arch", {
        "txt": "y", "who": "y", "ts": "y", "thr": "n", "→who": "n", "lat": "n", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "n", "j/l": "n",
        "pin": "n", "link": "n", "call": "n", "bot": "n",
    }, "Memory blocks over a single agent-user dialogue; multi-party chat structure is out of scope."),

    "MemoriLabs/Memori": ("arch", {
        "txt": "y", "who": "y", "ts": "y", "thr": "n", "→who": "n", "lat": "n", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "n", "j/l": "n",
        "pin": "n", "link": "n", "call": "n", "bot": "n",
    }, "Conversation → structured state. No reaction handling anywhere in the repository."),

    "plastic-labs/honcho": ("arch", {
        "txt": "y", "who": "y", "ts": "y", "thr": "p", "→who": "p", "lat": "n", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "n", "j/l": "n",
        "pin": "n", "link": "n", "call": "n", "bot": "n",
    }, "Models *peers* and sessions, so it gets closest to a social representation — but the "
       "edges it infers come from dialogue content, not from platform interaction metadata."),

    "MemMachine/MemMachine": ("arch", {
        "txt": "y", "who": "y", "ts": "y", "thr": "?", "→who": "n", "lat": "n", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "?", "j/l": "n",
        "pin": "n", "link": "n", "call": "n", "bot": "n",
    }, "Profile + episodic memory over agent conversations; no chat-platform connector tier."),

    "trustgraph-ai/trustgraph": ("arch", {
        "txt": "y", "who": "?", "ts": "?", "thr": "n", "→who": "n", "lat": "n", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "p", "j/l": "n",
        "pin": "n", "link": "n", "call": "n", "bot": "n",
    }, "Ontology-driven context graphs over documents; conversation is not a modelled source type."),

    "onyx-dot-app/onyx": ("code+docs", {
        "txt": "y", "who": "y", "ts": "y", "thr": "y", "→who": "n", "lat": "n", "edit": "p",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "p", "acl": "y", "j/l": "n",
        "pin": "n", "link": "p", "call": "n", "bot": "p",
    }, "The most complete Slack ingestion in the set — threads and document-level permission "
       "sync are both real. Reactions are *not* ingested: the only `reactions_add`/`_remove` "
       "calls are its bot posting emoji as UI. Its **Zulip** connector does carry a "
       "`has_reactions` boolean — presence-only, and on the wrong platform."),

    "airweave-ai/airweave": ("code", {
        "txt": "y", "who": "y", "ts": "y", "thr": "y", "→who": "n", "lat": "n", "edit": "n",
        "rx": "p", "rx-who": "p", "rx-when": "p", "@": "n", "acl": "p", "j/l": "n",
        "pin": "n", "link": "p", "call": "n", "bot": "n",
    }, "**The one exception in the entire set.** Its `SlackMessageEntity` has no reaction field "
       "at all, but its **Teams** entity carries `reactions: List[Dict[str, Any]]` — and "
       "Microsoft Graph's `chatMessageReaction` includes both `user` and `createdDateTime`. So "
       "airweave *transports* reaction identity and timing for Teams. It does not model, index "
       "or reason over them: the payload is an opaque dict. Partial, not yes."),

    "nanocoai/nanoclaw": ("arch", {
        "txt": "y", "who": "y", "ts": "y", "thr": "p", "→who": "n", "lat": "n", "edit": "n",
        "rx": "?", "rx-who": "n", "rx-when": "n", "@": "y", "acl": "n", "j/l": "n",
        "pin": "n", "link": "n", "call": "n", "bot": "p",
    }, "Lives inside chat platforms as an agent; consumes what it needs to respond, not to model."),

    "elizaOS/eliza": ("arch", {
        "txt": "y", "who": "y", "ts": "y", "thr": "p", "→who": "n", "lat": "n", "edit": "n",
        "rx": "?", "rx-who": "n", "rx-when": "n", "@": "y", "acl": "n", "j/l": "?",
        "pin": "n", "link": "n", "call": "n", "bot": "y",
    }, "Discord/Slack clients are first-class, and @-mentions drive activation — but the "
       "platform's social metadata is a trigger, never a stored signal."),

    "cyrusagents/cyrus": ("arch", {
        "txt": "y", "who": "y", "ts": "y", "thr": "p", "→who": "n", "lat": "n", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "y", "acl": "n", "j/l": "n",
        "pin": "n", "link": "n", "call": "n", "bot": "p",
    }, "Threads are task containers, not memory. Nothing is retained after the task closes."),

    "Zackriya-Solutions/meetily": ("docs+arch", {
        "txt": "y", "who": "y", "ts": "y", "thr": "n", "→who": "n", "lat": "p", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "n", "j/l": "n",
        "pin": "n", "link": "n", "call": "y", "bot": "n",
    }, "Speaker diarization gives real author identity, and turn timestamps make response "
       "latency *implicitly* available — nobody computes it, but the data is right there."),

    "Vexa-ai/vexa": ("docs+arch", {
        "txt": "y", "who": "y", "ts": "y", "thr": "n", "→who": "n", "lat": "p", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "n", "j/l": "p",
        "pin": "n", "link": "n", "call": "y", "bot": "n",
    }, "Auto-join bots see participant join/leave events for the meeting itself — the only "
       "place membership dynamics are observed anywhere in this set."),

    "screenpipe/screenpipe": ("arch", {
        "txt": "p", "who": "n", "ts": "y", "thr": "n", "→who": "n", "lat": "n", "edit": "n",
        "rx": "n", "rx-who": "n", "rx-when": "n", "@": "n", "acl": "n", "j/l": "n",
        "pin": "n", "link": "n", "call": "p", "bot": "n",
    }, "Captures pixels, so it is the only tool that could *see* reactions appear in order — "
       "and the only one that models none of it. Everything arrives as undifferentiated OCR text."),
}

# Off-dataset competitors — not in the stars, so not in TAXONOMY, but the gap
# analysis is worthless if it ignores them.
COMPETITORS = [
    ("Beever Atlas", "github.com/Beever-AI/beever-atlas", "Apache-2.0, open source",
     "Votee AI (HK) + Beever AI (Toronto), open-sourced May 2026. Telegram/Discord/Mattermost/"
     "Teams/Slack → Neo4j knowledge graph + auto-generated wiki + MCP memory layer. A 6-stage "
     "pipeline distilling messages into atomic facts, entities and relationships.",
     "**The closest thing to your build that already exists, and it is not in your stars.** "
     "Its Slack docs list `Reactions | ✅ Metadata captured` and it requests the "
     "`reactions:read` scope — but its bridge types them as `{name, count}`, dropping identity, "
     "and its fact-extractor prompt lists reactions under **skip criteria** alongside greetings "
     "and acknowledgments. It captures the signal and then throws it away."),
    ("Untangle", "getuntangle.app", "closed SaaS",
     "Memory layer over Slack, Teams, GitHub, Jira, Linear, Zoom and Confluence; chronological "
     "work history, urgency detection, automated summaries, bring-your-own-model.",
     "Competes on *consolidation and recall*, not on structure — no public knowledge-graph "
     "claim. Urgency detection is the one place a timing signal shows up commercially."),
    ("Glean", "glean.com", "closed enterprise",
     "Enterprise search and assistant across workspace tools, with permission-aware retrieval.",
     "Only `gleanwork/glean-agent-toolkit` (64★) is in your stars — the client shim, not the "
     "platform. Sets the enterprise bar for ACL-correct retrieval."),
    ("Zep", "getzep.com", "commercial, OSS core",
     "The hosted product behind `getzep/graphiti`, which *is* in your stars.",
     "Effectively already covered: the interesting engineering — the bi-temporal model — is in "
     "the open-source core you have starred."),
    ("Scientia", "—", "unverified",
     "Named as a competitor but not identifiable from public sources on the evidence date.",
     "**Could not verify this exists** as a product in this space. Searches surfaced only "
     "generic agent-memory listicles. Treat the name as unconfirmed until you have a URL — "
     "it is not evidence of anything either way."),
]

# ---- Load --------------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)

by_name = {r["full_name"]: r for r in cl["repos"]}
nodes_by_id = {n["id"]: n for n in gr["nodes"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}

sel_names = list(TAXONOMY.keys())
sel_node_ids = {name_to_nodeid[n] for n in sel_names if n in name_to_nodeid}
inter_edges = [l for l in gr["links"]
               if l["source"] in sel_node_ids and l["target"] in sel_node_ids]
node_for = make_node_for(nodes_by_id, name_to_nodeid)

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)

# Rows of the matrix that exist in the dataset, in taxonomy order.
matrix_rows = [n for n in sel_names if n in PRIMITIVE_EVIDENCE and n in by_name]

MARK = {"y": "✅", "p": "◐", "n": "✖", "?": "?"}


def col_values(key):
    """All marks for one primitive across the matrix rows."""
    return [PRIMITIVE_EVIDENCE[n][1][key] for n in matrix_rows]


# ---- Build -------------------------------------------------------------------
gen = cl.get("generatedAt", "")
user = cl.get("username", "")
lines = []
A = lines.append

A(f"# {TITLE}")
A("")
A(f"> Derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`), cross-referenced with the repo-similarity graph "
  f"({fmt_int(len(gr['nodes']))} nodes / {fmt_int(len(gr['links']))} edges, "
  f"{len(gr['communities'])} communities). The primitive-coverage matrix is "
  f"additionally backed by documentation and source-code evidence gathered "
  f"{EVIDENCE_DATE} — see Methodology.")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/agent_memory.py` (regenerate any time — no API cost).")
A("")

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} tools** across the memory stack (**{fmt_int(total_stars)}★** combined):")
for c in ORDER:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`"
                      for x in sorted(cats[c], key=lambda x: -by_name[x]["stars"])))
A("- The category has split into two bets. **Vector-first** memory (`mem0`, `mempalace`, "
  "`letta`) optimises *recall* — get the relevant fact back. **Graph-native** memory "
  "(`cognee`, `graphiti`, `trustgraph`) optimises *structure* — represent how facts relate. "
  "Your Cognee + Qdrant stack deliberately spans both, which is the right call: the "
  "interesting queries over a Slack corpus are relational, but the retrieval still has to "
  "be fuzzy.")
A("- **`graphiti` is the only tool here with a serious temporal model** (bi-temporal: event "
  "time *and* ingestion time, with edge invalidation instead of deletion). Everything else "
  "treats time as a sortable field. If your hackathon thesis is temporal, that is the prior "
  "art to read.")
A("- The connector tier and the memory tier barely overlap. Tools that *reach* Slack "
  "(`onyx`, `airweave`) do not build memory; tools that *are* memory (`mem0`, `cognee`) "
  "treat Slack as one undifferentiated text source. **The gap between them is where the "
  "chat primitives get dropped.**")
A("- The matrix below tests the hypothesis that tools consume little beyond text, author and "
  "timestamp. **It largely holds, with two corrections** — thread structure and ACL are "
  "better covered than expected (the connector tier does real work there), and one tool "
  "carries reaction identity *and* timing for Microsoft Teams. Details in the two sections "
  "that follow.")
A("- Memory **evaluation is nearly absent**. `promptfoo` and `opik` are general LLM/RAG "
  "harnesses, not memory benchmarks; only `mempalace` competes explicitly on memory "
  "benchmark scores. Nobody in your set can tell you whether a memory layer got *better*.")
A("")

# --- Anatomy / pipeline table
A("## The memory pipeline at a glance")
A("")
A("Where each tier sits between a Slack message and an agent's answer.")
A("")
A("| Stage | What happens | Tools in your stars |")
A("|---|---|---|")
A("| **Capture** | Get the conversation out of the platform | "
  "`onyx`, `airweave`, `nanoclaw`, `eliza`, `cyrus`, `meetily`, `vexa`, `screenpipe` |")
A("| **Extraction** | Text → entities, relationships, atomic facts | "
  "`graphrag`, `LightRAG`, `GraphRAG-SDK`, `cocoindex`, `open-ontologies` |")
A("| **Structure** | Facts → a graph with types, time and provenance | "
  "`cognee`, `graphiti`, `MemMachine`, `trustgraph`, `semantica`, `mcp-knowledge-graph` |")
A("| **Recall** | Query-time retrieval into the context window | "
  "`mem0`, `mempalace`, `letta`, `hindsight`, `Memori`, `honcho`, `memvid`, `memsearch` |")
A("| **Storage** | The substrate underneath both | "
  "`qdrant`, `milvus`, `weaviate`, `pgvector`, `lancedb`, `FalkorDB`, `helix-db` |")
A("| **Governance** | What is retained, promoted, forgotten | "
  "`MGP`, and partially `trustgraph` |")
A("| **Evaluation** | Did any of it work? | `promptfoo`, `opik` |")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | "
  "Activity | Last push | Age | Contrib(90d) |")
A("|" + "---|" * 11)
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    A("| [{name}]({url}) | {cat} | {lang} | {lic} | {stars} | {lc} | {hs} | "
      "{act} | {push} | {age} | {auth} |".format(
        name=n, url=r["url"], cat=TAXONOMY[n][0],
        lang=r.get("primary_language") or "—",
        lic=(r.get("license") or "—"),
        stars=fmt_stars(r),
        lc=r.get("lifecycle_stage") or "—",
        hs=r.get("health_score") if r.get("health_score") is not None else "—",
        act=activity_label(r),
        push=days_to_human(r.get("days_since_push")) + " ago",
        age=days_to_human(r.get("age_days")),
        auth=r.get("unique_authors_90d") if r.get("unique_authors_90d") is not None else "—",
    ))
A("")

# --- Primitive coverage matrix
A("## Primitive coverage matrix")
A("")
A("**The question:** of everything a chat platform knows about a conversation, how much does "
  "each tool actually consume? Rows are the tools that ingest conversational data — stores, "
  "extraction libraries and evaluation harnesses are excluded because they consume whatever "
  "schema you hand them and so cannot be scored.")
A("")
A("Legend: ✅ consumed · ◐ partial / transported but not modelled · ✖ not consumed · ? undetermined")
A("")
A("| Col | Primitive | What it means |")
A("|---|---|---|")
for key, name, desc in PRIMITIVES:
    A(f"| `{key}` | {name} | {desc} |")
A("")
A("**Basis** distinguishes what was verified from what was reasoned: `code` = read in the "
  "project's source or entity schema; `docs` = stated in official documentation; "
  "`arch` = inferred from the tool's architecture, and therefore an inference rather than a "
  "documented fact.")
A("")
hdr = "| Tool | Basis | " + " | ".join(f"`{k}`" for k in PRIM_KEYS) + " |"
A(hdr)
A("|" + "---|" * (len(PRIM_KEYS) + 2))
for n in matrix_rows:
    basis, vals, _note = PRIMITIVE_EVIDENCE[n]
    cells = " | ".join(MARK[vals[k]] for k in PRIM_KEYS)
    A(f"| `{n.split('/')[-1]}` | {basis} | {cells} |")
A("")
A("### Per-tool notes")
A("")
for n in matrix_rows:
    _basis, _vals, note = PRIMITIVE_EVIDENCE[n]
    A(f"- **`{n}`** — {note}")
A("")

# --- Hypothesis verdict (computed, not asserted)
A("### Verdict on the hypothesis")
A("")
core = ["txt", "who", "ts"]
core_yes = sum(1 for n in matrix_rows
               if all(PRIMITIVE_EVIDENCE[n][1][k] == "y" for k in core))
rest_keys = [k for k in PRIM_KEYS if k not in core]
rest_marks = [PRIMITIVE_EVIDENCE[n][1][k] for n in matrix_rows for k in rest_keys]
rest_yes = sum(1 for m in rest_marks if m == "y")
rest_partial = sum(1 for m in rest_marks if m == "p")
density = rest_yes / len(rest_marks) if rest_marks else 0
A(f"The hypothesis was: *almost every tool consumes only text, author and timestamp, and the "
  f"right-hand columns are nearly empty.*")
A("")
A(f"- **Confirmed on the left.** {core_yes} of {len(matrix_rows)} tools consume all three core "
  f"primitives — the floor is universal.")
A(f"- **Confirmed on the right.** Across the other {len(rest_keys)} primitives × "
  f"{len(matrix_rows)} tools = {len(rest_marks)} cells, only **{rest_yes} are a full ✅ "
  f"({density:.0%})**, with {rest_partial} partial. The right-hand side of this matrix is "
  f"mostly empty, exactly as predicted.")
A("- **Correction 1 — you underrated the connector tier.** `thr` (thread structure) and `acl` "
  "(permissions) are genuinely well covered by `onyx` and `airweave`. Slack's reply graph is "
  "not unexploited territory; its *social* metadata is.")
A("- **Correction 2 — one tool does carry reaction timing, and you should know about it.** "
  "`airweave`'s Microsoft Teams entity stores raw `chatMessageReaction` dicts, and Microsoft "
  "Graph includes `createdDateTime` and `user` on every reaction. So reaction identity and "
  "timing *are* being transported today — on Teams, as an opaque payload, by a tool that "
  "never reads them. Nobody **reasons** over reaction ordering anywhere in this set.")
A("")
A("**The platform asymmetry is the finding that matters for your build:**")
A("")
A("| Platform | Reaction identity | Reaction timing | Available in backfill? |")
A("|---|---|---|---|")
A("| **Slack** | `users[]` array, may be incomplete | **not exposed at all** | "
  "No — history returns `{name, users, count}` with no timestamps |")
A("| **Microsoft Teams** | `user` per reaction | `createdDateTime` per reaction | "
  "Yes — via Microsoft Graph `chatMessageReaction` |")
A("")
A("Slack's message payload carries `reactions: [{name, users, count}]` and nothing more — no "
  "per-reaction timestamp exists in the history API, and the docs warn the `users` array "
  "*'might not always contain all users that have reacted'*, with no documented ordering. The "
  "only place Slack emits reaction timing is the **`reaction_added` event**, which carries "
  "`event_ts`, `user` and the target `item`.")
A("")
A("**Consequence, stated plainly:** on Slack, reaction ordering is a *live-capture-only* "
  "signal. No batch ingestion — including Cognee's — can ever reconstruct it from history. If "
  "you want it, you must be subscribed to `reaction_added` before the reactions happen. That "
  "is also the structural reason nobody has built on it: the data does not exist in the "
  "corpus everyone starts from.")
A("")

# --- The unbuilt column
A("## The unbuilt column")
A("")
zero_cols = [(k, name) for (k, name, _d) in PRIMITIVES
             if k not in core and "y" not in col_values(k)]
A(f"Primitives that **no tool in the set fully consumes** — {len(zero_cols)} of "
  f"{len(rest_keys)}:")
A("")
A("| Primitive | Best any tool manages | Why it is unexploited | 3-hour prototype |")
A("|---|---|---|---|")

UNBUILT = [
    ("pin", "**Pins & saved**", "Nothing — zero coverage",
     "**Overlooked.** Trivially available (`pins.list`), tiny volume, and the single "
     "highest-precision relevance label a workspace produces: a human explicitly said "
     "*this matters*.",
     "Weight graph nodes by pin status. Pinned messages become high-confidence seed entities; "
     "compare retrieval quality against an unweighted graph on the same queries."),
    ("→who", "**Who-replies-to-whom**", "◐ — `honcho` infers social structure from content only",
     "**Overlooked.** `thread_ts` is already ingested by half the connector tier; nobody "
     "aggregates it into a directed person→person graph. It is a `GROUP BY` away.",
     "Build the reply graph from data you already ingest, run PageRank per channel, and use "
     "'who does this person actually talk to' as a retrieval prior."),
    ("rx-who", "**Reaction identity**", "◐ — `airweave` transports it for Teams only",
     "**Overlooked.** Slack gives you `users[]` for free in the same payload as the message. "
     "Beever Atlas requests `reactions:read`, then discards identity at the adapter boundary "
     "by typing reactions as `{name, count}`.",
     "Treat a 👍 as a typed edge `person -[endorsed]-> message`. Consensus and dissent become "
     "queryable: *which decisions did nobody endorse?*"),
    ("j/l", "**Joins & leaves**", "◐ — `vexa` sees it for meetings, never for channels",
     "**Overlooked.** Membership events are in the same history stream as messages. They tell "
     "you who was *present* for a decision — the difference between 'we agreed' and 'the three "
     "people still here agreed'.",
     "Reconstruct channel membership over time; answer 'who was in the room' for any past "
     "decision node in the graph."),
    ("edit", "**Edits & deletions**", "◐ — `graphiti` invalidates edges, but not from edit events",
     "**Overlooked, and cheap.** A retraction is the strongest possible negative signal about a "
     "stored fact, and every memory layer here will happily keep serving the deleted version.",
     "Subscribe to `message_changed`/`message_deleted` and invalidate the derived facts. This "
     "is a correctness bug in every batch memory layer, demoed in an afternoon."),
    ("lat", "**Response latency**", "◐ — implicit in `meetily`/`vexa` turn timestamps, never computed",
     "**Half-overlooked.** Trivial to compute from two timestamps you already store. Nobody "
     "does. Signals urgency, escalation, and informal authority.",
     "Compute reply latency per thread; flag the threads where latency collapsed as candidate "
     "incidents, and use it to rank decision-bearing conversations."),
    ("rx-when", "**Reaction ordering & timing**", "◐ — `airweave` transports it for Teams only",
     "**Technically hard on Slack, and that is the whole story.** Not overlooked: structurally "
     "unavailable. History gives no per-reaction timestamps, so only a live `reaction_added` "
     "subscription can capture it. Every batch-first architecture in this category is "
     "*locked out* of this column by construction.",
     "Run a listener that stamps `reaction_added` events. Even one afternoon of live capture "
     "yields ordering nobody else has: first-reactor as an authority signal, and the "
     "accumulation curve as a proxy for how contested a message was."),
    ("call", "**Huddles & calls**", "◐ — `meetily`/`vexa` capture call *content*, not call *events*",
     "**Commercially thin.** The huddle event says two people talked; the interesting content "
     "is audio that a different tool already handles. Low information per unit of integration work.",
     "Probably skip. If anything, use huddle events only as edges — 'these two spoke' — to "
     "densify an otherwise text-only social graph."),
    ("bot", "**Bot & workflow events**", "◐ — `eliza` reacts to them; nobody stores them",
     "**Mostly correct to ignore.** High volume, low semantic density — CI noise. But "
     "deploy/alert bots are precisely the timeline anchors that make 'what happened when' "
     "answerable.",
     "Ingest bot messages as *event* nodes only, never as facts. They become the temporal "
     "spine the human conversation hangs off."),
]
for key, label, best, why, proto in UNBUILT:
    A(f"| {label} | {best} | {why} | {proto} |")
A("")
A("**Ranked by actionability for a three-hour build**, which is what you asked for:")
A("")
A("1. **Pins** — highest signal-to-effort ratio in the entire matrix. One API call, and it is "
   "a human-labelled relevance set you can evaluate against.")
A("2. **Reaction identity as typed edges** — the data is already in the message payload you "
   "are ingesting. This is the cheapest thing here that nobody has done.")
A("3. **The reply graph** — pure aggregation over `thread_ts` you already have.")
A("4. **Live `reaction_added` capture** — the only one that is genuinely novel rather than "
   "merely unbuilt, because the corpus everyone else uses cannot contain it. Highest ceiling, "
   "and the one worth starting the clock on first since it only accumulates while running.")
A("")
A("The honest framing for a demo: items 1–3 are *overlooked*, so the story is \"this was "
  "always available and the field walked past it\". Item 4 is *structurally excluded*, so the "
  "story is \"this cannot be retrofitted — you had to be listening\". The second is the more "
  "defensible claim, and it is also the one that decays if you start capturing late.")
A("")

# --- Category deep dives
A("## By category")
A("")
cat_blurb = {
    GRAPH_NATIVE: "Structure-first memory: extract entities and relationships, store them as a "
                  "graph, and answer relational questions. Costs more to build, pays off when "
                  "the question is 'how do these connect' rather than 'what did we say'.",
    VECTOR_MEM: "Recall-first memory: embed, store, retrieve the top-k. Simpler to operate and "
                "hard to beat on latency; weak whenever the answer is a path rather than a passage.",
    STORES: "The substrate. Note `helix-db` and `FalkorDB` betting that the graph/vector split "
            "is an implementation artifact rather than a real architectural boundary.",
    EXTRACTION: "The layer that turns unstructured conversation into typed structure — the "
                "step that actually determines what your graph can answer.",
    CONNECTORS: "The tier that touches Slack. Mature on content and permissions, indifferent to "
                "social metadata — which is precisely where this report's gap analysis lives.",
    CAPTURE: "Conversation that never passes through a chat API: meetings, calls, screens. "
             "Different acquisition problem, same memory problem downstream.",
    EVAL: "Thin, and general-purpose rather than memory-specific. The category's weakest link.",
}
for cat in ORDER:
    members = cats.get(cat) or []
    if not members:
        continue
    A(f"### {cat}")
    A("")
    A(f"_{cat_blurb[cat]}_")
    A("")
    for n in sorted(members, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        topics = ", ".join((r.get("topics") or [])[:8]) or "—"
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ · {r.get('primary_language') or '—'} · "
          f"{r.get('lifecycle_stage','—')}  ")
        A(f"  {TAXONOMY[n][1]}  ")
        A(f"  <sub>topics: {topics}</sub>")
    A("")

# --- Graph analysis
A("## Graph analysis — how they relate")
A("")
comm = {}
for n in present:
    nd = node_for(n)
    if nd is not None:
        comm.setdefault(nd.get("community"), []).append(n)
A(f"**Community clustering.** These {len(present)} tools span "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — a wide spread for "
  f"one report, which is itself the finding: 'agent memory' is not one community in your "
  f"stars, it is a theme cutting across several.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)** — the most "
  "hub-like memory tools in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between these tools** (top similarity edges where both endpoints are in "
  "this report):")
A("")
id_to_name = {v: k for k, v in name_to_nodeid.items()}
linked = set()
if inter_edges:
    shown = sorted(inter_edges, key=lambda x: -x["weight"])[:15]
    for e in shown:
        a = id_to_name.get(e["source"], e["source"])
        b = id_to_name.get(e["target"], e["target"])
        linked.add(a)
        linked.add(b)
        why = []
        if e.get("shared_topics"):
            why.append("topics: " + ", ".join(e["shared_topics"][:4]))
        if e.get("shared_authors"):
            why.append("authors: " + ", ".join(e["shared_authors"][:3]))
        A(f"- `{a}` ⇄ `{b}` (w={e['weight']:.3f})" + (f" — {'; '.join(why)}" if why else ""))
    if len(inter_edges) > 15:
        A(f"- …and {len(inter_edges) - 15} more.")
else:
    A("- _None._")
A("")

for e in inter_edges:
    linked.add(id_to_name.get(e["source"], ""))
    linked.add(id_to_name.get(e["target"], ""))
isolated = [n for n in present if n not in linked]
A(f"**Isolation.** {len(isolated)} of {len(present)} tools have *no* similarity edge to any "
  f"other tool in this report. Isolation is only meaningful in the tiers that are supposed to "
  f"cluster — a database sharing no vocabulary with a memory framework says nothing, so the "
  f"stores tier is discounted below. For the rest, the call is mine, based on isolation × "
  f"activity:")
A("")
A("| Isolated tool | ★ | Tier | Activity | Edges in full graph | Read |")
A("|" + "---|" * 6)


def full_degree(name):
    """Edge count in the whole 1,596-repo graph, not just this report's slice."""
    nid = name_to_nodeid.get(name)
    if nid is None:
        return 0
    return sum(1 for l in gr["links"] if l["source"] == nid or l["target"] == nid)


def isolation_verdict(name):
    """Name the call — including when the honest call is 'the metric can't support one'."""
    deg = full_degree(name)
    act = activity_label(by_name[name])
    fading = act in ("slowing", "stale") or (by_name[name].get("commits_90d") or 0) < 10
    if deg >= 5 and not fading:
        return ("**Artifact, not a signal** — well connected in the wider graph, just not to "
                "these 38. Different neighbourhood, not a dead end.")
    if deg >= 5 and fading:
        return ("**Watch** — connected elsewhere, but its own activity is fading. The risk is "
                "maintenance, not obscurity.")
    if fading:
        return "**Dead end** — few edges anywhere *and* losing momentum. Read it as fading."
    return ("**Genuinely peripheral, still moving** — few edges anywhere but actively "
            "developed. Early or idiosyncratic; the one shape worth a look.")


for n in sorted(isolated, key=lambda x: -by_name[x]["stars"]):
    A(f"| `{n}` | {fmt_int(by_name[n]['stars'])} | {TAXONOMY[n][0]} | "
      f"{activity_label(by_name[n])} | {full_degree(n)} | {isolation_verdict(n)} |")
A("")
A("**My read, and a correction to the obvious one.** The tempting story — *isolated in a "
  "crowded category means unexploited angle* — does not survive contact with the data here. "
  "Every isolated tool above still has "
  f"{min(full_degree(n) for n in isolated)}–{max(full_degree(n) for n in isolated)} edges in "
  "the full graph. They are not isolated in the ecosystem; they are isolated *in this "
  "report's slice of it*, because this graph's edges come from shared topics and shared "
  "contributors, and a Microsoft research repo simply does not share either with a "
  "single-maintainer MCP server. `microsoft/graphrag` is the proof: the most-copied approach "
  "in the whole category, and it shows up here with zero in-report edges. Calling that an "
  "unexploited angle would be a metric artifact dressed up as an insight.")
A("")
fading_iso = [n for n in isolated
              if activity_label(by_name[n]) in ("slowing", "stale")
              or (by_name[n].get("commits_90d") or 0) < 10]
if fading_iso:
    A("What the column *can* support is the narrower claim: isolation only becomes evidence "
      "when it coincides with fading activity. On that test the names that matter are "
      + ", ".join(f"`{n}`" for n in sorted(fading_iso, key=lambda x: -by_name[x]["stars"]))
      + " — and of those, only the ones you would actually depend on are worth acting on "
        "(see the maintenance table below).")
    A("")

# --- Maintenance & risk
A("## Maintenance & risk — alive or abandoned")
A("")
A("A memory tool that stopped shipping is a warning about the category, not just the repo. "
  "Bus factor = commit concentration (1 = single-maintainer risk).")
A("")
A("| Tool | Category | Health | Lifecycle | Activity | Last push | Bus factor | Top-author share |")
A("|" + "---|" * 8)
for n in sorted(present, key=lambda x: (by_name[x].get("health_score") or 0,
                                        by_name[x]["stars"])):
    r = by_name[n]
    tas = r.get("top_author_share")
    A("| `{n}` | {cat} | {h} | {lc} | {act} | {push} | {bf} | {tas} |".format(
        n=n, cat=TAXONOMY[n][0], h=r.get("health_score", "—"),
        lc=r.get("lifecycle_stage", "—"), act=activity_label(r),
        push=days_to_human(r.get("days_since_push")) + " ago",
        bf=r.get("bus_factor", "—"),
        tas=f"{tas:.0%}" if isinstance(tas, (int, float)) else "—"))
A("")
stale = [n for n in present if activity_label(by_name[n]) in ("slowing", "stale")]
solo = [n for n in present
        if (by_name[n].get("bus_factor") or 99) <= 1 and by_name[n]["stars"] > 1000]
if stale:
    A(f"**Slowing or stale ({len(stale)}):** " + ", ".join(f"`{n}`" for n in sorted(stale)) + ". ")
A(f"**Single-maintainer risk ({len(solo)} above 1k★):** "
  + ", ".join(f"`{n}`" for n in sorted(solo)) + ".")
A("")
A("Read the stale list as a statement about the category: agent memory has had a high launch "
  "rate and a high abandonment rate since 2025. Anything you build on here should treat the "
  "memory layer as replaceable — keep extraction and storage separable so a dead dependency "
  "costs you a rewrite of one module, not the graph.")
A("")

# --- Which one should you use
A("## Which one should you use?")
A("")
A("| If you are… | Use | Why |")
A("|---|---|---|")
A("| Building a Slack memory layer in three hours | **`cognee` + `qdrant`** | "
  "Your existing pick, and correct: Cognee gives ontology-shaped extraction with a Slack "
  "connector, Qdrant gives payload filtering you will need for per-channel scoping. |")
A("| Needing 'what did we believe, and when' | **`graphiti`** | "
  "The only bi-temporal model here. If your demo hinges on time, read it before building. |")
A("| Wanting recall with minimum ceremony | **`mem0`** | "
  "Message list in, facts out. Shallow, fast, and it will not model your reply graph. |")
A("| Needing ACL-correct retrieval over Slack | **`onyx`** | "
  "Genuine Slack permission sync. The only tool here that treats access control as real. |")
A("| Needing typed per-source entity schemas | **`airweave`**, with a caveat | "
  "Its entity definitions are the best documentation of what each SaaS API actually exposes — "
  "but it is the slowest-moving tool in this report (67 days since last push, 6 commits in 90 "
  "days, 2 authors). Read its schemas; do not depend on it. |")
A("| Capturing conversation off-platform | **`meetily`** or **`vexa`** | "
  "Local-first vs API-first respectively; both give speaker identity, which chat rarely does better. |")
A("| Evaluating whether memory improved | **nothing here is sufficient** | "
  "`promptfoo` can regression-test prompts; no tool in your set benchmarks memory quality. "
  "Build a fixed question set by hand and diff answers. |")
A("")
A("**For the hackathon specifically:** start the `reaction_added` listener before you write "
  "anything else. It is the only signal in this report that cannot be backfilled — every "
  "minute it is not running is data you cannot recover, and it is also the only column where "
  "you would be demonstrably first.")
A("")

# --- Off-dataset competitors
A("## Competitors not in your stars")
A("")
A("A gap analysis that only looks at starred repos will hallucinate open space. These were "
  "checked against the dataset and are **not** in it:")
A("")
for name, url, lic, what, why in COMPETITORS:
    A(f"### {name}")
    A("")
    A(f"_{url} · {lic}_")
    A("")
    A(f"- **What it is:** {what}")
    A(f"- **Why it matters to you:** {why}")
    A("")
A("**The actionable one is Beever Atlas.** It is Apache-2.0, ships the chat→knowledge-graph "
  "pipeline you are planning, and — per its own docs and source — captures reactions as "
  "`{name, count}` while instructing its extractor to skip reaction-only messages. That is "
  "simultaneously the strongest evidence that your gap is real *and* the clearest warning "
  "that someone else is one small change away from closing it. Worth starring and reading "
  "before you start.")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed as memory tools)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `data/classified.json` + `public/data/graph.json` for all repo metrics and "
  "graph structure. No API calls at generation time; fully reproducible.")
A("- **Selection**: keyword scan over `full_name` + `description` + `topics` for memory, "
  "knowledge graph, graph rag, temporal graph, entity extraction, ontology, retrieval, rag, "
  "vector, embedding, semantic search, conversation, chat history, slack, discord, teams, "
  "transcript, meeting notes, second brain, pkm, note-taking, context engineering, episodic "
  "and recall — 225 candidates, hand-curated to "
  f"{len(present)}. Matches were checked against descriptions, not just names: "
  "`vllm` ('memory-efficient'), `sudo-rs` ('memory safe'), `Graphite`/`PixiEditor` ('vector' "
  "graphics) and `Memento`/`NeMo-Agent-Toolkit` ('agent teams', not Microsoft Teams) are "
  "keyword collisions and were excluded.")
A(f"- **Primitive matrix evidence** was gathered on {EVIDENCE_DATE} from official "
  "documentation and GitHub code search, and is frozen as literal data in the generator so "
  "regeneration stays deterministic and offline. Primary sources:")
A(f"  - Slack: [`reactions.get`](https://docs.slack.dev/reference/methods/reactions.get/) "
  "(reaction objects are `{name, users, count}` — no timestamps; the docs state the `users` "
  "array *'might not always contain all users that have reacted'*) and "
  "[`reaction_added`](https://docs.slack.dev/reference/events/reaction_added/) "
  "(carries `event_ts`, `user`, `item`).")
A("  - Microsoft: [`chatMessageReaction`](https://learn.microsoft.com/en-us/graph/api/resources/chatmessagereaction) "
  "(carries `createdDateTime` and `user` per reaction).")
A("  - Source-level checks via GitHub code search across `cognee`, `graphiti`, `mem0`, `onyx`, "
  "`airweave`, `letta`, `Memori`, `honcho` and `Beever-AI/beever-atlas`.")
A("- **Basis markers are load-bearing.** Rows marked `arch` are inferences from architecture, "
  "not documented facts, and are the most likely to be wrong. A `✖` on an `arch` row means "
  "'no evidence found', which is weaker than 'confirmed absent'. Rows marked `code` were read "
  "in the project's own source or entity schemas and are the strongest claims here.")
A("- **Known limits of this evidence.** Absence of a keyword in a repository is not proof a "
  "feature is missing; several tools could consume a primitive through a generic metadata "
  "passthrough without ever naming it. The three reaction columns were checked most carefully "
  "because they carry the report's central claim; the long tail (`pin`, `j/l`, `call`) was "
  "checked less exhaustively and is more likely to contain a false `✖`.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag "
  "GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars and activity; the matrix and the "
  "competitor section are frozen text and need manual review when these tools ship "
  "connector changes.")
A("")
A(f"<sub>Tools covered: {len(present)} · Matrix rows: {len(matrix_rows)} · "
  f"Evidence date: {EVIDENCE_DATE} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta (consumed by build_index.py) --------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / RAG",
    "summary": (f"{len(present)} agent-memory and conversational-knowledge-graph tools "
                f"({fmt_int(total_stars)}★): graph-native vs vector-first memory, the stores "
                "underneath, chat connectors and meeting capture — plus a primitive-coverage "
                "matrix of which chat signals each tool actually consumes, and a ranked "
                "analysis of the ones nobody consumes at all."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in ORDER},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/agent_memory.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
print(f"  matrix rows: {len(matrix_rows)}")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
missing_adj = [n for n, _ in ADJACENT if n not in by_name]
if missing_adj:
    print("  WARNING adjacent missing:", missing_adj)

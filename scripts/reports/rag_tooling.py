#!/usr/bin/env python3
"""
Generate a comprehensive report on RAG (Retrieval-Augmented Generation) tooling
found in the starred-repos dataset: end-to-end frameworks/engines, vector
databases, ingestion/parsing/chunking, embeddings/rerankers, and novel
retrieval approaches.

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/rag-tooling.md   (+ reports/rag-tooling.meta.json)

Run: python3 scripts/reports/rag_tooling.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "rag-tooling"
TITLE = "RAG (Retrieval-Augmented Generation) Tooling — Landscape Report"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
TAXONOMY = {
    # End-to-end RAG frameworks & engines
    "infiniflow/ragflow": ("RAG framework / engine", "Leading OSS RAG engine; deep document understanding + template-based chunking, batteries included."),
    "run-llama/llama_index": ("RAG framework / engine", "The 'document agent' framework — data connectors, indices, query engines; foundational RAG toolkit."),
    "HKUDS/LightRAG": ("RAG framework / engine", "Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall."),
    "deepset-ai/haystack": ("RAG framework / engine", "Pipeline-oriented orchestration for production RAG / context-engineered LLM apps."),
    "HKUDS/RAG-Anything": ("RAG framework / engine", "All-in-one multimodal RAG over text, tables, images, equations."),
    "llmware-ai/llmware": ("RAG framework / engine", "Enterprise RAG with small, specialized models; private-deployment focus."),
    "SylphAI-Inc/AdalFlow": ("RAG framework / engine", "Library to build & *auto-optimize* LLM/RAG apps (prompt + retriever tuning)."),
    "airweave-ai/airweave": ("RAG framework / engine", "Context-retrieval layer that syncs apps/DBs into agent-queryable knowledge."),
    "Bessouat40/RAGLight": ("RAG framework / engine", "Lightweight modular RAG framework for quick pipelines."),
    "FalkorDB/GraphRAG-SDK": ("RAG framework / engine", "SDK to build GraphRAG apps on FalkorDB at scale."),

    # Vector databases & similarity search
    "qdrant/qdrant": ("Vector DB / search", "High-performance, massive-scale vector DB & search engine (Rust)."),
    "chroma-core/chroma": ("Vector DB / search", "AI-native search/vector DB; popular default for prototyping RAG."),
    "weaviate/weaviate": ("Vector DB / search", "Vector DB storing objects + vectors with hybrid (keyword+vector) search."),
    "pgvector/pgvector": ("Vector DB / search", "Vector similarity search as a Postgres extension — RAG without new infra."),
    "alibaba/zvec": ("Vector DB / search", "Lightweight, lightning-fast in-process vector database."),
    "facebookresearch/faiss": ("Vector DB / search", "Foundational dense-vector similarity-search library; the index under many DBs."),
    "FalkorDB/FalkorDB": ("Vector DB / search", "Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval."),

    # Ingestion / parsing / chunking
    "Unstructured-IO/unstructured": ("Ingestion / parsing / chunking", "ETL that turns PDFs/docs/HTML into clean, chunk-ready structured elements."),
    "PaddlePaddle/PaddleOCR": ("Ingestion / parsing / chunking", "Powerful OCR — turns PDFs/images into structured text for the RAG ingest stage."),
    "chonkie-inc/chonkie": ("Ingestion / parsing / chunking", "Lightweight, fast chunking library (the 🦛) — many strategies, minimal deps."),
    "chonkie-inc/chonkiejs": ("Ingestion / parsing / chunking", "TypeScript port of Chonkie for JS/TS RAG pipelines."),

    # Embeddings / retrieval models / rerankers
    "huggingface/sentence-transformers": ("Embeddings / rerankers", "SoTA embeddings, retrieval & reranking models — the encoder layer of RAG."),
    "illuin-tech/colpali": ("Embeddings / rerankers", "Vision embeddings (ColPali/ColQwen) for document retrieval straight from page images."),
    "superlinked/sie": ("Embeddings / rerankers", "Inference engine/server for embeddings & rerankers in production retrieval."),

    # Novel / efficient retrieval approaches
    "VectifyAI/PageIndex": ("Novel retrieval approach", "Vectorless, reasoning-based RAG — builds a document index/tree, navigates with the LLM."),
    "yichuan-w/LEANN": ("Novel retrieval approach", "Storage-frugal RAG: ~97% storage savings while keeping fast, accurate retrieval."),
    "zilliztech/claude-context": ("Novel retrieval approach", "Code-search MCP that makes an entire codebase the retrievable context for coding agents."),
}

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("langchain-ai/langchain", "general agent/LLM framework — RAG is one use case, too broad to list as RAG-specific"),
    ("topoteretes/cognee", "covered in the *memory frameworks* report (graph memory, RAG-adjacent)"),
    ("memvid/memvid", "covered in the *memory frameworks* report"),
    ("NirDiamant/RAG_Techniques", "excellent *tutorial* collection, not a tool/library"),
    ("KRLabsOrg/LettuceDetect", "RAG *evaluation* (hallucination detection) — see the LLM-evaluation report"),
]

# Themes that cut across categories
GRAPHRAG = ["HKUDS/LightRAG", "FalkorDB/GraphRAG-SDK", "FalkorDB/FalkorDB"]

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

def node_for(name):
    nid = name_to_nodeid.get(name)
    return nodes_by_id.get(nid) if nid else None

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
        return f"{d//30}mo"
    return f"{d/365:.1f}y"

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
  f"{len(gr['communities'])} communities).")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/rag_tooling.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = ["RAG framework / engine", "Vector DB / search",
         "Ingestion / parsing / chunking", "Embeddings / rerankers",
         "Novel retrieval approach"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} RAG tools** in your stars (**{fmt_int(total_stars)}★** combined) — "
  f"the largest AI category here — organized along the RAG pipeline:")
for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A(f"- Mental model — RAG is a pipeline: **ingest/parse → chunk → embed → store/index → "
  f"retrieve/rerank → generate**. Each category above owns one stage; the frameworks stitch "
  f"them together.")
A(f"- Two clear trends: **GraphRAG** (graph-structured retrieval — `LightRAG`, "
  f"`GraphRAG-SDK`, `FalkorDB`) and **post-vector** retrieval that questions the embed-everything "
  f"default (`PageIndex` vectorless, `LEANN` 97% storage savings).")
A(f"- Python dominates the frameworks; the vector-DB layer is mostly systems languages "
  f"(Rust/Go/C/C++) for performance.")
A("")

# --- Pipeline table
A("## The RAG pipeline at a glance")
A("")
A("| Stage | What happens | Tools in your stars |")
A("|---|---|---|")
A("| **Ingest / parse** | PDFs, images, HTML → clean text/elements | "
  "`unstructured`, `PaddleOCR` |")
A("| **Chunk** | Split documents into retrievable units | "
  "`chonkie`, `chonkiejs` |")
A("| **Embed / rerank** | Encode chunks & queries; reorder hits | "
  "`sentence-transformers`, `colpali`, `sie` |")
A("| **Store / index** | Persist vectors/graphs for ANN search | "
  "`qdrant`, `chroma`, `weaviate`, `pgvector`, `zvec`, `faiss`, `FalkorDB` |")
A("| **Retrieve / generate** | Orchestrate retrieval + LLM answer | "
  "`ragflow`, `llama_index`, `haystack`, `LightRAG`, `RAG-Anything`, `llmware`, `AdalFlow`, `airweave`, `RAGLight`, `GraphRAG-SDK` |")
A("| **Rethink** | Approaches that change the pipeline itself | "
  "`PageIndex` (vectorless), `LEANN` (tiny storage), `claude-context` (code) |")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | "
  "Activity | Last push | Age | Contrib(90d) |")
A("|" + "---|" * 12)
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    A("| [{name}]({url}) | {cat} | {lang} | {lic} | {stars} | {lc} | {hs} | "
      "{act} | {push} | {age} | {auth} |".format(
        name=n, url=r["url"], cat=TAXONOMY[n][0],
        lang=r.get("primary_language") or "—",
        lic=(r.get("license") or "—"),
        stars=fmt_int(r["stars"]),
        lc=r.get("lifecycle_stage") or "—",
        hs=r.get("health_score") if r.get("health_score") is not None else "—",
        act=activity_label(r),
        push=days_to_human(r.get("days_since_push")) + " ago",
        age=days_to_human(r.get("age_days")),
        auth=r.get("unique_authors_90d") if r.get("unique_authors_90d") is not None else "—",
    ))
A("")

# --- Category deep dives
A("## By category")
A("")
cat_blurb = {
    "RAG framework / engine": "End-to-end systems that orchestrate the whole pipeline. "
        "Engines (ragflow) are batteries-included apps; libraries (llama_index, haystack) "
        "are composable toolkits.",
    "Vector DB / search": "Where embeddings live and approximate-nearest-neighbour search "
        "happens. Choice often comes down to scale, hybrid search, and ops footprint.",
    "Ingestion / parsing / chunking": "The unglamorous-but-decisive front of the pipeline: "
        "garbage chunks in → garbage retrieval out.",
    "Embeddings / rerankers": "The models that turn text (or page images) into vectors and "
        "reorder candidate hits for precision.",
    "Novel retrieval approach": "Projects challenging the embed-everything-into-a-vector-DB "
        "default — vectorless, storage-frugal, or domain-specialized retrieval.",
}
for cat in order:
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

# --- GraphRAG theme
A("## Spotlight: GraphRAG")
A("")
A("A cross-cutting trend — instead of a flat vector store, build a **knowledge graph** over "
  "chunks so retrieval can follow relationships (better for multi-hop questions). In your stars:")
A("")
for n in GRAPHRAG:
    r = by_name.get(n)
    if r:
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ — {TAXONOMY[n][1]}")
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
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities**.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A("**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' RAG tools "
  "in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between RAG tools** (top similarity edges where both endpoints are in "
  "this report):")
A("")
if inter_edges:
    id_to_name = {v: k for k, v in name_to_nodeid.items()}
    shown = sorted(inter_edges, key=lambda x: -x["weight"])[:15]
    for e in shown:
        a = id_to_name.get(e["source"], e["source"])
        b = id_to_name.get(e["target"], e["target"])
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

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle "
  "+ activity before adopting.")
A("")
A("| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |")
A("|---|---|---|---|---|---|---|")
for n in sorted(present, key=lambda x: -(by_name[x].get("health_score") or 0)):
    r = by_name[n]
    tas = r.get("top_author_share")
    A("| {n} | {h} | {lc} | {act} | {bf} | {tas} | {rel} |".format(
        n=n, h=r.get("health_score", "—"), lc=r.get("lifecycle_stage", "—"),
        act=activity_label(r), bf=r.get("bus_factor", "—"),
        tas=f"{tas:.0%}" if isinstance(tas, (int, float)) else "—",
        rel=r.get("releases_total", "—")))
A("")

# --- Selection guidance
A("## Which one should you use?")
A("")
A("| If you want… | Start with | Why |")
A("|---|---|---|")
guide = [
    ("A batteries-included RAG app over your docs", "`infiniflow/ragflow`",
     "Most-starred engine here (health 96); strong document parsing + chunking out of the box."),
    ("A composable toolkit to build custom RAG", "`run-llama/llama_index` or `deepset-ai/haystack`",
     "Mature libraries; connectors, indices, and pipeline primitives."),
    ("Graph-structured / multi-hop retrieval", "`HKUDS/LightRAG`",
     "Fast GraphRAG; builds an entity graph over chunks."),
    ("A production vector store at scale", "`qdrant/qdrant`",
     "High-performance Rust vector DB; health 88, widely deployed."),
    ("RAG with zero new infrastructure", "`pgvector/pgvector`",
     "Adds vector search to the Postgres you already run."),
    ("Best document parsing for ingestion", "`Unstructured-IO/unstructured` (+ `PaddleOCR`)",
     "Turns messy PDFs/HTML into clean, chunkable elements; OCR for scanned docs."),
    ("Good chunking without heavy deps", "`chonkie-inc/chonkie`",
     "Lightweight, many strategies; JS port available."),
    ("To skip vector DBs entirely", "`VectifyAI/PageIndex`",
     "Vectorless, reasoning-based retrieval over a document tree."),
    ("Tiny-footprint / on-device RAG", "`yichuan-w/LEANN`",
     "~97% storage savings vs. a conventional vector index."),
]
for want, pick, why in guide:
    A(f"| {want} | {pick} | {why} |")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed as RAG tools)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external "
  "calls; fully reproducible.")
A("- **Selection**: keyword scan (rag / retrieval-augmented / graphrag / vector db / "
  "embedding / rerank / chunk / semantic-search) + manual curation into pipeline stages. "
  "Tutorials, general agent frameworks, and memory-layer projects were routed to adjacent "
  "reports or excluded (see above).")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may "
  "lag GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars/activity.")
A("")
A(f"<sub>Tools covered: {len(present)} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta (consumed by build_reports_index.py) ------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / RAG",
    "summary": (f"{len(present)} RAG tools ({fmt_int(total_stars)}★) across the pipeline: "
                "frameworks/engines, vector DBs, ingestion/chunking, embeddings/rerankers, "
                "and novel retrieval approaches."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/rag_tooling.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)

#!/usr/bin/env python3
"""
Generate a landscape report on LLM-driven 3D modelling for 3D printing:
code-CAD authoring, parametric component libraries, implicit/SDF modelling,
generative image-to-3D, mesh validation & repair, print prep & slicing, and
the agent bridges that wire them together.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/3d-printing-stack.md   (+ reports/3d-printing-stack.meta.json)

Run: python3 scripts/reports/printing_stack.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for, retired_rows

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "3d-printing-stack"
TITLE = "LLM-Driven 3D Modelling for 3D Printing — Landscape Report"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

RETIRED = {}

# ---- Curated taxonomy --------------------------------------------------------
C_CAD = "Code-CAD authoring"
C_LIB = "Parametric component library"
C_SDF = "Implicit / SDF modelling"
C_GEN = "Generative 3D (image→mesh)"
C_FIX = "Mesh validation & repair"
C_PRN = "Print prep & slicing"
C_AGT = "Agent bridge / viewer"

TAXONOMY = {
    # --- Code-CAD authoring: the model writes code, the code makes geometry
    "openscad/openscad": (C_CAD, "CSG solid modeller scripted in its own language. The largest CAD corpus any LLM has trained on — generated code compiles more often than for any other target here."),
    "CadQuery/cadquery": (C_CAD, "Python on the OpenCascade B-rep kernel; fluent API, real fillets/chamfers, STEP export. Larger ecosystem than build123d."),
    "gumyr/build123d": (C_CAD, "The cleaner successor API to CadQuery — same OCCT kernel, builder + algebra modes, far more Pythonic to generate."),
    "KittyCAD/modeling-app": (C_CAD, "Zoo Design Studio: the KCL language, a native text-to-CAD ML API and the Zookeeper conversational agent on a purpose-built B-rep engine."),
    "BOMWiki/partmode": (C_CAD, "Local-first parametric CAD running in the browser on OpenCascade — a good human review surface for agent-authored geometry."),

    # --- Component libraries: grounding, so the model stops inventing dimensions
    "BelfrySCAD/BOSL2": (C_LIB, "Threads, gears, rounding, joiners and attachments for OpenSCAD. The single biggest quality jump available to an LLM authoring loop."),
    "nophead/NopSCADlib": (C_LIB, "Hundreds of real 'vitamins' — fasteners, bearings, extrusions, PSUs — with correct measured dimensions."),
    "gumyr/cq_warehouse": (C_LIB, "Bearings, fasteners and thread profiles with real dimensions for CadQuery / build123d."),

    # --- Implicit: organic form that is watertight by construction
    "fogleman/sdf": (C_SDF, "Signed-distance-function modelling in Python. Organic shapes that are watertight by construction — skips the repair stage entirely."),
    "libfive/libfive": (C_SDF, "The heavier implicit-geometry kernel; functional representation with interactive meshing."),
    "NVIDIA/warp": (C_SDF, "Differentiable GPU kernels with marching cubes — the performant route to SDF and volumetric geometry."),

    # --- Generative: where 'astonishing' comes from, and where printability dies
    "microsoft/TRELLIS.2": (C_GEN, "Structured-latent 3D generation; the strongest open-weight visual quality for image-to-3D."),
    "Tencent-Hunyuan/Hunyuan3D-2": (C_GEN, "Open-weight shape + PBR texture generation. Different failure modes to TRELLIS, so useful as a second opinion."),
    "img2threejs/img2threejs": (C_GEN, "Rebuilds a reference image as procedural, quality-gated *code* rather than a mesh — the generative look with code-CAD guarantees."),
    "TencentARC/Pixal3D": (C_GEN, "Pixel-aligned 3D generation from images (SIGGRAPH 2026); tighter fidelity to a reference than diffusion-only paths."),
    "TencentARC/InstantMesh": (C_GEN, "Fast feed-forward single-image-to-3D via multi-view diffusion + sparse-view reconstruction."),
    "Comfy-Org/ComfyUI": (C_GEN, "The node graph that actually runs the generators above locally, reproducibly, with the pre/post steps attached."),

    # --- Validation & repair: the layer that decides whether it prints
    "mikedh/trimesh": (C_FIX, "The assert layer. is_watertight, winding consistency, Euler number, volume and bounds — turns 'looks fine' into a pass/fail an agent can loop against."),
    "elalish/manifold": (C_FIX, "Guaranteed-manifold boolean kernel — also what modern OpenSCAD uses internally. Booleans that cannot emit broken geometry."),
    "pyvista/pymeshfix": (C_FIX, "One call turns a generative mesh into a watertight polyhedron: removes singularities, self-intersections and degenerate faces."),
    "cnr-isti-vclab/meshlab": (C_FIX, "The canonical mesh processing and repair application — the interactive surface for diagnosing what went wrong."),
    "cnr-isti-vclab/PyMeshLab": (C_FIX, "MeshLab's filter set as a Python API. Without it, none of the repair capability is scriptable."),
    "wjakob/instant-meshes": (C_FIX, "Instant field-aligned retopology. Turns 200k unstructured generative triangles into a clean quad mesh that slices predictably."),
    "isl-org/Open3D": (C_FIX, "Point-cloud and mesh operations — the entry point if geometry comes from scanning rather than generating."),

    # --- Print prep & slicing: the reward signal
    "OrcaSlicer/OrcaSlicer": (C_PRN, "The slicer to automate against: documented CLI, exit codes, and overhang detection/mitigation flags."),
    "prusa3d/PrusaSlicer": (C_PRN, "The reference slicer every Orca-family fork descends from; same CLI patterns, useful as a cross-check."),
    "Ultimaker/CuraEngine": (C_PRN, "Headless slicing engine with no GUI attached — the easiest thing to embed directly in a loop."),
    "3MFConsortium/lib3mf": (C_PRN, "Reference implementation of 3MF. STL discards colour, materials and per-object settings; 3MF is the only format that carries them."),

    # --- Agent bridges & viewers
    "ahujasid/mcp-for-blender": (C_AGT, "Puts Blender under direct agent control — print-toolbox checks, booleans, displacement, decimation."),
    "neka-nat/freecad-mcp": (C_AGT, "Parametric GUI CAD under agent control, leaving a feature tree a human can pick up afterwards."),
    "f3d-app/f3d": (C_AGT, "Fast CLI 3D viewer that screenshots from arbitrary cameras — the render-back step that gives a vision model eyes."),
    "meshy-dev/meshy-3d-agent": (C_AGT, "Agent skills for a hosted 3D-generation platform; a reference pattern for wiring generation into a tool loop."),
}

ORDER = [C_CAD, C_LIB, C_SDF, C_GEN, C_FIX, C_PRN, C_AGT]

CAT_BLURB = {
    C_CAD: "LLMs are unreliable at emitting vertices and good at emitting code. These are the "
           "targets that code gets written against — the choice sets your compile-success rate.",
    C_LIB: "Grounding. Handing the model a library of correct parts beats asking it to derive "
           "involute gear maths or an M3 thread, which it will get subtly and invisibly wrong.",
    C_SDF: "The missing middle between boxy CSG and beautiful-but-broken generative meshes: "
           "organic form that is manifold by construction, so the repair stage never happens.",
    C_GEN: "Where visual impact comes from — and where printability goes to die. Output is "
           "routinely non-manifold, self-intersecting, baseless and sub-nozzle in places.",
    C_FIX: "The layer that decides whether a model prints. Assertions first, repair second, "
           "retopology third. Everything here is scriptable, which is the point.",
    C_PRN: "Slicing headlessly and reading the result back is the loop's reward signal: "
           "print time, filament, support volume, and hard failures.",
    C_AGT: "The wiring. Bridges hand an agent a real modelling application; the viewer closes "
           "the perception gap by turning geometry back into an image the model can judge.",
}

# Repos whose low health score means 'finished', not 'dead'
STABLE_NOT_DEAD = {
    "wjakob/instant-meshes": "Research code from the 2015 SIGGRAPH paper. Feature-complete and still "
                             "the default field-aligned retopology tool; nothing has replaced it.",
    "fogleman/sdf": "A small, complete single-purpose library. The SDF maths does not change.",
    "nophead/NopSCADlib": "A dimension library. Slow commit rate reflects a stable parts catalogue, not neglect.",
    "gumyr/cq_warehouse": "Same — a fastener and bearing catalogue; churn would be a bad sign.",
}

# Genuinely at risk — low health for the ordinary reason
WATCH = {
    "Tencent-Hunyuan/Hunyuan3D-2": "Pinned to the 2.x line while the upstream family has moved on; "
                                   "treat as a snapshot, not a maintained dependency.",
    "TencentARC/InstantMesh": "No push since Jan 2025 and superseded by TRELLIS.2 on quality. Keep for "
                              "speed comparisons; do not build on it.",
    "cnr-isti-vclab/PyMeshLab": "Binding lags the MeshLab application it wraps. Have pymeshfix as a fallback.",
}

# Adjacent but deliberately excluded
ADJACENT = [
    ("agmmnn/awesome-blender", "a curated *list*, not a tool — useful for finding the Blender 3D-Print Toolbox, but not part of the stack"),
    ("voxel51/fiftyone", "dataset curation for visual AI; matched on 'voxel' but unrelated to solid modelling"),
    ("CesiumGS/3d-tiles", "geospatial 3D streaming — a different meaning of 3D entirely"),
    ("the3deer/android-3D-model-viewer", "an Android STL/OBJ viewer app, not a modelling or prep tool"),
    ("modelcontextprotocol/servers", "the MCP substrate the bridges build on — covered in the *MCP tooling* report"),
    ("blender/blender", "not starred; reachable via `mcp-for-blender` and listed there instead"),
]

# The loop: stage -> (what happens, tools)
PIPELINE = [
    ("Intent", "Prompt, reference images, hard constraints", "_the chat model_"),
    ("Author", "Emit code, or generate a mesh", "`openscad`, `build123d`, `cadquery`, `sdf`, `TRELLIS.2`, `Hunyuan3D-2`"),
    ("See", "Render back to an image the model can judge", "`f3d`, `mcp-for-blender`"),
    ("Validate", "Machine-checkable assertions on the mesh", "`trimesh`, `manifold`, `Open3D`"),
    ("Repair", "Make it watertight; fix topology", "`pymeshfix`, `PyMeshLab`, `meshlab`, `instant-meshes`"),
    ("Prep", "Orient, split, hollow, carry materials", "`lib3mf`, `mcp-for-blender`, `freecad-mcp`"),
    ("Slice", "G-code, and the warnings that come with it", "`OrcaSlicer`, `PrusaSlicer`, `CuraEngine`"),
]

# Task rankings — evidence gathered at authoring time, frozen into the generator
TASK_RANKINGS = [
    ("Functional part that must fit real hardware",
     [("openscad/openscad", "+ BOSL2; highest compile-success rate"),
      ("gumyr/build123d", "when you need true fillets and STEP out"),
      ("CadQuery/cadquery", "larger ecosystem, more training data")],
     "Text2CAD-Bench (arXiv 2605.18430) found models degrade sharply on raw command sequences versus a Python CAD API; CadQuery-family scripts are the stronger LLM target."),
    ("Sculptural piece that must still print",
     [("fogleman/sdf", "watertight by construction — no repair stage"),
      ("microsoft/TRELLIS.2", "best open visual quality, then repair"),
      ("img2threejs/img2threejs", "procedural code from a reference image")],
     "Generative meshes are reported non-manifold with inverted normals and 50k+ unorganised triangles as the normal case; the SDF route avoids the class of defect rather than repairing it."),
    ("Turning an AI mesh into something the slicer accepts",
     [("pyvista/pymeshfix", "one call to a watertight polyhedron"),
      ("wjakob/instant-meshes", "retopology before decimation"),
      ("mikedh/trimesh", "verify the result actually passed")],
     "PyMeshFix implements the MeshFix algorithm: removes singularities, self-intersections and degenerate elements while leaving defect-free regions untouched."),
    ("Closing the loop without a human in it",
     [("f3d-app/f3d", "render N cameras headless"),
      ("OrcaSlicer/OrcaSlicer", "exit codes + overhang flags as reward"),
      ("ahujasid/mcp-for-blender", "when the fix needs a real modeller")],
     "OrcaSlicer documents a headless CLI with defined exit codes plus --detect-overhang-wall and --make-overhang-printable, which is what makes automated pass/fail possible."),
    ("Letting an agent drive an application directly",
     [("ahujasid/mcp-for-blender", "28k★; mesh, materials, print toolbox"),
      ("neka-nat/freecad-mcp", "parametric, leaves a feature tree"),
      ("KittyCAD/modeling-app", "commercial text-to-CAD + agent")],
     "Zoo shipped the Zookeeper conversational CAD agent with Design Studio v1.1 in Jan 2026, adding engine-level tools to inspect and debug geometry mid-generation."),
]

SELECTION = [
    ("The highest chance that generated code just compiles", "`openscad/openscad` + `BelfrySCAD/BOSL2`",
     "Biggest training corpus of any CAD target, and BOSL2 supplies the primitives the model would otherwise derive wrong."),
    ("Parts with real fillets that export to STEP", "`gumyr/build123d`",
     "OCCT B-rep kernel with the most generation-friendly Python API here."),
    ("Organic shapes without a repair stage", "`fogleman/sdf`",
     "Signed distance functions mesh to watertight geometry by construction."),
    ("Maximum visual impact from a reference image", "`microsoft/TRELLIS.2`",
     "Strongest open-weight image-to-3D quality — budget for retopology and repair after it."),
    ("A single assertion to gate every model", "`mikedh/trimesh`",
     "is_watertight plus volume and bounds is 90% of the value for three lines of code."),
    ("Automated slicing you can read results from", "`OrcaSlicer/OrcaSlicer`",
     "Documented CLI, exit codes and overhang detection; health 83 and shipping."),
    ("Colour or multi-material output", "`3MFConsortium/lib3mf`",
     "STL cannot carry it; 3MF can."),
    ("An agent that operates a real modeller", "`ahujasid/mcp-for-blender`",
     "28k★ and the broadest capability surface of the bridges here."),
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
  f"`scripts/reports/printing_stack.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} tools** ({fmt_int(total_stars)}★ combined) covering the full path from a "
  f"prompt to g-code, grouped by the stage of the pipeline they own:")
for c in ORDER:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- **The principle the stack rests on:** chat models are unreliable at emitting mesh geometry "
  "and reliable at emitting *code that generates* geometry. Nothing here asks a model for an STL. "
  "It writes a script, the script runs, the result is rendered, asserted on, and sliced.")
A("- **Output quality is set by loop tightness, not model choice.** The two stages people skip — "
  "rendering the model back to an image the LLM can judge, and asserting on the mesh before "
  "slicing — are the two that separate printable output from plausible-looking failures.")
A("- **Looking good and printing are different problems.** The generative tools solve the first "
  "and actively work against the second: their meshes are routinely non-manifold, self-intersecting "
  "and baseless. The implicit/SDF route sidesteps the whole class of defect by making geometry "
  "watertight by construction.")
A("- Authoring is Python and OpenSCAD; the validation, repair and slicing layers are almost "
  "entirely C++, which is why they are fast enough to sit inside an automated loop.")
A("")

# --- Pipeline table
A("## The loop, stage by stage")
A("")
A("| Stage | What happens | Tools in your stars |")
A("|---|---|---|")
for stage, what, tools in PIPELINE:
    A(f"| **{stage}** | {what} | {tools} |")
A("")
A("Stages **See** and **Validate** are the ones normally missing. Without _See_, the model is "
  "authoring blind and iterates on geometry it has never perceived. Without _Validate_, nothing "
  "distinguishes a model that will print from one that merely renders.")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits. Read the low health scores in "
  "this set with care — see *Maintenance & risk* below.")
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

# --- Task rankings
A("## Best tool per task")
A("")
A("Rankings combine the dataset's metrics with web research carried out when this generator was "
  "written; the evidence column is frozen text and does not refresh with the data.")
A("")
A("| Task | 🥇 First pick | 🥈 Second | 🥉 Third | Evidence / note |")
A("|---|---|---|---|---|")
for task, picks, evidence in TASK_RANKINGS:
    cells = []
    for repo, note in picks:
        short = repo.split("/")[-1]
        cells.append(f"`{short}`<br><sub>{note}</sub>")
    A(f"| **{task}** | {cells[0]} | {cells[1]} | {cells[2]} | {evidence} |")
A("")

# --- Category deep dives
A("## By category")
A("")
for cat in ORDER:
    members = cats.get(cat) or []
    if not members:
        continue
    A(f"### {cat}")
    A("")
    A(f"_{CAT_BLURB[cat]}_")
    A("")
    for n in sorted(members, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        topics = ", ".join((r.get("topics") or [])[:8]) or "—"
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ · {r.get('primary_language') or '—'} · "
          f"{r.get('lifecycle_stage','—')}  ")
        A(f"  {TAXONOMY[n][1]}  ")
        A(f"  <sub>topics: {topics}</sub>")
    A("")

# --- Blueprints
A("## Three stacks worth assembling")
A("")
A("### 1. Parametric, agent-driven — functional parts")
A("")
A("For enclosures, brackets, adapters: anything that has to fit something that already exists.")
A("")
A("```")
A("prompt → openscad + BOSL2 → f3d renders 4 cameras → vision critique → re-author")
A("                                     ↓ (on pass)")
A("                       trimesh asserts → OrcaSlicer CLI → g-code + warnings")
A("```")
A("")
A("The critique and assert steps both feed back to authoring. Compile success is highest here "
  "because OpenSCAD is the best-represented CAD language in training data, and BOSL2 removes the "
  "geometry the model would otherwise derive incorrectly.")
A("")
A("### 2. Generative, repaired — sculptural work")
A("")
A("Highest visual ceiling, longest path to something printable.")
A("")
A("```")
A("reference image → ComfyUI[TRELLIS.2 | Hunyuan3D-2] → instant-meshes retopo")
A("     → pymeshfix watertight → trimesh verify → mcp-for-blender orient/base → slicer")
A("```")
A("")
A("Every stage after generation exists to undo a property of generative output. Budget for it: "
  "a mesh that renders beautifully will typically fail `is_watertight` on the first try.")
A("")
A("### 3. Implicit / SDF — organic form, no repair stage")
A("")
A("The route that gets skipped most often and deserves to be tried first for sculptural work.")
A("")
A("```")
A("prompt → model writes an SDF (fogleman/sdf) → marching cubes → watertight by construction")
A("     → f3d render → critique → straight to slicer")
A("```")
A("")
A("No repair layer, because the class of defect cannot occur. The trade is that form is expressed "
  "as maths rather than sculpted — which happens to be a thing language models are good at writing.")
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
A("**Centrality (PageRank in the full graph)** — the most hub-like tools of this set:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")
A("**Direct links** (similarity edges where both endpoints are in this report):")
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
    A("- _None — this set is newly assembled and the similarity graph has not yet linked it._")
A("")

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("This set breaks the usual reading of health scores, so it is worth stating plainly: **a "
  "geometry library with a low health score is often finished rather than dead.** Mesh algorithms "
  "and fastener dimensions do not change. Commit velocity is a poor proxy for viability here in a "
  "way it is not for, say, an agent framework.")
A("")
A("**Low health, but finished — safe to depend on:**")
A("")
for n, why in STABLE_NOT_DEAD.items():
    r = by_name.get(n)
    if r:
        A(f"- **`{n}`** · health {r.get('health_score','—')} · {r.get('lifecycle_stage','—')} — {why}")
A("")
A("**Low health for the ordinary reason — treat with care:**")
A("")
for n, why in WATCH.items():
    r = by_name.get(n)
    if r:
        A(f"- **`{n}`** · health {r.get('health_score','—')} · {r.get('lifecycle_stage','—')} — {why}")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk).")
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
for want, pick, why in SELECTION:
    A(f"| {want} | {pick} | {why} |")
A("")

# --- Constraints
A("## Constraints to put in the system prompt")
A("")
A("A model will not infer these, and stating them removes most unprintable output before the "
  "first render. Figures assume a 0.4 mm nozzle on FDM.")
A("")
A("| Constraint | Value | Note |")
A("|---|---|---|")
A("| Minimum wall thickness | 0.8–1.2 mm | 2–3 perimeters |")
A("| Unsupported overhang | ≤ 45° | 55° achievable with good part cooling |")
A("| Unsupported bridge | 5–10 mm | longer spans need support |")
A("| Smallest feature | 0.4 mm wide, 0.3 mm deep | below nozzle width it disappears |")
A("| Clearance, loose fit | 0.3 mm | press fit 0.1 mm |")
A("| Minimum hole diameter | 2 mm | holes print ~0.15 mm undersize |")
A("| Bottom-edge chamfer | 0.2 mm | counteracts elephant's foot |")
A("| Resin hollowing | 2 mm wall | plus 2 × 3 mm drain holes |")
A("| Build volume | 256³ mm typical | split beyond, with registration features |")
A("")
A("Three rules that matter more than any single number: **require a flat base** — generative "
  "models almost never produce one, and it is the most common cause of a failed art print; "
  "**state which axis takes load**, because parts are weakest across layer lines; and **split "
  "oversized parts with dovetails or pins**, not a bare plane cut — BOSL2 has both.")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls at "
  "generation time; fully reproducible.")
A("- **Selection**: keyword scan over `full_name + description + topics + README` for 35 CAD, "
  "mesh and printing terms, then a cross-check of 60 curated ecosystem repos for presence, then "
  "manual curation into pipeline stages. Name collisions were filtered by description — 'mesh' "
  "matches service meshes, 'cura' matches 'accuracy', 'stl' matches Rust and C++ standard-library "
  "references.")
A("- **Origin**: this landscape began as a gap audit. At the 2026-09-06 snapshot only 12 of these "
  "tools were starred and four of the seven pipeline stages had no coverage at all; the validation, "
  "print-prep and slicing layers were entirely absent. Twenty-one repos were added on 2026-09-12 "
  "to close those gaps, and this report covers the completed set.")
A("- **Task rankings** are backed by web research carried out at authoring time (Text2CAD-Bench "
  "arXiv:2605.18430; OrcaSlicer CLI documentation; PyMeshFix/MeshFix documentation; Zoo Design "
  "Studio release notes; open image-to-3D comparisons, September 2026). That text is frozen in the "
  "generator and will not refresh with the dataset — re-verify when major releases land.")
A("- **Printing figures** are conventional starting points for FDM at 0.4 mm, not measurements "
  "from your printer. Calibrate with test coupons before trusting a tolerance.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and lag GitHub's "
  "current state. In this set especially, low health frequently means *finished* — see above.")
A("")
for _line in retired_rows(RETIRED, by_name):
    A(_line)
A(f"<sub>Tools covered: {len(present)} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "Engineering",
    "summary": (f"{len(present)} tools ({fmt_int(total_stars)}★) for driving 3D modelling with LLMs: "
                "code-CAD authoring, parametric libraries, implicit/SDF modelling, generative "
                "image-to-3D, mesh validation & repair, and print prep & slicing."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in ORDER},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/printing_stack.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)

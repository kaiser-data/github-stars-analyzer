# Tree-stump base for a Pokal

> Built from the **3d-printing-stack** report, against 2,140 starred repos (snapshot `2026-09-12T16:25:05.965Z`). Regenerate any time — no API cost.

A stump base is the textbook case for the implicit/SDF route: the form is organic and irregular (where code-CAD is painful), it needs no support (it is its own flat base), and SDF output is watertight by construction — so the repair layer never runs.

## The stack this uses

| Stage | Tool | Stars | Health | Lifecycle |
|---|---|---|---|---|
| Author | [`fogleman/sdf`](https://github.com/fogleman/sdf) | 2,001 | 4 | Abandoned |
| See | [`f3d-app/f3d`](https://github.com/f3d-app/f3d) | 4,669 | 82 | Classic |
| Validate | [`mikedh/trimesh`](https://github.com/mikedh/trimesh) | 3,678 | 74 | Classic |
| Slice | [`OrcaSlicer/OrcaSlicer`](https://github.com/OrcaSlicer/OrcaSlicer) | 15,676 | 83 | Classic |

Metrics are live from the dataset. A low health score in geometry libraries usually means *finished*, not dead — see the parent report's maintenance section.

## Measure these first

No dimensions appear in the prompt on purpose. This part carries a trophy that already exists, so every size is derived from it.

| Input | What to measure | Why it drives the shape |
|---|---|---|
| `MOUNT_DIA` | The trophy's spigot, rod or foot where it meets the base | Sets the socket |
| `MOUNT_DEPTH` | How far that spigot can sink in | Sets socket depth |
| `MOUNT_TYPE` | Threaded rod / plain spigot / flat foot | Decides socket vs. through-hole |
| `TROPHY_HEIGHT` | Full height of the trophy alone | Drives footprint — tall needs wide |
| `TROPHY_MASS` | Weigh it | Decides whether ballast is needed |
| `TROPHY_COG` | Roughly how high its mass sits | Tall, top-heavy cups need more base |
| `PLATE_W, PLATE_H` | The engraving plate, if there is one | Sizes the flat facet |

## The prompt

> You are writing Python that generates a 3D-printable model using the `sdf` library
> (`fogleman/sdf`). Output a single script, nothing else. Units are millimetres.
>
> **Model: a naturalistic tree stump that serves as the base of a trophy (Pokal).**
> It is not a standalone ornament — it carries an existing trophy, and every dimension is
> derived from that trophy rather than chosen.
>
> Begin the script with an input block holding only *measured* values: `MOUNT_DIA`,
> `MOUNT_DEPTH`, `MOUNT_TYPE`, `TROPHY_HEIGHT`, `TROPHY_MASS`, `TROPHY_COG`, and optionally
> `PLATE_W` / `PLATE_H`. I will fill these in. Everything else must be **computed** from
> them, each derived value a named constant with a one-line comment explaining the rule.
>
> Derive the proportions with these rules:
>
> - **Footprint** scales with trophy height and how high its mass sits — a tall or top-heavy
>   cup needs a wider stump. Size it so the whole assembly does not tip until it is leaned
>   well past any angle a display shelf would see, and state the resulting tip angle in a comment.
> - **Stump height** is a visual proportion of the trophy, not a fixed number: tall enough to
>   read as a plinth, short enough that the cup stays the subject.
> - **Taper** narrows from base to cut face; the cut face must be comfortably wider than
>   `MOUNT_DIA` so the socket is not cutting into the rim.
>
> Build these features, in this order:
>
> 1. **Trunk body** — a tapered vertical solid with a non-circular cross-section. Modulate
>    the radius by angle, and let that irregularity change with height so no two cross-sections
>    match. It must read as a real stump, not a noisy cylinder.
> 2. **Root flare** — the lower portion swells into five or six uneven buttress roots,
>    unequally spaced and of differing sizes, blended into the trunk with a smooth union
>    (`k=` roughly 4–6) so there is no seam. Roots widen the footprint, so account for them
>    in the stability calculation rather than treating them as decoration.
> 3. **Bark** — vertical ridges over the full height, irregular in spacing and depth, broken
>    by a second finer noise so they do not look striped. Relief must be at least 0.8 mm
>    peak-to-valley or it will not survive 0.2 mm layers.
> 4. **Cut face** — flat, level, perpendicular to Z, with a slightly ragged outer edge where
>    the bark meets it. Cut concentric growth rings into it, irregularly spaced and off-centre,
>    0.6 mm wide and 0.4 mm deep, with two or three fine radial cracks. **Keep the rings clear
>    of the socket** — they should read as wood around the mount, not run into it.
> 5. **Mount socket**, centred on the cut face, according to `MOUNT_TYPE`:
>    - *plain spigot* — a blind socket, `MOUNT_DIA` plus 0.3 mm diametral clearance, depth
>      `MOUNT_DEPTH` plus 1 mm so it seats on the shoulder and not the floor.
>    - *threaded rod* — a through-hole with the same clearance, opening into a hex or
>      cylindrical recess in the underside deep enough to take a nut and washer.
>    - *flat foot* — a shallow register recess matching the foot outline with 0.3 mm clearance,
>      so the trophy locates instead of sliding.
> 6. **Nameplate facet** — if `PLATE_W` is set, flatten one area of the bark into a smooth
>    planar facet a little larger than the plate, tilted slightly upward toward a viewer.
>    It must be genuinely flat so the plate sits without rocking, and must not cut so deep
>    that it breaks into the interior.
> 7. **Ballast cavity** — if `TROPHY_MASS` is large enough to matter, hollow the interior
>    from the underside into a cavity for sand or steel shot, leaving walls of at least 3 mm
>    and keeping the cavity clear of the socket and the nameplate facet. Ballast is far more
>    effective than infill for stability because it sits low. If it is not needed, say so in
>    a comment and skip it.
> 8. **Underside** — perfectly flat at z=0, guaranteed by intersecting with a half-space,
>    with a shallow recess inset from the edge to take a felt pad.
>
> **Hard printability constraints — these override aesthetics:**
>
> - Nothing may overhang more than 45° from vertical. The root flare is the risk: keep its
>   underside sloping outward and down to the base, never undercutting.
> - Minimum wall and minimum feature 0.8 mm. No knife edges.
> - One connected solid, no floating geometry.
> - Print orientation is cut-face-up, as modelled — do not design anything that assumes supports.
> - Mesh fine enough to resolve 0.4 mm detail: pass `step=0.25` to `save()`.
>
> Expose every noise seed and ridge parameter as a named constant so the shape can be
> re-rolled without touching the body of the code.
>
> Save to `stump_base.stl`. After saving, print the bounding box, the volume, the computed
> footprint and the tip angle, so I can check the derivation before printing.

## Variants

Append one of these:

- **Multiple places** — "Make the cut face a stepped tier with sockets at different heights for first, second and third place."
- **Broken stump** — "Replace the sawn top with a splintered break, the socket set into the one intact area. Keep every splinter above 45° from horizontal."
- **Integrated plate** — "Instead of a facet for a metal plate, emboss the engraving text directly, raised 0.6 mm on a flat panel, and expose the text as a constant."

## Verify before you print

```bash
# generate
python3 stump_base.py
```

```bash
# assert on the geometry
python3 -c "
import trimesh; m = trimesh.load('stump_base.stl')
print('watertight:', m.is_watertight)
print('winding ok :', m.is_winding_consistent)
print('euler      :', m.euler_number)
print('volume cm3 :', round(m.volume/1000, 1))
print('centre of mass:', m.center_mass.round(1))
"
```

```bash
# look at it
f3d stump_base.stl --output=view.png --camera-direction=-1,-1,0.4
```

`is_watertight` should be `True` first try. If not, the SDF has disjoint components —
usually a root lobe that floated free. Raise the smooth-union `k` rather than reaching for a
repair tool; fixing it at the source keeps the guarantee that made this route worth choosing.

**Test the socket before printing the whole thing.** Slice a 10 mm tall disc containing just
the socket and print that first — a clearance that is wrong costs minutes there and hours on
the full base. FDM shrinkage varies enough between filaments that 0.3 mm is a starting point,
not an answer.

Then show the render and the trimesh numbers back to the model and iterate. That loop, not
the first generation, is where the shape gets good.

<sub>Generated by `scripts/prompts/stump_base.py` · parent report: `3d-printing-stack`</sub>

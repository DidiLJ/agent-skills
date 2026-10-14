---
name: tripo-asset-kit
description: 'Produce a 3D game asset AND its separated parts (construction kit, vehicle parts, destructible pieces) with Tripo Studio from a tight exploded-view reference image, then inspect, prepare, optimise and integrate it in a game engine (Godot-oriented: mobile budgets, one material, real scale, destruction-ready parts). Use for any building, building kit, vehicle or multi-part prop made with Tripo, in any project, and before touching Tripo exports.'
---

# Tripo asset + kit from an exploded view

General method (any project, any agent). Project paths and tool names below are examples from one reference implementation: use the equivalent tools of your project (see its agent instructions) and adapt the paths and budgets.

Status (14 Oct 2026): the account owner's chain is **Smart Mesh, Quad, 4 polycounts, Segment Simple, Smart UV, Texture 8K** (section 3); the earlier HD Model route below was validated on 10 Oct and stays the fallback. Status (10 Oct 2026): method validated on two assets (car: 17 parts, 21 193 triangles; building: 10 parts, 20 188 triangles), both prepared and merged, then run end to end on a kit pavilion (17 expected parts -> 17 parts, 19 973 triangles, 1 material; full chain 130 credits: generate 60 + retopo 40 + fill 0 + texture 30). Steps marked **(to complete)** still need a measured run; update this file with the numbers when you get them.

Read first, if the project has them: its lessons file (asset import and physics sections), its modular-building practice sheet, its asset pipeline and Tripo workflow documents.

## Hard rules
- Tripo runs in a browser session already logged in to Tripo Studio, in your own tab. Only the lead agent, or an agent explicitly delegated by the account owner. Never touch the user's other tabs.
- **Check the upload path first.** The reference image must reach Tripo's file input. Browser automation with a real file-upload call (e.g. Claude in Chrome `file_upload` with a local path) works. Some embedded agent browsers cannot: they do not let the agent drive the native file dialog, they block requests from a public page to `localhost`, and a synthetic Ctrl+V fires no paste event (all measured 14 Oct 2026). Test one upload before preparing a batch, and do not open public tunnels or other workarounds: use a browser that can upload, or ask the account owner.
- Read the credit quote on the button and the balance before every click. Stop if the balance would go below the credit floor set by the account owner (example: **10 000**). Log every spend and every export in a ledger file next to the raw exports (e.g. `<raw assets folder>/tripo/LEDGER.md`). Privacy **Private** on every generation.
- Provenance for every committed asset: source (who made it, tool, date, method, settings), SHA-256 of the source and of every prepared file, licence line. Git LFS for glb/png/jpg. Follow the project's content and licence rules (e.g. SFW store builds; some tools have licences that exclude regions or uses, such as Hunyuan endpoints for EU users or SMPL-based tools: check before using one).
- Masters (4K/8K exports, raw Tripo files) stay outside git in a raw-assets folder (e.g. `<raw assets folder>/tripo/exports/`).

## 1. Design the asset for the game before drawing it
- **Building kits:** every wall module is exactly one bay of **3.0 m wide x 3.2 m tall** (aspect about 0.94), wall 0.3-0.4 m thick, separate corner pieces, one roof slab, parapets per side. Simple shapes give the cleanest parts. A first test building had bays 1.35-1.6 times wider than tall: its footprint fits the grid but its walls do not cut into 3 m modules. Design the bays, do not fix them afterwards.
- **Vehicles:** only one good instance of each symmetric part is needed (best wheel used 4 times, best door mirrored). The central body must be right. Hidden or open parts (trunk shown open, interior) are replaced later; plan for it.
- Write the expected part list (name, count, size on the grid) before generating: it is the acceptance list for every later step.

## 2. Exploded reference image (Codex)
- **Two prompts from the account owner (14 Oct 2026)**, both run on ONE reference image of the whole asset (a full building, vehicle or prop, ideally a three-quarter view):
  - `references/prompt-kit-sheet.md`: a construction-kit sheet with exactly ONE instance of each unique module (walls, corners, walls with openings, roof sections, columns, standalone features), spaced on a plain neutral background, no annotation. For reusable modular kits: every module is generated once and reused by instancing.
  - `references/prompt-exploded-spacing.md`: the same asset as an exploded assembly with clear gaps (about 4-6 % of the asset width) along the natural assembly directions, recognisable at a glance. For a specific building or object that must be reassembled exactly.
  - Compare both on the same reference before a batch (part count, uniqueness, fidelity, separation measured as below). The verdict and the measured Tripo result go in the project's notes and here.
- Tool: skill `codex-imagegen` (`gen.sh`). Prompt structure: `references/prompt-template.md`. Ultra photorealistic photograph wording; never write "3D model", "texture" or "render".
- **Tight exploded view, read as ONE object.** Each part moves only a short distance outward along its own normal (gaps about 4-6 % of the assembled width), roof lifted straight up, translation only, nothing rotated toward the camera, one shared orthographic 3/4 camera, same scale. With the HD Model route (Generate in Parts), never a parts sheet, rows or a catalogue, never spread the parts afterwards: a widely spaced image was read as several objects and only one was generated (measured twice on 10 Oct: exploded car -> central shell only; 12-module sheet -> one module). The kit-sheet prompt with the Smart Mesh + Segment chain is still to be measured **(to complete)**.
- Transparent background, no glow, halo, text, arrows or shadow; empty window and door openings (no glass), no interior, no floor.
- Generate 2-4 variants, open each at full size. Count parts: binarise the alpha and count connected components (must equal the expected part count; fewer = parts touching or hidden). Smallest gap in px. For kits, measure the front bay aspect.
- Codex "transparent" output: subject alpha 250-254 (never 255) and 12-21 % of pixels partially transparent, also inside parts. Clean with a short PIL script (alpha < 128 -> 0, rest 255, edge colour fixed) that does **not** spread the parts apart (no `--spread`-style option). The Read tool ignores alpha: judge transparency with PIL, view on a grey composite.
- Commit the chosen raw + cleaned image and a `.prompt.md` (tool and version, date, full prompt, reference SHA-256, output SHA-256, licence "generated, OpenAI terms") under the project's art-reference folder (`.../art/refs/<category>/`).

## 3. Tripo Studio pipeline
Copy the upload file into the session scratchpad first. Workspace `https://studio.tripo3d.ai/workspace/generate`.

Account owner's chain (14 Oct 2026):

| Step | Settings | Cost seen |
|---|---|---|
| Generate | Model > **Smart Mesh**, single image (the chosen reference), Topology **Quad** for everything that is not a human or rigged character (Triangle only for those), **Number of Generation 4**, Customize Poly Counts **500 / 5 000 / 10 000 / 25 000**, Privacy **Private**, AI model **P2.0** | 100 credits seen on the button for 4 generations |
| Choose | Open the four results and keep the **lowest** polycount that still looks right at the game's viewing distance; take a higher one only where the low one loses visible detail | 0 |
| Segment | Segment mode **Simple** (fastest cut into parts); check the part list against the expected module list | to record |
| Smart UV | Run **Smart UV** for clean UVs; download the clean UV file if the project repaints or bakes | to record |
| Texture | The **same** reference image(s) used for the generation, **Remove Lighting ON** (clean albedo for dynamic lighting), resolution **8K** (master; optimise at integration) | to record |
| Export | GLB, file name = asset id; masters stay outside git | 0 |

Previous route (HD Model, validated 10 Oct 2026; fallback when the chain above fails):

| Step | Settings | Cost seen |
|---|---|---|
| Generate | Model > **HD Model**, single image, **Generate in Parts ON** (Simple 3-6 / Balanced 6-15 / Detailed 15+ parts; the label is a hint, Simple returned 17 parts on the car), Geometry & Texture: **Ultra Mesh Quality ON, AI Complete ON, Texture OFF, Triangle, polycount max (2 000 000)**, 8K Texture OFF, Privacy **Private**, AI model **H3.1 Best Quality** | 60 credits |
| Retopo | Topology **Quad** for non-rigged assets (buildings, props, vehicles), Triangle if it will be rigged; Smart Mesh P1.0 ON; Polygon Count 10 000 (max) gives about 20 000 triangles for the whole asset; the part list is kept | 40 credits |
| Fill Parts | Segment > Fill Parts, Complete Mode **Quick Cap** ("quick completion"; AI Completion is the other mode), button Part Completion, about 80 s | free |
| Texture | the reference image is pre-filled (keep the **same** exploded image), Texture Style None, **Remove Lighting ON** (clean albedo for dynamic lighting), resolution 8K (master) | 30 credits |
| Export | GLB, **Pack UV ON** (one material, one atlas instead of one texture set per part: car 1 material + 3 maps instead of 17 materials + 51 maps), texture resolution **4K** (8K is "Current"; 4K is enough as a master), file name = asset id | 0 |

- Smart UV is part of the account owner's chain (14 Oct 2026). On the HD route, Tripo's texture step already made the UVs.
- Export mechanics: Chrome downloads to `Downloads/Unconfirmed NNNNNN.crdownload` (the name is localised, e.g. "Non confirmé" on a French browser; the save dialog is invisible). Wait until its size is stable, copy it to `exports/<asset>.glb`, check the glTF header (`glTF`, version 2, length = file size). Pack UV makes the export 30-60 s slower.
- Measured on the kit pavilion: bays came out about 15 % wider than tall (1.15 for 0.94 asked) although the reference measured about 0.9; ask for slightly TALLER bays in the image than the target.
- After each Tripo step, look at the part list and the viewport before paying for the next one; stop at two failed attempts on the same part and fix in Blender instead.
- Measured nine-asset test (10 Oct): **4K texture + Remove Lighting costs 20 credits**; the eight native-generation Pack UV exports have one material and two 4096 maps; the locally reduced/reimported coupe has one material and one 4096 albedo map. Wait for the processing indicator to disappear and for the expected geometry/topology to be active before starting the next operation: enabled navigation alone is not completion.
- **Quick Cap can close intended openings or create spikes** (desk, boutique, van measured). Inspect the openings and the rear after completion; restore the previous version when damaged, and repair locally instead of repeatedly applying automatic completion.
- Part-count labels are only hints: Simple returned 9,20,23,24 and32 parts on the new buildings/vehicles. Extra trim must be attached to its parent before calling the kit ready. A uniform local decimation damaged coupe wheels at about20k total; preserving8000tri per documented wheel gave44830tri with their silhouettes retained. This is a prototype result, not a mobile budget certification.
- **Rollback through History:** if a new generation, retopo, completion or texture result is inconclusive or deformed, open the viewport's **History**, select the last sound version, inspect it, then use **Restore & Edit** to make it the working version. Selecting a thumbnail only previews that version. Keep evidence of the rejected result and record which step failed; do not pay for the next step until the restored geometry is checked.
- **Delete parts in Segment:** individual unwanted parts can be deleted directly from their part-row menu in the **Segment** section. Identify the part in the viewport first, preserve a recoverable version/export, delete only the confirmed unwanted part, then verify the remaining part count and geometry. Do not delete a required wall, roof, wheel or symmetric counterpart merely because it is hidden from the current camera.

## 4. Inspect the export
- If the project has an inspection script: `blender -b --python-exit-code 1 -P <project>/tools/tripo_inspect.py -- <glb> --output-dir <dir>` (metrics + four neutral renders). `blender` comes from PATH or from the project's agent instructions.
- `blender -b --python-exit-code 1 -P <skill folder>/scripts/analyse_parts.py -- <glb> <out_prefix>`: per part triangles, **welded** components and open edges, image sizes, two textured renders. GLB vertices are split along UV seams: without welding every part looks open (thousands of false open edges).
- Accept when: part count matches the expected list (or the extras are trivial), each part is one welded component, open edges per part small (0-30) and explained, one material, textures present.

## 5. Prepare for the game
Common to every asset:
- Labelled capture of every part (name -> role, kept or rejected and why). Keep the best of each symmetric set; mirror copies and flip faces/normals, check bounds are exactly opposite.
- Real scale: Tripo normalises to about 1 m. Choose the factor from a known size (door 2.0-2.2 m, tyre 0.70-0.73 m, kit footprint on whole bays) and justify it in the report. Pivots per the target contract.
- One material, textures imported VRAM-compressed with mipmaps and `size_limit = 2048` (set `compress/mode=2`, `mipmaps/generate=true` in the `.import`, then re-import). Import the game project with your headless Godot import step (the project's import script if it has one), never two Godot imports at once.
- Never decimate the GLB as imported: weld first (`remove_doubles`), then decimate, then clamp the shape back if the decimation inflated it (wheel radius +5 % measured).
- `asset.json` / manifest with provenance and hashes; reproducible preparation script committed next to the asset (rerun it: identical output).
Vehicles (example files kept next to the asset: a `prepare_<asset>.py`, `label_parts.py`, `extract_textures.py` and an `<asset>.assembly.json`):
- Put parts back from the exploded positions by measured offsets, verified on front/side/top renders. A part generated open (trunk at 62°) cannot be fixed by rotation: build a simple panel that samples a flat colour area of the same atlas.
- Body parts stay separate `MeshInstance3D` (future damage); one wheel `Mesh` on the four `VehicleWheel3D`, hub at origin, radius read from the mesh; collision = simple boxes, never the visual mesh; mass and centre of mass plausible. Jolt: `jolt_physics_3d/simulation/continuous_cd_max_penetration = 0.05` kept a 4.4 m car out of 5 cm walls at 30 m/s.
- Budgets measured: car 15 251 triangles after wheel decimation (research target 9 000, still above), +16 draw calls without shadows, +37 with the sun shadow pass (limit 20): merging parts that never get damaged is the next lever.
Buildings and kits (example conventions from one project: pivot bottom-left back, facade +Z, external 2048 textures, one `asset.json` per module, a per-asset check script):
- Tripo parts of one generation do not match exactly (rear wall 10 % longer than the front, roof 23 % short on one building): measure every side, close the ring joint to joint, report the residuals; deform height only, at most 15 %.
- Keep zero-area triangles (they close T-junctions); count open edges after welding.
- Cut a module only on a bay boundary and only if the cut is clean; otherwise keep it whole and say so.
- Pavilion kit 4 x 2 bays (17 parts = 6 module types, measured 10 Oct 2026):
  - Bay width exactly 3.000 m needs a plan factor per type (17.10-18.25, 7 % apart). Height-only stretch to the storey: +6-10 % at 3.0 m (door +16.9 %) vs +14-25 % at 3.2 m: pick 3.0 and record both in the manifest. Door opening 1.25 x 2.18 m, window 1.14 x 1.57 m.
  - Bounds lie: 12 collinear zero-area triangles stretched the roof box by 1.68 m (12 %). Use the extent of non-sliver triangles (area / longest edge^2 >= 1e-5), trim stray slivers outside it, fail the check if box - drawn extent > 1 mm.
  - Flush boxes (gap 0.000 mm) are not closed joints: bay ends are stepped, the wall body stops 59-70 mm short (pier shaft 138-143 mm), a 12-25 cm see-through slit per seam. Shoot rays through each seam at +/-1 mm (886/928 leaked); fix by moving the end-zone vertices onto the box plane (monotone, box unchanged): 0/928.
  - One pier mesh for four corners: make it square (separate x/depth factors), close its two inward faces, rotate yaw 0/90/180/-90.
  - Budget: 17 instances = 17 draw calls (no batching in Compatibility), 43 with the sun shadow, 19 475 triangles instanced, 8 931 unique, 6 meshes. Check that the Python used for texture scripts has numpy (a system Python may not).

## 6. Destruction readiness (to complete)
- Keep every part a separate node and record its role (`Body_DoorL`, `baie-fenetre`...): it is the unit that detaches or fractures.
- Building modules go through the project's destruction pipeline (cells, load model, body caps); vehicle parts detach through the same admission queue. Document the integration here once it is done in your project.

## Measured drone test (10 Oct 2026)
- H3.1 HD Simple produced **9 meshes** for the planned **5 functional modules**: body + four arms + four complete rotor units. Keep each arm/rotor pair under one module parent; the GLB still contains 9 meshes, not 5.
- Raw export: 10 532 triangles, 1 material, two 4K maps; prepared assembled/kit: 9 529 triangles, 1 material, two 2K maps, 0.60 m prototype span. Total quoted Tripo cost 120 (60+40+20), export 0.
- Check the **underside**, not only front/top: automatic completion retained a lower closure. First partial removal was rejected; the corrected empty shell passed 9 upward ray checks. Identify the actual closure on the specific mesh; do not apply a global deletion heuristic to other assets.
- Assembled/kit BIN data identical; only four module translations differ within numerical tolerance. Final PNG proofs use true alpha, 60-degree elevation, shared camera and scale per view. Godot/phone/CAD qualification remains unverified.
## 7. Verify and report
- Lab or game checks green (exact tokens), new asset check with a negative case, real-renderer captures at 2400x1080 opened by you (3/4 front, 3/4 back, in use), then build the APK and test it on a real phone.
- Report: expected vs obtained parts, credits spent (ledger lines), triangles per part and total, draw calls, texture VRAM, scale factor and why, what is not verified (phone, Web), and a lessons-learned section. Update this skill with every new measured fact.

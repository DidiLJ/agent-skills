---
name: codex-imagegen
description: 'Generate raster images (game icons, UI mockups, textures, concept art, sprites, transparent cutouts) through the OpenAI Codex CLI''s built-in image_gen tool, then retrieve and inspect them yourself. Use whenever a task needs an AI-generated bitmap, the user asks for an image, a visual mockup or an icon, or another agent without an image tool (e.g. a Devin agent: the Devin CLI has no image tool, tested 2026-10-06) needs images. Do not use for vector/SVG or code-drawn visuals, or to edit an existing editable source asset.'
---

# Codex image generation

Some agent CLIs (e.g. the Devin CLI) cannot create images. The Codex CLI (`codex`, on PATH) has a built-in `image_gen` tool
that runs on the ChatGPT account signed in to Codex (`codex login`; no `OPENAI_API_KEY`). You drive it non-interactively, then read the PNG
with your own image viewer (the Read tool) and judge it. Never present an image you have not opened.

## Generate

```bash
bash <skill folder>/scripts/gen.sh "<prompt>" <out.png> [reference.png ...]
```

- **Edit an image:** `gen.sh --edit "<only what to change>" <out.png> <image-to-edit.png> [more refs]`. Codex
  changes only the named part (a button colour, a character's outfit, a background) and keeps the rest.
- **Combine references:** pass several images without `--edit` and say how to combine them ("the layout of image
  1 with the palette of image 2 and the icon style of image 3").
- **Iterate from a game capture:** pass a real screenshot of the game as the image to edit to get a redesign
  proposal of that exact screen, which is the fastest mockup for UI pre-validation.
- One call = one image, about 90 s. Run several calls in parallel (background) for variants.
- The script runs `codex exec` in a temporary folder with `-s workspace-write` and low reasoning, tells Codex to use
  the built-in tool only, then copies the newest PNG of that thread from `~/.codex/generated_images/<thread>/`
  to `<out.png>`. It prints the path, or `NO_IMAGE` with the log paths (`<out>.codex.jsonl`, `.codex.err.txt`).
- Reference images (style, composition) are passed with `-i`.
- MCP connection errors in the `.err.txt` (e.g. 127.0.0.1:8288) are Codex's own MCP servers failing: harmless.

## Measured (2026-10-06)

- Output 1254x1254 PNG. RGB on a plain background; "transparent background (real alpha)" gives RGBA with true
  alpha 0-255.
- About 200k input and 700 output tokens per call (Codex's startup context), on the ChatGPT plan quota.
- Style words are interpreted: "thin gold line art" came back flat line art on a solid background, but the same
  words with "transparent background" came back as a rich embossed 3D medal. State the rendering explicitly
  ("flat 2D vector style, no shading, no bevel") when it matters, and generate 2-3 variants.

## Uses

- **Mockups before any UX/UI implementation:** 2-3 variants, inspected, shown to the user for pre-validation,
  then handed to the implementing agent as reference images.
- **Real assets:** UI icons and ornaments (transparent PNG), textures (ask for "seamless tileable", then check
  the tiling by placing 2x2 copies side by side), decals, posters and signs inside the game world, character
  portraits, item sprites, concept sheets and orthographic front/side views that guide 3D modelling. A 3D
  model itself is not produced here: images only feed the modelling pipeline.
- **Transparency:** "transparent background (real alpha)" gives an RGBA PNG with true alpha.
- Game assets still follow the project rules: provenance, licence line, Git LFS, the project's content rules.

## Prompting

Write the prompt as a short spec: use (game UI icon, texture, mockup), subject, style and rendering, palette
with names and hex codes (e.g. deep red #8a1c2b, warm gold #c9a14a), background (plain colour or transparent), framing
(centered, square, margin), and constraints (no text, no watermark, no logo of a real brand). One subject per
image. For an icon family, generate one master, then pass it as a reference image for the others.

## References for 3D asset generation (image-to-3D, e.g. Tripo)

These rules apply ONLY to reference images that feed a 3D generator (characters, monsters, outfits,
accessories, weapons, furniture, building parts). They do NOT apply to UX/UI mockups, icons, textures or
any other professional design work, where the normal prompting above stays the rule.

- Describe the subject entirely in text and ask for an **ultra photorealistic photograph**; never write
  "3D model", "texture", "render" or "game asset style": the 3D generator inherits the realism of the image.
- Multi-view input: each view (front, side, back...) is a SEPARATE image file;
  never put several views of the same asset in one image. Keep identity with `--multi` (Image 1 first,
  then the other views using Image 1 as reference) or, for characters, a seed-locked workflow (e.g. a RunningHub workflow with
  the same seed).
- Avoid attaching a photorealistic face as reference for new views of a person: the content filter may treat it as a
  real person and refuse. Say the reference is an AI-generated image made for asset creation.
- The output filter can refuse a prompt that passed before: retry up to 3 times, then report. Never seek explicit content.
- Several views in one call: `gen.sh --multi "<prompt asking for N separate images>" <out.png>` copies every
  image of the thread to `<out>-1.png ... <out>-N.png`; a 3-view prompt asks for Image 1 first, then
  Images 2 and 3 using Image 1 as reference (same character, only the orientation changes).
  `GEN_LOG_DIR=<dir>` keeps the Codex logs out of the asset folder.
- Transparent background: every reference image for a 3D asset asks for a
  "transparent background (real alpha)" instead of a studio backdrop, so the 3D generator does not turn the
  backdrop or floor into geometry, texture or segments. Check the alpha after generation.
- Buildings and building modules: window and door openings are EMPTY see-through
  holes showing the plain studio background (no glass, frame, door leaf or interior). Window/door inserts are
  generated separately (frame + glass only, no wall), orthographic front view. Glass on other objects: plain
  uniform dark glass with nothing behind it.
- Outfits: dress the base model and ask for clearly separate garments (top, bottom, shoes) so the 3D tool can
  cut each piece.

## Rules

- Never `--dangerously-bypass-approvals-and-sandbox`, never `-s danger-full-access`.
- Never the CLI/API fallback (`scripts/image_gen.py`, needs a paid API key) without the user's approval and cost.
- Content rules of the project apply (e.g. SFW store builds, no real brands, no real people).
- Provenance for every image kept in a project: tool `Codex CLI <version> built-in image_gen`, date, full prompt,
  reference images, SHA-256 of the file. OpenAI terms assign the output to the user [Probable]; record
  "generated, OpenAI terms" as the licence line.
- Keep generated images out of the repo until chosen; commit only the selected ones (Git LFS covers png).
- Inspect every image at full size before using or showing it: subject correct, no text artefacts, alpha clean
  at the edges, readable at the target size (downscale a copy to the real UI size, e.g. 48 px, and look again).

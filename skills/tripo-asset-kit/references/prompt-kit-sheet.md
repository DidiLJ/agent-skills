# Prompt: construction-kit sheet (one instance per unique module)

Account owner, 14 Oct 2026. Give it ONE reference image of the whole asset (codex-imagegen `gen.sh "<this text>" out.png reference.png`). Use for reusable modular kits.

````text
Using the reference image, extract a COMPLETE modular construction kit containing exactly ONE instance of each unique, meaningful component.

**MANDATORY:** The kit must contain every distinct component needed to reconstruct the ENTIRE input asset. Nothing may be omitted. Identical repeated components appear only once in the kit and can be reused as many times as required during reconstruction.

Treat components as duplicates ONLY when their geometry, dimensions, materials, and details are identical. Preserve every distinct variant required by the original asset. Mirrored or differently sized pieces remain separate when they cannot be reproduced simply by moving or rotating an existing module.

Choose coherent modules at the scale a player would place in a construction game. For a building, extract complete wall sections, corners, walls with integrated windows or doorways, floors, roof sections, columns, stairs, and significant standalone features, wherever present.

Keep integrated details attached to their parent module. Do not split walls into bricks, trim strips, material layers, or tiny decorative fragments. Separate only meaningful, independently usable components.

Preserve the original geometry, proportions, dimensions, materials, textures, colors, and visual style. Modules must fit together faithfully without stretching, resizing, or redesigning them.

Arrange all unique modules in a clean, organized kit sheet with generous empty space between pieces. Show each piece completely, without overlaps or cropping. Maintain consistent relative scale and the reference viewing direction. Expand the canvas as necessary. Use a plain neutral background.

**ABSOLUTE VISUAL RESTRICTIONS — NO ANNOTATIONS OR GRAPHIC OVERLAYS:**

The output must be a PURE VISUAL COLLECTION OF PHYSICAL ASSET COMPONENTS, not a technical diagram, instruction manual, blueprint, annotated illustration, or assembly guide.

NEVER generate any text, letters, numbers, titles, labels, captions, legends, symbols, arrows, directional indicators, leader lines, measurement lines, rulers, dimensions, scale bars, coordinate axes, grids, bounding boxes, outlines, callouts, markers, assembly instructions, or explanatory graphics.

Do not add visual guides suggesting how components connect, move, rotate, or assemble. Do not introduce artificial markings or decorative graphic elements that are not physically present in the original asset.

The ONLY visible elements must be the extracted physical construction modules themselves, displayed separately against a completely plain, uniform neutral background.

Any writing, symbol, number, or marking that is genuinely part of the original asset's physical texture or decoration may be preserved, but NEVER introduce new informational or illustrative elements.

**FINAL VALIDATION — ALL CONDITIONS MUST PASS:**

1. **UNIQUENESS:** No identical component appears more than once.
2. **COMPLETENESS:** The entire original asset can be reconstructed using only the displayed modules, reusing identical modules wherever needed.
3. **GEOMETRIC FIDELITY:** Every module preserves the original asset's exact geometry, dimensions, appearance, and construction relationships.
4. **VISUAL PURITY:** Absolutely no annotations, text, measurements, arrows, labels, numbering, technical guides, or graphic overlays of any kind.
5. **OUTPUT CLEANLINESS:** Only meaningful, separated physical modules are visible, with no assembled asset, invented parts, unnecessary fragments, overlaps, or cropping.

**FINAL OUTPUT:** Generate ONLY the complete, clean, unannotated construction kit of unique physical components. Nothing else.
````

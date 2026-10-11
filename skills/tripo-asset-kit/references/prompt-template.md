# Exploded-view reference prompts (Codex `gen.sh`)

Structure proven by tests with Tripo exploded views. Fill the `<...>` parts. Keep one prompt per image; pass the assembled references of the asset with `gen.sh ... <out.png> <ref1.png> <ref2.png>` and say they are identity references that may be imperfect.

## 1. Generation prompt

```
Generate ONE SPATIAL EXPLODED AXONOMETRIC DIAGRAM of <asset: e.g. a simple rectangular one-storey pavilion / the same compact two-door sedan as the reference images>.
NOT a parts sheet, NOT an inventory, NOT rows of parts, NOT a catalogue. The image must read unmistakably as ONE <asset> whose neighbouring components have moved a short distance outward from their assembled positions.

Use a virtual 3D scene with the <asset> centre fixed at the origin. First reconstruct the assembled <asset>. Then separate exactly these parts:
<numbered part list with counts and sizes, e.g.
 - 4 front wall bays: 1 door bay, 2 window bays, 1 plain bay, each 3.0 m wide x 3.2 m tall x 0.35 m thick
 - 4 corner pilasters, 0.5 x 3.2 x 0.5 m
 - 1 parapet run per side, attached to nothing
 - 1 flat roof slab>
Each part keeps its own attached trim and details; do not invent extra parts, do not merge parts, do not duplicate any part.

CRUCIAL SPATIAL LAYOUT:
Move every part along its own outward normal by the SMALLEST distance that leaves a clearly visible gap, about 4-6 percent of the assembled width. Neighbouring parts must still trace the assembled envelope. Lift the roof (or top part) straight up above the same centre, no horizontal shift, with a clear gap below it. Translation ONLY: no rotation, mirroring, resizing or deformation. Reverse the translations and the <asset> reassembles exactly. Nothing is copied underneath the detached parts; no central body, no floor, no platform.

One shared ORTHOGRAPHIC camera at FRONT-RIGHT, about 30 degrees from the front, looking down about 40 degrees. Front = -Y, right = +X, up = +Z. Never rotate a part to face the camera: far parts show their real back or edge.
Every part shares ONE physical scale and matching edge dimensions.

<style line: ultra photorealistic photograph of <materials and colours>, e.g. pale stone with dark metal trim / deep blue metallic paint>, soft even studio lighting, consistent illumination.
EXCLUDE ground, plinth, floor slab, interior rooms, furniture, machinery. No glazing: window and door openings are EMPTY and see-through.
GENUINE transparent RGBA background and empty gaps; no gradient, no painted checkerboard, no glow, no bloom, no halo, no shadow, no text, arrows, labels, numbers or outlines. Expand the canvas so nothing is cropped, with margins.
```

## 2. Correction pass (edit the best variant, change only the spacing)

```
Keep EXACTLY the same parts, geometry, materials, camera and orientations.
Change ONLY their separation distances: move every part a little farther outward along its existing normal, leaving a clearly visible gap of about <5> percent of the assembled width between neighbours, no touching, no shared trim. Lift the roof a little higher so every part below is fully visible.
Use a larger transparent canvas if needed. No resizing, rotation, new cuts, regrouping, new parts, duplicates or missing parts. No glow, no shadow, no text.
```

## 3. Checks before Tripo
- Connected components of the binarised alpha = expected part count.
- Smallest gap visible (a few px is enough for Tripo to see the cut; a gap so wide that parts float apart is the failure case).
- Kit bays: front bay width / height close to 0.94 (perspective-corrected roughly).
- Cleaned copy: alpha only 0 or 255, nothing opaque on the canvas border.

---
name: human-quality-gate
description: Audit every rendered UI, visual, slide, or content view end-to-end before delivery, combining Impeccable passes, senior UX/UI direction, factual checks, and anti-AI-slop copy review.
metadata:
  short-description: Verify every view before shipping
---

# Human Quality Gate

Use this skill whenever a task delivers a UI, visual composition, slide deck, social asset, page, component, or public-facing copy. It is a delivery gate, not a suggestion to inspect only a representative example.

## Non-negotiable outcome

Do not deliver while any view has an actionable defect. Inspect every rendered view/state in scope, then re-render the complete set after fixes. A clean code test or a good example does not clear the rest of the set.

## Fail-closed visual evidence rule

This gate is invalid unless the agent has actually opened every final rendered view at full resolution. A test result, DOM measurement, contact sheet, file listing, or verbal description is not visual evidence.

- For every slide, route, breakpoint, state, and device frame in scope, call a real image/viewer tool (`view_image`, the official integrated Browser screenshot, or the equivalent visual surface) and inspect the returned pixels. Use one evidence entry per view; do not count a contact sheet as inspection of its children.
- Inspect the complete frame, then zoom/read the dense regions: headers, cards, KPI labels and values, table rows, badges, footers, CTAs, counters, and every edge. A view is not checked because its center looks correct.
- After any edit, invalidate every previous visual conclusion. Re-render the entire matrix and reopen every final image again. A stale screenshot, cached Browser tab, previous output directory, or pre-edit hash cannot satisfy the gate.
- If a view cannot be opened at full resolution, mark the gate **blocked** and do not claim completion. Never downgrade missing visual evidence to a warning.
- The final report must name the exact evidence path/URL for every view and state the number opened versus the number required. If the counts differ, the gate fails.

## Human-common-sense hard stops

The following failures are blockers for any interface, component, page, screen, document, visual composition, or public-facing content, even when automated geometry tests pass:

- **Avoidable metadata wrapping:** when related labels, status indicators, filters, tags, or compact controls fit in one row at the target width, keep them in one clear ordered group. Do not split a coherent information cluster merely because the stylesheet permits wrapping.
- **Unused available space:** content-dense views must use their available space intentionally. Lists, grids, tables, cards, and detail panels should expand, breathe, or re-balance into safe remaining space instead of leaving a conspicuous empty region. A fixed `min-height` or a green overflow test is not proof of good composition.
- **Balanced KPI rows at every breakpoint:** reject cards/KPIs stretched into large empty surfaces and any row with an orphan item or conspicuously unused grid track. At intermediate widths, change the column count or span the final cards so a partial row uses the available width; use one row only when every label and value remains legible. Retain whitespace only for a demonstrated reading, grouping or interaction purpose, or an explicit user decision.
- **Interaction over the whole surface:** test mouse-wheel and touch scrolling while the pointer is over diagrams, charts and embedded canvases, not only beside them. Noninteractive diagrams must not capture the page's scroll.
- **Visible affordance:** every filter, disclosure, toggle, or other actionable control must look actionable before activation through a clear button or link surface, an appropriate icon or caret, and visible hover/focus/expanded states. Native `<summary>` text styled like ordinary body copy is insufficient even when it remains keyboard-accessible; verify the cue with mouse, touch, and keyboard.
- **Information semantics:** every reference, provenance, metadata, or explanatory block must expose a human-readable origin, category, identifier, title, or consequence. Reject database-like concatenations, duplicate blocks, orphan identifiers, and labels that require the original page or developer knowledge to understand.
- **Opaque official references:** preserve the exact source identifier, but identify its type and issuing body/source in the UI and pair it with meaningful context such as date or title. A technical-looking code without a label must never be left to appear as an error or stray internal data.
- **Honest feature state:** distinguish a feature that is not integrated from a verified search with no results, and distinguish both from data that exists but is not linked. Use an explicit “coming soon” state only for the first case; never describe it as an empty source or a completed search.
- **Bounded lists and complete access:** show a useful, proportionate first set for long lists, state the exact total, and provide clear pagination or expansion. Make the export scope explicit and preserve access to all intended results without loading the whole corpus into the initial page.
- **Purposeful columns:** each visible column or side rail must carry useful related content or navigation. If it has none, reflow the main content instead of reserving an empty column; do not duplicate full cards just to fill space.
- **Evidence-based affiliations and proportions:** show a group or organisation membership only when the source and dates support that relationship for the context being described. Counts (votes, ratings, responses) must match the published totals; show a denominator or proportion only when that applicable group size is verified, and keep absences distinct from recorded values.
- **Fresh-artifact identity:** record a render manifest containing the exact source/content identity, output directory, timestamp, viewport/state, and every rendered-view path. Never accept a contact sheet, cached browser tab, previous output directory, or stale screenshot as proof for a new edit.
- **Human re-open after every edit:** invalidate all prior visual conclusions after any UI, CSS, content, asset, or responsive-layout change. Re-open every final view at original resolution and inspect dense regions and all four edges again.

The visual pass is human-first: explicitly look for clipped glyphs, text touching borders, labels escaping cards, duplicated counters, inconsistent spacing, fake affordances, accidental overlays, and content that is technically inside a parent box but visibly colliding. If a normal person can see it, it is a defect even when automated geometry is green.

## Requirement-to-pixels acceptance record

Before edits, turn the user's latest requirements and unresolved earlier feedback into a short acceptance record. For each requirement, name the affected views and the visible condition that would prove it was met. Keep project-specific examples in that task's record, never in this reusable skill.

- Track `rendered`, `opened`, `inspected`, and `passed` separately. Opening an image proves only that it was opened. Do not prefill passing verdicts, copy a previous report, or generate visual judgments from a loop or a test result.
- After looking at each view, record a concrete observation about hierarchy, grouping, readability, identity, emphasis, and space usage. A generic "looks good" is not a review. Compare every requested change with its acceptance condition in the actual final pixels.
- Test space allocation explicitly: could moving a secondary element, widening a dense column, grouping related metadata, or combining adjacent sparse views improve comprehension without losing content? If yes, fix the composition. Do not merely enlarge all text or stretch empty containers.
- Check identity and meaning, not just image loading: the displayed image must depict the named entity; every number must have its unit or context; emphasis must select complete meaningful phrases and preserve the original facts.
- Verify the capture itself: exact dimensions, complete edges, no repeated tiles, missing layers, transient loading, or scaling artifacts. A faulty screenshot is not proof that the underlying view is correct or incorrect. Use a supported alternate capture method and inspect it again.
- When delivery passes through an export, conversion, download, print, or packaging step, inspect the actual resulting artifact as well as the live preview. Matching layout in the browser does not prove that fonts, images, layers, links, or fallbacks survive that step. Exercise the real production conversion path; a substitute screenshot does not validate it. Required missing resources must fail visibly instead of producing a silently incomplete deliverable.
- A failed criterion blocks that view and the final completion claim. A requirement not rechecked after a relevant edit remains unverified. Record limitations honestly; no skill can guarantee universal aesthetic agreement or replace actual judgment.

## Required workflow

1. Establish truth before editing.
   - Identify the real audience, purpose, platform, viewport/device classes, source content, and approved visual direction.
   - Separate user-facing copy from developer/operator metadata. Never expose internal validation notes, implementation labels, pipeline states, or instructions to the public unless they are genuinely part of the product experience.
   - Enumerate every view/state in scope: every slide, route, carousel page, breakpoint, empty/error/loading state, and meaningful content variant.
   - Never invent factual content, statistics, names, logos, screenshots, or affordances. Mark unresolved source data honestly.

2. Run the relevant Impeccable passes on the incumbent visual system.
   - Load `impeccable context --target <exact surface>` before a new session's work.
   - The gate covers the complete Impeccable command surface: `shape`, `init`, `document`, `extract`, `critique`, `audit`, `polish`, `bolder`, `quieter`, `distill`, `harden`, `onboard`, `animate`, `colorize`, `typeset`, `layout`, `delight`, `overdrive`, `clarify`, `adapt`, `optimize`, and `live` (with `craft` treated only as its deprecated alias). For a visual delivery or an explicit Impeccable request, route every applicable pass through the gate and record why a non-applicable pass was not run; never introduce motion, novelty, or a redesign merely to satisfy a command name.
   - Read `craft-floor.md` immediately before UI edits.
   - Run the mechanical detector once after the edit pass over all changed UI targets. Treat findings as evidence to verify, not as a substitute for visual judgment. Explain intentional exceptions.

3. Apply the senior human review to every view.
   - **Purpose:** Is the main point immediately clear to someone unfamiliar with the product? Does every element earn its space?
   - **Hierarchy:** Does a blur/squint test reveal the primary message, supporting proof, and next step in the right order?
   - **Composition:** Check alignment, grouping, spacing rhythm, density, balance, whitespace, baselines, edge padding, safe areas, and visual weight.
   - **Consistency:** Compare all views side by side for the same DA, typography, radii, borders, shadows, icon family, colors, image treatment, counters, labels, and terminology.
   - **Existing design system, element by element:** For every badge, filter, KPI, card, chart, identity row and digest, locate the equivalent component elsewhere in the product and compare the actual render. Reuse the shared component and semantic tokens; an unexplained weaker local variant fails the gate. A divergence requires a concrete user benefit or an explicit user decision, not implementation convenience.
   - **Semantic color and icon pairing:** Every badge and filter must pair its meaning with an appropriate semantic color and icon. Keep that pairing identical in summaries, filters, rows, charts and detail views, including selected, unselected and dark states. Color never replaces a readable label. Check that caller overrides do not silently remove shared colors or icons.
   - **Entity identity:** Show available verified images or marks alongside readable names, with the same fallback treatment as elsewhere in the product. An unexplained missing image is a data/import/rendering defect to investigate. Do not substitute an associated entity's image or mark without an established identity relation; acronyms alone or a tooltip repeating only the acronym fail comprehension.
   - **Honest absence and useful space:** Trace missing content back through the reader, stored data, import and official source before classifying it as an external limitation. Distinguish a missing relation from a nonexistent activity, and an import gap from a source gap. Do not reserve large permanent empty sections for data that is inapplicable or rarely related; preserve access where useful and render real related content when present.
   - **Content:** Check factual fidelity, completeness, relevance, chronology, repeated information, missing context, misleading emphasis, and source traceability.
   - **Usability:** Check reading order, scannability, touch targets, focus/keyboard order, semantics, alt text, contrast, and whether visual affordances imply an action that does not exist.
   - **Robustness:** Check long titles, missing logos, unknown groups, multiple rows, wrapping, narrow/wide layouts, localization expansion, zoom, crop boundaries, and overflow.
   - **Child-level geometry:** Do not infer text safety from a parent card's `scrollWidth`/`scrollHeight` alone. Measure every visible text node, icon, badge, KPI label/value, table row, and CTA against its own card's inner bounds; check right, left, top, and bottom edges plus line wrapping. A flex child can overflow while its parent still reports a clean layout.
   - **Human test:** Ask literally: "Would a normal person find this beautiful, calm, clear, useful, and worth reading?" If the answer is not an unqualified yes, identify the exact defect and fix it.
   - **Visual sign-off:** For each view, record `opened-full-resolution`, `read-dense-regions`, `checked-all-edges`, and `no-visible-collision`. Any false value blocks delivery.

4. Apply the anti-AI-slop gate to every visible string.
   - Remove meta-narration aimed at the creator or reviewer: "extrait vérifié", "vue simplifiée", "dans cette slide", "voici comment nous...", "pour les développeurs", or claims that merely describe an expected internal process.
   - Remove generic filler, throat-clearing, fake collaboration, and chatbot tics: "explorez...", "plongeons dans...", "il est important de noter...", "en quelques mots...", "allons découvrir...", "absolument", "n'hésitez pas...", and interchangeable "une expérience...". Start with the concrete fact or action.
   - Remove vague authority and unsupported credibility: "les experts", "les études montrent", "une solution innovante", "des sources fiables", "vérifié" without naming the source or adding user value.
   - Avoid synonym cycling, symmetrical slogan pairs, stacked adjectives, rhetorical questions used as decoration, dramatic fragments, inflated superlatives, empty conclusions, and repeated em-dash asides.
   - Prefer one concrete actor, verb, object, date, result, or consequence. Repeat the clearest noun when repetition improves comprehension; do not vary words merely to sound sophisticated.
   - Spell out unfamiliar acronyms and put the abbreviation after the full name when useful. Use the audience's language, not database codes or internal labels.
   - Keep claims proportional to evidence. If the source does not provide a fact, remove the claim rather than manufacture a polished substitute.
   - Read each string aloud once. If no human would naturally say it to this audience, rewrite it.

5. Verify and close the gate.
   - Render the full matrix, not a sample. Inspect every output visually at original resolution in the intended Browser/device frame; a contact sheet is only an index and never the sole visual evidence. Use the official integrated Browser when browser verification is requested.
   - Enforce artifact freshness: after the final UI edit, recapture every output and record the source/content identity, render timestamp or hash, and output directory. Never present a capture produced before the last edit or allow a stale browser/cache artifact to stand in for the final render.
   - Run the visual evidence matrix again after the final edit. The gate is closed only when `opened_count === required_count`, every view has a clean sign-off, and the automated checks are also green.
   - Compare the final render against the previous approved reference and the acceptance record. Batch actionable fixes, then inspect the affected set again. If the same defect survives two attempts, stop repeating the patch-and-capture cycle: diagnose its actual cause before proceeding. Never stop with a known defect merely because a pass count was reached.
   - Re-run the minimal relevant tests, type/lint checks, detector, and `git diff --check`.
   - Report what was verified, what changed, and any explicitly unresolved external limitation. Never claim a full visual pass if only examples were inspected.

### Goal-closure contract

Do not call `update_goal({status:"complete"})` for visual work until all of the following are true:

1. the final UI or visual artifact has been rendered after the last edit;
2. a local preview is reachable over HTTP and opened in the Codex browser/panel when browser review is part of the request;
3. every required view, route, state, breakpoint, and device frame has an exact fresh evidence path and has been opened at full resolution;
4. the visual checklist above has no actionable finding;
5. automated tests, type/lint checks, and the Impeccable detector are green.

If any item is missing, the goal remains active or is reported blocked; never infer completion from a previous run.

## Evidence standard

For each delivered set, retain or show:

- the complete rendered set (all slides/views, not only a representative sample);
- the exact source/content identity used for the render;
- the checklist findings and fixes for any failed view;
- the final targeted test/detector results.

## Research basis

The anti-slop rules are grounded in UX-writing guidance that favors clear, concise, specific language and full phrases for unfamiliar acronyms, plus observed AI-writing patterns such as filler, vague attribution, meta-commentary, synonym cycling, generic conclusions, and unsupported superlatives. Relevant references include NN/G's UX-writing guidance, GOV.UK plain-language error guidance, and anti-AI-pattern guides. These references inform the gate; they do not override the product's approved voice or factual source.


# General bible format

Use this when creating a general bible, or when an existing one is silent on a point. If the bible's own README defines something differently, its README wins.

## Layout

```
<bible>/
  README.md        purpose, when to read it, blocker protocol, structure, entry format, update rules
  SOURCES.md       one row per ingested source (id, title, author, type, published, ingested, bias, method, link)
                   + analysis notes (model misreadings caught, gaps between narration and screen)
  TOOLS.md         one row per tool or service: what for, cost or licence with the date observed, entry ids
  CHANGELOG.md     dated list of changes
  domains/         one file per game-dev domain, numbered for reading order
  engines/         one file per engine, only engine-specific facts (APIs, versions, renderer limits)
```

Suggested domains (create a file only when its first entry exists): production and AI agents, art direction, 3D assets, characters and animation, world/terrain/vegetation, water/VFX/atmosphere, rendering and performance, UI/UX, audio, gameplay systems, AI and NPCs, networking, physics and destruction, platforms and release, business and store.

## Entry template

```markdown
### PREFIX-NNN · Short imperative title
- **Use when:** the problem or situation.
- **How:** the method, key steps and parameters.
- **Evidence:** facts and numbers with source ids and timestamps or sections, e.g. [S004 5:08].
- **Caveats:** limits, costs, licences, platform restrictions.
- **Status:** Proven | Reported | Claimed · **Applies to:** any engine | <engine and version> | ...
- **Added:** YYYY-MM-DD · **Updated:** YYYY-MM-DD or -
```

- Each domain file starts with an `Index:` line listing its ids and short titles. Keep it current.
- Prefixes: PRD (production), ART, AST (assets), ANI, WLD (world), FX, PERF, UI, AUD (audio), GPL (gameplay), NPC, NET, PHY, REL (release), BIZ, and one per engine (GDT Godot, UNI Unity, UNR Unreal...).
- Status:
  - **Proven:** official documentation, or measured in a real project.
  - **Reported:** visible evidence in a credible source.
  - **Claimed:** assertion only, or an interested party.
  - **Recommendation:** advice derived from other entries, which it cites.
  Mixed claims get one status each, e.g. "Proven (API) / Claimed (speed)". The writer's own inferences are marked "[Probable]" or "[Guess]" inside the entry.
- Sources consulted only to verify (linked posts, PRs) get one SOURCES row per group, which says which parts were used. Corrections to older entries go both in the source's analysis notes and in the CHANGELOG.
- **Merging:** one idea, one entry. A new source enriches the existing entry: add its evidence and raise the status if warranted.
- **Contradiction:** keep both facts with source and date, and say which one wins when. Otherwise mark it `Open question`.
- **Removal:** only when proven wrong. Leave the id unused and log the removal in the CHANGELOG.

## README essentials (for a new bible)

- What it is, and that it names no specific project.
- When to read it: before starting work in a domain, and on every blocker.
- **Blocker protocol:**
  1. Search the general and project bibles.
  2. Report to the supervisor or user: what fails, what was tried, the recommendation.
  3. Research the established practice (official docs, release notes, postmortems, mature open source). Almost nothing in games is a world first.
  4. No fragile workaround or silent regression.
  5. Report the lesson once solved.
- The structure, the entry format and the update rules (this file).

# Project bible format

The project bible is the project's selection from the general bible, plus its own rules, measurements and decisions. If the project already keeps practice sheets, guidelines or a lessons file, that **is** the project bible: give its index the name "project bible", link it to the general bible, and add the sections below. Do not create a parallel document.

## Index file essentials

1. **Title and status line:** name, status, last update date.
2. **Pointer to the general bible:** its path, and that leads are cited by the general bible's ids.
3. **Rule for every agent:**
   - read your domain's sheet before starting;
   - deviate only with evidence;
   - **blocker protocol:** search both bibles, report to the supervisor (or the user) with what you tried and what you recommend, research the established practice, no fragile workaround; the supervisor or user decides.
4. **Sheets:** one per domain, with the owner of each topic, so each topic has a single source of truth.
5. **External leads:** the table below.
6. **Review:** dates and triggers (engine upgrade, a lab contradicting a rule, a new pitfall).

## External leads table

| Id (general bible) | Lead | Why it matters here | Owning sheet | State (date) |
|---|---|---|---|---|
| ANI-003 | Blend locomotion clips by measured speed | Fixes our foot sliding at walk speed | animation | to test (YYYY-MM-DD) |

- **Why it matters here:** tie it to a known problem, goal or budget of this project (a measured bottleneck, a user complaint, a missing feature). A lead with no local reason is noise.
- **States:** to test, in test, validated (the owning sheet adopted it), rejected (with the reason).
- A lead becomes a rule only after it is measured on the project's real targets (devices, platforms, budgets). Record the measurement in the owning sheet.

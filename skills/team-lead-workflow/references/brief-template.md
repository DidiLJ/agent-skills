# Brief templates

## Common rules file (one per project, shared by every team)

- **Read first:** the project instructions, the checklist lines of your domain, the lessons file, the project bible (your domain's sheet and leads), the general bible, and the integration contract (the API that features must plug into).
- **Ownership:** one team = one sandbox = one domain. Touch others' files only through the contract. Create new sandboxes inside the main project.
- **Blocker protocol:** search the bibles, write a BLOCKER note, research the established practice. Never a workaround.
- **Technique:** tool paths, mandatory flags, timeouts, code conventions, and input rules (touch AND mouse/keyboard...).
- **Checks:** the exact commands. Add one check per unit, with an exact OK token and a negative case.
- **Finishing:**
  - real-renderer captures at target size, plus 2x crops;
  - a critic pass, PASS or FAIL, with at least 2 fixes per FAIL;
  - a reviewed video for anything that moves.
- **Resources:** free and licence-clear sources with provenance. Paid generation goes through the lead.
- **Device:** who exports and measures (the lead), and the budgets.
- **Git:**
  - one commit per unit;
  - merge main at the start and before the final checks;
  - never commit-all or a bare stash;
  - never push, never create pull requests, never install on devices.
- **Final report:**
  - what works, with capture and video paths;
  - check tokens;
  - the video verdict;
  - what is not verified;
  - open flaws;
  - BLOCKER notes;
  - next steps;
  - "Lessons".

## Team brief

```
# Team <name> — brief round <n> (<date>)
Worktree: <path> (branch <branch>, sparse: <folders>), based on <commit>. Read <common rules file> first.

## Goal
<one checkable sentence; the user's words if they gave them; checklist line id>

## What exists (read it, do not redo it)
<files, previous rounds' results with numbers, known defects with evidence, bible leads>

## You own / Do not touch
<paths and sandbox> / <other teams' areas> ; contracts with <team>: <fields, ids>

## Units (in order; commit and report after each)
1. <unit: deliverable + proof + check token>
2. ...

## Proof required in the report
<captures, crops, videos, checks, measurements>
```

## Launch message (to the agent)

```
You are the <team> team of <project>. Work ONLY inside <worktree>.
Read, in this order, and follow exactly: 1. <common rules>; 2. <team brief>.
Working style: be fast and efficient; do exactly what the briefs ask with the smallest change that works,
reusing existing code first; no refactor or feature outside the scope (report it instead).
You cannot ask questions: choose the option that changes the least and list your assumptions.
When blocked, apply the blocker protocol and end your turn with a BLOCKER note.
Report after each unit.
```

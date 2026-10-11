---
name: bible-ingest
description: 'Turn links into durable game-development knowledge. Use this whenever the user shares one or more links to learn from (YouTube or other videos, articles, blog posts, docs, release notes, GitHub repos, forum or social threads, PDFs, talks), even when they only paste links with no instruction, or say "analyse this", "what can we take from this video", "any good practices here", "add this to the bible". It analyses each source (for videos: transcript, frames, plus a Gemini video pass when available), extracts practices, patterns, tools, methods, numbers and pitfalls, merges them into the general game-dev bible without duplicates or contradictions, updates the current project''s bible, and gives the user a short, plain-language report with what matters now.'
---

# Bible ingest

A link is worth ingesting only if what it teaches outlives the conversation. This skill turns sources into two kinds of durable knowledge:

- **General bible:** knowledge valid for any game project, kept even when no current project can use it (another engine, a feature nobody plans yet).
- **Project bible:** the selection that matters for the project at hand, with the project's own problems and test status.

It ends with a short report to the user.

The bibles are only useful if agents can trust them. So the work is careful: every fact has a source and a date, nothing is duplicated, contradictions are made explicit, and the claims you could not check are labelled as such.

## 1. Locate the two bibles

- **General bible:** look, in this order, for a path given by the user, then in the user-level agent instructions, then in the project instructions (search those files for "bible"). If none exists, say so and create one following `references/bible-format.md`, in a location the user's instructions suggest for cross-project material. Then add a pointer to it in the user-level instructions.
- **Project bible:** look for the path in the project instructions or its documentation index. Projects often already have an equivalent (practice sheets, guidelines, lessons): reuse it and name it consistently rather than creating a second one. If none exists, create it from `references/project-bible-format.md` and reference it from the project instructions.

Read the general bible's README and the project bible's index before extracting anything. You need their structure, their id scheme and the project's open problems to file things in the right place. If the project bible points to a different general-bible path than the instructions do, follow the instructions and mention the mismatch in your report.

## 2. Analyse each source

Note for every source: title, author, publication date, the date you analysed it, and any bias (sponsor, affiliate link, vendor, marketing). A sponsored video can still teach a sound method, but its quality claims about the sponsor's product stay "Claimed" until something visible proves them.

**Videos.** Follow `references/video-analysis.md`. You combine three views:
- **Narration:** the transcript, read in full, gives the intent and the reasons.
- **Frames:** contact sheets, then full frames of settings, numbers and code, give the exact values.
- **Gemini** (when available; a `gemini-video-review` skill, if present, holds the local command) catches the on-screen text and the motion you skimmed past.

`scripts/prepare_video.py` (run it with any Python 3) does the download, transcript, contact sheets and parts in one command. Every number Gemini reports must be confirmed on a frame or in the transcript before it is filed.

**Articles, docs, release notes, pull requests.** Read the full text, not a summary: some web tools return a model-written summary, which hides numbers and caveats. `references/source-fetching.md` has the recipes (raw page to text, GitHub API for PRs and issues). Search the whole body for numbers and tables before concluding that something is absent: benchmark tables often sit at the very end of a PR description. Follow links to primary sources and note the version each fact applies to.

**Repositories.** Read the README, the docs, the licence, the latest release and the last commit date. Skim open issues for known problems. A brilliant but abandoned addon is a risk worth recording.

**Threads and social posts.** Treat them as leads: find the primary source before rating anything above "Claimed".

When a key claim is cheap to verify (an API exists in a given engine version, a setting's name, a licence clause), verify it. Mark the rest as unverified rather than dropping it.

## 3. Extract

Extract anything a game developer could reuse:
- best practices and proven patterns;
- workflows and methods, with steps and parameters;
- tools and services, with cost, licence, version and the date observed;
- numbers and benchmarks, with their context;
- pitfalls with their fix;
- recommendations and trade-offs;
- clever tricks.

Keep items that do not fit the current project. Leave out filler, pure promotion and advice too vague to act on.

Write in your own words. Short quotations (well under 15 words) are fine as evidence. Never copy long passages.

## 4. Merge into the general bible

Follow the bible's own README. Where it is silent, use `references/bible-format.md`.
- **Search before writing.** Grep the bible for the main keywords of each item. If an entry already covers the idea, add the new evidence (source id and timestamp) to it and adjust its status. Never create a second entry for the same idea.
- **Re-verify first when the source is primary.** If the new source is the primary source behind an existing entry (an official post behind a facts list taken from a video, a PR behind a claimed benchmark), check that entry's claims against it before adding anything. Correct what is wrong.
- **Log every correction twice:** in the source's analysis notes in `SOURCES.md`, saying what was wrong and what replaces it, and in `CHANGELOG.md`.
- **Secondary material.** Posts, PRs and docs consulted only to verify get one `SOURCES.md` row per group, which says which parts were actually used.
- **Contradictions.** Keep both facts in the entry, each with source and date, and state which one wins under which conditions. If nothing decides, mark it `Open question`. Silently overwriting a fact destroys information another project may need.
- **Ids are stable.** New entries take the next free number with the domain prefix. Domain files keep their index line up to date.
- **Status:**
  - **Proven:** official docs, or measured in a real project.
  - **Reported:** visible evidence in the source.
  - **Claimed:** asserted only, or by an interested party.
  - **Recommendation:** advice derived from other entries, which it cites.
  When the claims inside one entry differ, give each its status (e.g. "Proven (API) / Claimed (speed)"). Mark your own inferences inside an entry with "[Probable]" or "[Guess]", so they cannot be mistaken for the source's facts.
- **No project names, no personal paths.** The general bible serves every project.
- **Registers.** Update `SOURCES.md` (including how you analysed the source and Gemini's corrections), `TOOLS.md` and `CHANGELOG.md`. Use absolute dates everywhere.
- If the bible is a git repository, commit the ingestion as one commit with a clear message. Amending your own local, unpushed ingestion commit to keep it as one commit is fine. If the bible has a remote, push after committing.

## 5. Update the project bible

Before writing leads, grep the project's recent research notes, lessons and decisions for the same topics. A lead should link to the project's own work on the subject, and must not contradict a decision silently.

Select the entries that could matter for this project and add them to its external-leads list:
- the bible id;
- the lead in one line;
- why it matters **here**, tied to a known problem, goal or budget of the project when possible;
- the owning sheet or domain;
- the state: to test, in test, validated, rejected (with the reason).

A lead is not a rule. It becomes one only after the project measures it on its real target platforms. When an entry clearly confirms or contradicts something the project already does, say so in the lead. Commit with the project's usual rules, staging only the files you changed.

## 6. Report to the user

Write in the user's language, in plain words, and explain any jargon in a few words the first time. Be brief: the user wants the gist, not the bible. Use this structure:

```
Sources: one line each (title, length or size, bias flag if any).
To keep now for the project (up to 7 items): what it is, why it matters here, suggested next step, confidence.
  If the source brings nothing for the project's known problems, say so in one line, naming them.
Added to the general bible: number of entries created or enriched by domain, plus 2-4 notable items
  that do not apply to the project today but are worth knowing.
Doubts and corrections: unverifiable claims, model misreadings you caught, corrections made to older
  entries, licence or cost questions.
Files changed: one short line (commits), not a file list.
```

Use the confidence vocabulary the user prefers if their instructions define one; otherwise use certain, probable and guess.

## Pitfalls

- **Partial downloads.** A combined subtitle and video download can fail on one rate-limited subtitle track (HTTP 429). The script fetches them separately. Never conclude a video is unreadable after one failed attempt: try another format or language.
- **Gemini misreadings.** Gemini misreads version numbers, prices and small UI text. It can also name the wrong engine or role, or describe a teaser as a finished method. Its value is coverage, not precision.
- **Frame timestamps.** Frames sampled with an fps filter can be offset by a few seconds from the label. Re-extract a full frame with `-ss` before reading small text.
- **Narration against the screen.** When the narration and the on-screen counter disagree, report what the screen shows and note the gap.
- **Staleness.** Prices, model names and limits go stale within weeks: always store the observation date with them.

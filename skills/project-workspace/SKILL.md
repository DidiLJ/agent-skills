---
name: project-workspace
description: Use or set up a local multi-project workspace for project documentation, decisions, references, evidence and progress while agents remain in their existing desktop applications. Use when onboarding, maintaining the shared project view, publishing milestone evidence or preparing a handoff. It does not install an agent runner or replace the project's canonical files.
---

# Project workspace

The workspace is a shared view of existing project sources, not a second project database. Keep agents in their current desktop applications. A card, screenshot or manifest is an index or evidence, never sufficient proof of the current implementation.

## Find the right project before working

1. Resolve `WORKSPACE_ROOT` and `PROJECT_ROOT` from the project's instructions and existing workspace configuration. Do not infer a project from the last open tab. Read the local integration documentation for the configuration path and schema; do not guess JSON keys.
2. Open the project library, then the selected project. Keep navigation in English; preserve source documents in their existing language, including French. Branding belongs in local configuration, not this skill.
3. Follow links to the canonical decisions, specification, checklist, project bible and latest handoff. Read their dates and status. Compare the selected checkout, branch, commit and working-tree changes with what the workspace displays.
4. Inspect the actual code and relevant runtime evidence before relying on a claim. If the displayed revision, result or source no longer matches, mark it stale and state what needs rechecking. A stale card does not justify changing branches or discarding work.

## Maintain the shared view as work progresses

- At a meaningful milestone, decision, blocker, review or handoff, update the owning canonical document first, then refresh its workspace entry. Do not create a duplicate decision log, checklist or status file merely for the viewer.
- Keep links to existing files rather than copying them into a new content tree. Derived summaries identify their source, revision and date; they do not silently become authoritative.
- Distinguish **proposed**, **in progress**, **implemented**, **verified** and **user approved**. These are different claims, not an automatic progression. Preserve the project's existing vocabulary if equivalent. Only record user approval when the user actually gave it.
- Visual evidence identifies the build/commit, device, relevant settings and capture date. Label reference, current result and before/after explicitly. Use matching viewpoints when comparing; generated concepts never masquerade as engine captures.
- Record a check's scope and limitations: desktop does not prove mobile performance; an isolated lab does not prove integrated behaviour. Link the actual report or log, not only a green status badge.
- Give each shared file one owner. Coordinate before touching another agent's paths; do not move worktrees, launch alternative agents or change their workflow through the workspace.

## Handoff and resumption

Leave the canonical handoff with current branches/commits, dirty files and ownership, verified results, outstanding defects, next bounded task, and owned processes. Link it from the project view. Preserve earlier handoffs. A returning agent rechecks these facts against the checkout; the workspace is the entry point, not a substitute for verification.

## Set up or add a project

Read [references/setup.md](references/setup.md) only for installation, upgrades or registering another project. Reuse the existing local deployment and its configuration before adding code. Adding a project should be a configuration change, not a fork of the application.

## Report

State which canonical sources changed, which evidence was checked, and what remains stale or unverified. Do not declare a project complete because its workspace looks complete.

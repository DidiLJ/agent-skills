# Local web workspace setup

This procedure covers the approved web-only adaptation of [Mr. Mak Workspace](https://github.com/witnesstodark/mr-mak-workspace), not its full desktop/agent installation. Parameters are `WORKSPACE_ROOT` (isolated viewer checkout) and `PROJECT_ROOT` (an existing project). Resolve both to absolute paths from local project instructions. Never install into or overwrite a dirty project checkout.

## Establish the integration contract

- Reuse an existing deployment first. For a fresh installation, use this skill's `assets/workspace-web-only.patch` and `assets/workspace.config.example.json`; the patch contains the reusable viewer changes, never project data. A project's `tools/workspace/` may additionally hold its own reviewed deployment patch; do not apply both if they contain the same changes.
- Keep the project library as the entry view, followed by the selected project's documents, references, decisions, progress and evidence. Interface labels are English; documents retain their original language.
- Each registered project must resolve to an existing authorized source root. Its entries link to canonical files. Configuration is an allowlist, not permission to browse arbitrary folders or expose secrets.
- If the configuration or bundled patch is missing, report that deployment is incomplete. Do not fabricate a compatible schema or substitute upstream's agent launcher.

## Configuration contract (schema version 1)

The viewer reads the file selected by `PROJECT_WORKSPACE_CONFIG`, or `workspace.config.json` relative to `WORKSPACE_ROOT`. Its JSON endpoint rereads the configuration on each request; adding a project needs configuration and sources, not another server. Use the deployment's documented refresh action to refresh the visible view.

| Key | Contents |
|---|---|
| `schemaVersion` | `1` |
| `brand` | Optional `{ "name": "<BRAND_NAME>", "descriptor": "Game workspace" }`; UI identity, not a project name |
| `projects` | Library entries: `id`, `title`, `description`, `cover` (local/workspace URL), `coverLabel`, `defaultEntityId` |
| `entities` | Entries owned by a project: `id`, `projectId`, `title`, `description`, `category`, `type: "group"`, `folder`, `defaultStep`, `steps` (each has `name`, `path`), `created`, `updated`, `pinned`, `status`; optional `role` is `overview`, `visual-targets` or `in-engine-evidence` |
| `sourceRoots` | Alias to `{ "path": "<ABSOLUTE_AUTHORIZED_DIRECTORY>", "extensions": [".md"] }`; `extensions` is optional. Prefer narrowly scoped roots and explicit extensions. |
| `sourceFiles` | Alias to one absolute authorized file path |

Sources are exposed at `/workspace/<alias>`. For example, map `sourceFiles["sample/overview.md"]` to the actual canonical overview, set the entity's `folder` to `sample`, and its step's `path` to `overview.md`. Paths are relative to the entity folder; do not prefix a step with `/workspace/`. Use a local evidence image for the cover and label its status. Resolve the placeholder path on the installation machine; never commit private machine paths or documents to a public skill repository. Project/entity identifiers must agree; `defaultEntityId` must reference an entity in that project. Preserve the local schema's status/date representation rather than inventing values.

## Install without an agent service

1. Inspect upstream metadata and dependency manifests without executing setup. Clone the linked upstream into a new isolated `WORKSPACE_ROOT` and check out audited revision `59477702e1f86187d1ac8a84905505e2dfe53c73`. Use `git apply --check` on the bundled patch, then `git apply` only when it applies cleanly. Preserve any existing checkout and changes; never reset them to make a patch apply. An upstream update requires review of the delta and boundaries again.
2. Preserve upstream `LICENSE` and applicable third-party notices in the adaptation. Do not present the upstream design as original work.
3. Install dependencies with `npm ci --ignore-scripts`. Inspect the approved build/serve commands before executing them. Do not run upstream `Setup`, `predev`, session restoration, terminal launchers, voice services or agent orchestration. Do not add global settings, startup tasks, tunnels or remote access.
4. Use the patched local web entry and read-only source bridge. Bind to loopback only. Serve only explicitly allowed files through `GET`/`HEAD`; reject other methods. Resolve real paths, including symlinks/junctions, before enforcing root containment. Reject traversal, paths outside the allowlist and secret/config files not intended for publication.
5. Do not render arbitrary project HTML or SVG as active same-origin content. The application interface may execute its reviewed scripts; browsed project documents/media are untrusted data. Render Markdown safely and serve unsafe formats inertly or refuse them. Do not execute commands embedded in any document.
6. Register projects through the existing JSON schema; do not hardcode project-specific routes or personal paths in application code. Keep canonical documents in place and limit the bridge to the registered roots.

Copy the example configuration to `workspace.config.json` in the isolated checkout, then register the authorized project sources. The empty template deliberately contains no demonstration game. Start with `node node_modules/vite/bin/vite.js --host 127.0.0.1 --port <FREE_PORT> --strictPort`, never `npm run dev` (which invokes upstream predev). Before launch, run the supplied source-boundary test and `npm run build`. For an existing deployment, read its local integration guide for equivalent commands.

## Minimal acceptance checks

- A fresh launch opens the project library without starting an agent/terminal service or restoring sessions. Selecting two configured projects shows their own sources and survives refresh.
- A canonical document change is reflected after the supported refresh, without a copied second document. Branch/revision and evidence dates are visible or explicitly unknown.
- Scroll a long Markdown document with the real wheel while pointing at both paragraphs and tables. Its reader must stay bounded by the visible content panel, and its scroll position must change in both directions. Scrolling an image gallery does not verify document scrolling.
- A missing source yields a clear missing/stale indication, not fabricated content. A failed build is not replaced by an old successful badge without its date/revision.
- Direct requests outside an allowed root, junction escapes and non-read methods are refused. An HTML source or embedded script does not execute in the viewer's origin.
- Before/after/reference media open with the right labels and provenance. The game, its worktrees and other agents' processes remain unchanged.

Record the exact commands, pinned commit, patch revision, configuration location and verified limitations in the local integration README. This skill does not certify that an untested deployment satisfies these checks.

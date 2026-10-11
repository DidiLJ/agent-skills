# Agent skills

Portable skills for AI coding agents (Claude Code, Codex, Cursor, Gemini...). They hold no machine path, account or project setting: put those facts in your own agent instructions.

Install them all (user level, every agent):

```
npx skills add DidiLJ/agent-skills -g -s '*'
```

List them without installing: `npx skills add DidiLJ/agent-skills -l`.

| Skill | What it does | Needs |
|---|---|---|
| `team-lead-workflow` | Run a project as a lead supervising AI agents: one team per domain and sandbox, waves by dependency, briefs, verification gates, bibles, git hygiene, reporting | an agent tool that can spawn subagents |
| `bible-ingest` | Turn links (videos, articles, repos) into a general game-dev knowledge bible plus a project bible, then a short report | `ffmpeg`, `ffprobe`, `yt-dlp` for videos; `gemini-video-review` optional |
| `gemini-video-review` | Have Gemini watch a short clip and list motion defects with timestamps | Antigravity CLI `agy` signed in with a Google account |
| `mobile-game-check` | Final mobile-first checklist for a Godot game unit: touch and mouse input, web export, phone display, performance, physics | Godot 4.x, an Android phone for measurements |
| `human-quality-gate` | Inspect every rendered view before delivery: UX/UI review, factual checks, anti-AI-slop copy | the `impeccable` skills (pbakaus/impeccable) |
| `codex-imagegen` | Generate or edit images (mockups, icons, textures, 3D references) with the Codex CLI built-in image tool | Codex CLI signed in to a ChatGPT account |
| `tripo-asset-kit` | Build a 3D asset and its separate parts (kit, vehicle, destructible prop) with Tripo Studio from an exploded-view image, then prepare it for a game engine | Tripo Studio account, `codex-imagegen`, Blender |

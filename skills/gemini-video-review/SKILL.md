---
name: gemini-video-review
description: Have Gemini watch a short video (gameplay capture, animation, physics, UI motion) and list visible defects with timestamps, through the Antigravity CLI (agy) signed in with a Google account. Use when a defect only shows in motion (animation, physics, clipping during movement, transitions) and frames are not enough; not for static layout checks.
---

# Gemini video review

Claude and Codex see images, not video. Gemini (via the Antigravity CLI `agy`, which replaced Gemini CLI for personal accounts in 2026) can watch a video file.

## When to use
- Motion defects: animation glitches, foot sliding, clothing clipping during a move, ragdoll jitter, physics popping, UI transitions.
- Not for static checks (layout, text, colours): a screenshot is cheaper and exact.
- Treat its output as a second opinion to verify, never as proof: cross-check every claimed defect on a frame you extract yourself.

## Steps
1. Record a short silent clip (5-15 s) of the running app. Example with Godot, windowed, never headless (take the `godot` executable from PATH or from the project's agent instructions):
   `godot --audio-driver Dummy --path <project> [scene/flags] --resolution 1280x582 --write-movie <tmp dir>/<name>.avi --fixed-fps 30 --quit-after <frames>`
   (the output folder must exist before Godot starts), then
   `ffmpeg -y -loglevel error -i <name>.avi -c:v libx264 -crf 26 -pix_fmt yuv420p <name>.mp4`.
   On the phone: `adb shell screenrecord --time-limit 10 /sdcard/c.mp4` then `adb pull`.
2. `bash <skill folder>/scripts/review.sh <name>.mp4 "<what the clip shows and what to check>"`.
   Keep the prompt neutral (do not name the defect you suspect) so the answer is a real test.
3. Extract the frames at the reported timestamps (`ffmpeg -ss <t> -i <mp4> -frames:v 1 f.png`) and look at them before acting.

## Measured (2026-10-07)
- YouTube link (2026-10-08): with read_url only, agy fetches the page HTML, not the frames. It CAN watch it if it is allowed to download the file first (an interactive agy session did: download, then view_file). Headless route that works: `python -m yt_dlp -f "bv*[height<=720][ext=mp4]+ba[ext=m4a]/b[height<=720]" --merge-output-format mp4 -o <name>.mp4 <url>` (needs yt-dlp; install it first if missing) then the review script on the file. Never declare a limit after one failed attempt.
- `gemini -p` fails: personal OAuth is "no longer supported", migrate to Antigravity. `agy` (1.2.3 tested) works once signed in with a Google account.
- Without `--mode plan` and a "view_file only" instruction, a "strict review" prompt makes it try shell commands, auto-denied in headless mode (no output).
- 8 s Meshy gallery clip: it found, unprompted, the two known defects (skirt clipping through the thighs, over-bright plastic skin) plus plausible extras (no floor shadows, stiff fingers). About 30-60 s per call.

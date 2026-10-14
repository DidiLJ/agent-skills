# Video analysis method

Three independent views of the same video, then a cross-check. Each view misses things the others catch.

## 1. Prepare

```
python <skill folder>/scripts/prepare_video.py "<url>" --out <work dir>/<video id>
```

- Use one folder per video, outside any repository. Delete the media once the analysis is filed (keep the transcript and notes if useful).
- The script prints a JSON summary: duration, transcript path and word count, contact sheets, parts (with their start offset in seconds) and notes on anything that failed.
- Without subtitles, the transcript is missing. The Gemini pass then has to carry the narration: ask it to summarise what is said, and check key statements against frames.
- Requirements: `ffmpeg` and `ffprobe` on PATH, and `yt-dlp` (`pip install yt-dlp`) for URLs. Downloading a video for private analysis can conflict with a platform's terms: follow the user's instructions on downloads, and never redistribute the file.

## 2. Your own reading

1. **Description:** chapters, credits, data sources, sponsor disclosure.
2. **Transcript:** read all of it. List the claims, numbers, tools and steps with their timestamps.
3. **Contact sheets:** look at every sheet. Mark the moments that show settings, UI panels, numbers, code, diagrams, or before/after comparisons.
4. **Full frames** for those moments: `ffmpeg -ss <seconds> -i video.mp4 -frames:v 1 frame.png`, cropped if the text is small (`-vf "crop=w:h:x:y,scale=2*iw:-1"`). Read the exact values from them.

- If you cannot view the contact sheets (an image budget or tool limit), extract single frames at the timestamps the transcript points to, and around every on-screen number you plan to cite.

## 3. Gemini pass (if a Gemini video-capable CLI or API is available)

If a `gemini-video-review` skill exists on this machine, read it: it holds the local command, the model and known quirks. The method:
- Send one part (≤ 5 minutes) per call. Long files get vaguer answers.
- Run read-only. Use a "plan" or no-tools mode and tell it to use only the file-view tool, otherwise a headless CLI may try commands that get denied and returns nothing.
- Attach the local file. Some CLIs only fetch the HTML of a YouTube URL instead of watching it.
- Keep the prompt neutral: ask what is shown, not whether your hypothesis is right.
- A local review script may append its own instructions (for example a defect-oriented list capped at 12 bullets). For extraction, call the CLI directly with the same flags and the prompt below, so that the two instructions do not conflict.

Extraction prompt (adapt the length limit):

```
This clip is part of a game-development video. Describe what is shown on screen, in order:
every tool, software, website, AI model or plugin (exact names and versions when readable),
the menus, settings and parameter values visible, the workflow steps, the results shown (good or bad),
the problems that appear and how they are handled, and any advice or recommendation stated on screen.
Copy on-screen text exactly when it matters. Each item with an approximate timestamp in seconds from
the start of THIS clip. Mark uncertain items as uncertain; do not invent. English, max 30 bullets.
```

Run the calls in the foreground, or poll their output files: a call started in a background sub-shell can report "finished" before the model has answered.

Timestamps come back relative to each part. Add the part's offset (from the script's summary) to get video time.

## 4. Cross-check before filing

- Every number, price, version or setting that goes into the bible must be confirmed by a frame you looked at or by the transcript. Mark Gemini-only items "seen by Gemini only, not checked on a frame" and give them a lower status.
- Write down Gemini's errors in the source's analysis notes. That record tells future readers how much to trust each kind of reading.
- When the narration and the screen disagree, report the screen and mention the gap.
- A teaser (the "next episode") is a Claim, not a method.

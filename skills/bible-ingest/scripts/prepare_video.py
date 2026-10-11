#!/usr/bin/env python3
"""Prepare a video for analysis: download (<=720p), subtitles, description, timestamped transcript,
contact sheets (one frame every N seconds) and parts short enough for a video model.

Usage: python prepare_video.py <url-or-local-file> [--out DIR] [--every 10] [--part-minutes 5]
                               [--sub-langs en-orig,en,fr]
Needs ffmpeg/ffprobe on PATH; yt-dlp (python module or CLI) for URLs.
Prints a JSON summary of what it produced; a missing optional piece (subtitles) is reported, not fatal.
"""
import argparse, glob, importlib.util, json, os, re, shutil, subprocess, sys


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def ytdlp_cmd():
    if importlib.util.find_spec("yt_dlp"):
        return [sys.executable, "-m", "yt_dlp"]
    if shutil.which("yt-dlp"):
        return ["yt-dlp"]
    sys.exit("yt-dlp not found (pip install yt-dlp, or put the yt-dlp CLI on PATH)")


def download(url, out, sub_langs, notes):
    y = ytdlp_cmd() + ["--no-warnings", "-o", os.path.join(out, "video.%(ext)s")]
    meta = run(y + ["--skip-download", "--write-info-json", "--write-description", url])
    if meta.returncode:
        notes.append("metadata failed: " + meta.stderr.strip()[-300:])
    # Subtitles separately: a rate-limited subtitle track (HTTP 429) must not abort the video download.
    for lang in sub_langs:
        r = run(y + ["--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", lang,
                     "--sub-format", "vtt", url])
        if glob.glob(os.path.join(out, "*.vtt")):
            break
        notes.append(f"subtitles '{lang}' unavailable: " + r.stderr.strip()[-200:])
    for fmt in ("bv*[height<=720][ext=mp4]+ba[ext=m4a]/b[height<=720][ext=mp4]",
                "bv*[height<=720]+ba/b[height<=720]/b"):
        r = run(y + ["-f", fmt, "--merge-output-format", "mp4", url])
        if os.path.exists(os.path.join(out, "video.mp4")):
            return True
        notes.append(f"video format '{fmt}' failed: " + r.stderr.strip()[-200:])
    return False


def vtt_to_transcript(vtt, dst, bucket=30):
    def secs(t):
        h, m, s = t.split(":")
        return int(h) * 3600 + int(m) * 60 + float(s)
    out, seen, buf, start, cur = [], set(), [], 0.0, 0.0
    for line in open(vtt, encoding="utf-8", errors="replace").read().splitlines():
        m = re.match(r"(\d\d:\d\d:\d\d\.\d+) -->", line)
        if m:
            cur = secs(m.group(1))
            continue
        text = re.sub(r"<[^>]+>", "", line).strip()
        if not text or line.startswith(("WEBVTT", "Kind:", "Language:")) or text in seen:
            continue
        seen.add(text)
        if cur - start >= bucket and buf:
            out.append(f"[{int(start // 60)}:{int(start % 60):02d}] " + " ".join(buf))
            buf, start = [], cur
        buf.append(text)
    if buf:
        out.append(f"[{int(start // 60)}:{int(start % 60):02d}] " + " ".join(buf))
    open(dst, "w", encoding="utf-8").write("\n".join(out))
    return sum(len(x.split()) for x in out)


def duration(video):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video])
    return float(r.stdout.strip() or 0)


def contact_sheets(video, out, every):
    d = os.path.join(out, "sheets")
    os.makedirs(d, exist_ok=True)
    # select keeps the first frame at or after each N-second boundary, so the stamp shows the frame's real time
    # (fps=1/N picks frames about N/2 seconds after the label)
    base = "select='isnan(prev_selected_t)+gte(t-prev_selected_t\\,%d)',scale=320:180" % every
    stamp = ",drawtext=text='%{pts\\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6"
    for vf in (base + stamp + ",tile=4x4", base + ",tile=4x4"):  # drawtext needs a font; fall back without it
        r = run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-vf", vf, "-fps_mode", "vfr", os.path.join(d, "s%02d.png")])
        sheets = sorted(glob.glob(os.path.join(d, "s*.png")))
        if r.returncode == 0 and sheets:
            return sheets, "drawtext" in vf
    return [], False


def split_parts(video, out, total, part_minutes):
    n = max(1, int(-(-total // (part_minutes * 60))))
    size = total / n
    parts = []
    for i in range(n):
        p = os.path.join(out, f"part{i + 1}.mp4")
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{i * size:.2f}", "-i", video]
        if i < n - 1:
            cmd += ["-t", f"{size:.2f}"]
        run(cmd + ["-c", "copy", p])
        parts.append({"file": p, "offset_s": round(i * size, 2)})
    return parts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--out")
    ap.add_argument("--every", type=int, default=10, help="seconds between contact-sheet frames")
    ap.add_argument("--part-minutes", type=float, default=5)
    ap.add_argument("--sub-langs", default="en-orig,en,fr")
    a = ap.parse_args()
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            sys.exit(f"{tool} not found on PATH")
    vid = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{6,})", a.source)
    out = a.out or os.path.abspath("video-" + (vid.group(1) if vid else "local"))
    os.makedirs(out, exist_ok=True)
    notes, video = [], os.path.join(out, "video.mp4")
    if os.path.isfile(a.source):
        shutil.copyfile(a.source, video)
    elif not download(a.source, out, a.sub_langs.split(","), notes):
        print(json.dumps({"ok": False, "out": out, "notes": notes}, indent=1))
        sys.exit(1)
    summary = {"ok": True, "out": out, "video": video, "duration_s": round(duration(video), 1)}
    vtts = sorted(glob.glob(os.path.join(out, "*.vtt")))
    if vtts:
        t = os.path.join(out, "transcript.txt")
        summary["transcript"], summary["transcript_words"] = t, vtt_to_transcript(vtts[0], t)
    sheets, stamped = contact_sheets(video, out, a.every)
    summary.update(sheets=sheets, sheets_timestamped=stamped, sheet_frame_every_s=a.every)
    summary["parts"] = split_parts(video, out, summary["duration_s"], a.part_minutes)
    summary["notes"] = notes
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()

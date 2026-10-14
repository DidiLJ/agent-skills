#!/usr/bin/env bash
# Ask Gemini (Antigravity CLI "agy", signed in with a Google account) to review a video and list visible defects.
# Usage: review.sh <video.mp4> "<what this video shows and what to check>" [model]
# Plan mode + "view_file only" keeps it from running commands (headless mode cannot approve them).
set -u
# Windows path for agy when running under Git Bash/MSYS (cygpath); unchanged path elsewhere.
winpath() { cygpath -w "$1" 2>/dev/null || printf '%s' "$1"; }
video=$(cygpath -w "$(realpath "$1")" 2>/dev/null || echo "$1"); ask="$2"; model="${3:-Gemini 3.8 Flash (High)}"
dir=$(dirname "$1"); name=$(basename "$1")
cd "$dir" || exit 2
# agy (Go, Windows) rejects Google TLS when SSL_CERT_FILE points to a custom bundle: drop it for agy only.
timeout 600 env -u SSL_CERT_FILE agy --model "$model" --mode plan --add-dir "$(winpath "$(pwd)")" -p "@$name Use only the view_file tool on the attached video, no other tool. $ask List only what is visible, each item with an approximate timestamp in seconds and the object or character concerned; mark uncertain items as uncertain; do not invent. English, max 12 bullets."

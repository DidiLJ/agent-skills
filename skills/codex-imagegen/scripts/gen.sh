#!/usr/bin/env bash
# Generate or edit one image with the Codex CLI built-in image_gen tool and copy it to <out.png>.
# Usage: gen.sh [--edit] "<prompt>" <out.png> [reference-image ...]
#   --edit : modify the FIRST reference image (change only what the prompt names, keep the rest identical);
#            further images are extra references.
#   default: generate a new image; reference images guide style/composition or are combined as the prompt says.
# Prints the destination path on success. Logs go next to the output: <out>.codex.jsonl / .codex.err.txt
#   --multi: the request asks for several separate images (e.g. turnaround views); every image of the thread is
#            copied, oldest first, to <out-stem>-1.png, -2.png, ...
# GEN_LOG_DIR=<dir> puts the Codex logs there instead of next to the output.
set -u
mode=generate
if [ "${1:-}" = "--edit" ]; then mode=edit; shift; fi
if [ "${1:-}" = "--multi" ]; then mode=multi; shift; fi
prompt="$1"; out="$2"; shift 2
refs=(); for r in "$@"; do refs+=("--image=$r"); done  # --image=FILE: a bare -i is variadic and would swallow the prompt
if [ "$mode" = edit ] && [ ${#refs[@]} -eq 0 ]; then echo "--edit needs at least one image" >&2; exit 2; fi

if [ "$mode" = edit ]; then
  instr="Use your built-in image_gen tool in edit mode (never a script, never the CLI/API fallback) on the first attached image: change only what the request names and keep everything else identical (composition, colours, framing, untouched regions). Other attached images are references. Produce exactly one image, do not copy or post-process the file, reply DONE. Edit request: $prompt"
elif [ "$mode" = multi ]; then
  instr="Use your built-in image_gen tool (never a script, never the CLI/API fallback) to generate the separate images the request asks for, one tool call per image, in the requested order. Attached images, if any, are references. Do not copy or post-process the files, reply DONE. Image request: $prompt"
else
  instr="Use your built-in image_gen tool (never a script, never the CLI/API fallback) to generate exactly one image. Attached images, if any, are references to follow or combine as the request says. Do not copy or post-process the file, reply DONE. Image request: $prompt"
fi

work=$(mktemp -d)
logbase="${out%.*}"; [ -n "${GEN_LOG_DIR:-}" ] && { mkdir -p "$GEN_LOG_DIR"; logbase="$GEN_LOG_DIR/$(basename "${out%.*}")"; }
log="$logbase.codex.jsonl"; err="$logbase.codex.err.txt"
mkdir -p "$(dirname "$out")"
timeout 900 codex exec --skip-git-repo-check -s workspace-write -C "$work" \
  -c model_reasoning_effort='"low"' --json "${refs[@]}" "$instr" > "$log" 2> "$err"
rc=$?
thread=$(grep -o '"thread_id": *"[^"]*"' "$log" | head -1 | sed 's/.*"\([^"]*\)"$/\1/')
rm -rf "$work"
if [ "$mode" = multi ]; then
  i=0; for f in $(ls -tr "$HOME/.codex/generated_images/$thread/"*.png 2>/dev/null); do
    i=$((i+1)); cp "$f" "${out%.*}-$i.png" && echo "${out%.*}-$i.png"; done
  [ "$i" -eq 0 ] && { echo "NO_IMAGE rc=$rc thread=$thread (see $log, $err)" >&2; exit 1; }
  exit 0
fi
src=$(ls -t "$HOME/.codex/generated_images/$thread/"*.png 2>/dev/null | head -1)
if [ -z "$src" ]; then echo "NO_IMAGE rc=$rc thread=$thread (see $log, $err)" >&2; exit 1; fi
cp "$src" "$out" && echo "$out"

#!/usr/bin/env bash
# Runs under the virtual display started by take-screenshot.sh.
# Usage: capture.sh <output.png> <seconds> [xdotool key names...]
set -euo pipefail

out=$1
seconds=$2
shift 2

python src/main.py &
game=$!
sleep 1
window=$(xdotool search --name "Space Invaders" | head -n 1)
xdotool windowfocus "${window}" || true
for key in "$@"; do
  xdotool key --window "${window}" "${key}"
  sleep 0.2
done
sleep "${seconds}"
import -window "${window}" "${out}"
kill "${game}" || true

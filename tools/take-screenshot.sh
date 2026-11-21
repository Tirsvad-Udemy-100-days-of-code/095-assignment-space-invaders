#!/usr/bin/env bash
# Runs inside the Docker image of tools/Dockerfile.
# Usage: take-screenshot.sh <name> [seconds] [xdotool key sequence...]
#   name     output file docs/images/<name>.png
#   seconds  how long the game runs before the picture is taken (default 3)
#   keys     xdotool key names pressed after one second, e.g. Left Left space
set -euo pipefail

name=${1:?usage: take-screenshot.sh <name> [seconds] [keys...]}
seconds=${2:-3}
shift $(( $# < 2 ? $# : 2 ))

out="docs/images/${name}.png"
mkdir -p docs/images

# The inner script runs under the virtual display.
SECONDS_TO_RUN=$seconds OUT_FILE=$out xvfb-run -a -s "-screen 0 1024x768x24" bash -c '
  set -euo pipefail
  python src/main.py &
  game=$!
  sleep 1
  window=$(xdotool search --name "Space Invaders" | head -n 1)
  xdotool windowfocus "$window" || true
  for key in "$@"; do xdotool key --window "$window" "$key"; sleep 0.2; done
  sleep "$SECONDS_TO_RUN"
  import -window "$window" "$OUT_FILE"
  kill "$game" || true
' _ "$@" 

#!/usr/bin/env bash
# Runs inside the Docker image of tools/Dockerfile.
# Usage: take-screenshot.sh <name> [seconds] [xdotool key names...]
#   name     output file docs/images/<name>.png
#   seconds  how long the game runs before the picture is taken (default 3)
#   keys     xdotool key names pressed after one second, e.g. Left Left space
set -euo pipefail

name=${1:?usage: take-screenshot.sh <name> [seconds] [keys...]}
seconds=${2:-3}
shift $(($# < 2 ? $# : 2))

mkdir -p docs/images
xvfb-run -a -s "-screen 0 1024x768x24" \
  bash tools/capture.sh "docs/images/${name}.png" "${seconds}" "$@"

# Isolated environment for the screenshots: a virtual display, so the game never
# opens on the host desktop.
FROM python:3.14-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-tk tk xvfb xdotool imagemagick x11-utils \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /work
ENTRYPOINT ["bash", "/work/tools/take-screenshot.sh"]

# Isolated environment for the screenshots: a virtual display, so the game never
# opens on the host desktop.
FROM python:3.14-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-tk tk xvfb xauth xdotool imagemagick x11-utils \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir pytest==8.4.2
RUN useradd --create-home --uid 1000 shots
WORKDIR /work
USER shots
ENTRYPOINT ["bash", "/work/tools/take-screenshot.sh"]

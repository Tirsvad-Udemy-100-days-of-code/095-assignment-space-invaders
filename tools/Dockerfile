# Isolated environment for the screenshots and the GUI tests: a virtual display,
# so the game never opens on the host desktop.
FROM python:3.14-slim@sha256:9aaa474097d094040649f2162a627c0049b408f52138d980916788d80f04802f
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python3-tk tk xvfb xauth xdotool imagemagick x11-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir pytest==8.4.2
RUN useradd --create-home --uid 1000 shots
WORKDIR /work
USER shots
ENTRYPOINT ["bash", "/work/tools/take-screenshot.sh"]

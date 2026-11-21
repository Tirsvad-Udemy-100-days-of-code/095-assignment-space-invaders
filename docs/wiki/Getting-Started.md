**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting Started

How to run the game and its tests on your own machine. The game needs Python 3.14 or newer with Tk, and no other package.

## Create and use a local `.venv`

Clone the repository, then create the environment inside it and update `pip` first.

```powershell
git clone ssh://git@git.tirsystem.com:10022/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders.git
cd 095-assignment-space-invaders
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the game

With the `.venv` active, start the game. Use the arrow keys to move and the space bar to fire.

```bash
python src/main.py
```

## Run the tests

The rules and the constants are tested on your machine. Tests that open a `turtle` window run in a Docker container on a virtual display, so they never take over your desktop.

```bash
python -m pytest
docker build -t space-invaders-shots tools
docker run --rm -v "$PWD:/work" -e SPACE_INVADERS_GUI_TESTS=1 -e PYTHONPATH=src --entrypoint bash space-invaders-shots -c "timeout 120 xvfb-run -a python -m pytest"
```

## Take the screenshots

Each step page has a screenshot. They are made in the same container: the first argument is the file name, the second the seconds to wait, then key names to press.

```bash
docker run --rm -v "$PWD:/work" space-invaders-shots step-3-shooting 0.1 Left Left Left space
```

## Scan before you push

Scan the working tree with opengrep and fix every finding before a push.

```powershell
& "$HOME\.opengrep\cli\latest\opengrep.exe" scan --config auto --error .
```

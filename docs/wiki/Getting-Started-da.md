[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Sådan kører du spillet og dets tests på din egen maskine. Spillet kræver Python 3.14 eller nyere med Tk og ingen andre pakker.

## Opret og brug et lokalt `.venv`

Klon repositoryet, opret derefter miljøet i det og opdater først `pip`.

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

## Kør spillet

Start spillet med det aktive `.venv`. Brug piletasterne til at flytte og mellemrumstasten til at skyde.

```bash
python src/main.py
```

## Kør testene

Reglerne og konstanterne testes på din maskine. Tests, der åbner et `turtle`-vindue, kører i en Docker-container på en virtuel skærm, så de aldrig overtager dit skrivebord.

```bash
python -m pytest
docker build -t space-invaders-shots tools
docker run --rm -v "$PWD:/work" -e SPACE_INVADERS_GUI_TESTS=1 -e PYTHONPATH=src --entrypoint bash space-invaders-shots -c "timeout 120 xvfb-run -a python -m pytest"
```

## Tag skærmbillederne

Hver trinside har et skærmbillede. De tages i den samme container: første argument er filnavnet, andet er sekunder at vente, derefter tastenavne, der skal trykkes.

```bash
docker run --rm -v "$PWD:/work" space-invaders-shots step-3-shooting 0.1 Left Left Left space
```

## Scan, før du pusher

Scan arbejdstræet med opengrep, og ret hvert fund, før du pusher.

```powershell
& "$HOME\.opengrep\cli\latest\opengrep.exe" scan --config auto --error .
```

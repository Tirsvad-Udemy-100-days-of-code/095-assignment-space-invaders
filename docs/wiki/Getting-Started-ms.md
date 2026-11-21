[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Cara menjalankan permainan dan ujiannya pada mesin anda sendiri. Permainan memerlukan Python 3.14 atau lebih baharu dengan Tk, dan tiada pakej lain.

## Cipta dan guna `.venv` tempatan

Klon repositori, kemudian cipta persekitaran di dalamnya dan kemas kini `pip` dahulu.

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

## Jalankan permainan

Dengan `.venv` aktif, mulakan permainan. Gunakan kekunci anak panah untuk bergerak dan palang ruang untuk menembak.

```bash
python src/main.py
```

## Jalankan ujian

Peraturan dan pemalar diuji pada mesin anda. Ujian yang membuka tetingkap `turtle` dijalankan dalam bekas Docker pada paparan maya, jadi ia tidak pernah mengambil alih desktop anda.

```bash
python -m pytest
docker build -t space-invaders-shots tools
docker run --rm -v "$PWD:/work" -e SPACE_INVADERS_GUI_TESTS=1 -e PYTHONPATH=src --entrypoint bash space-invaders-shots -c "timeout 120 xvfb-run -a python -m pytest"
```

## Ambil tangkapan skrin

Setiap halaman langkah mempunyai tangkapan skrin. Ia dibuat dalam bekas yang sama: hujah pertama ialah nama fail, yang kedua ialah saat untuk menunggu, kemudian nama kekunci untuk ditekan.

```bash
docker run --rm -v "$PWD:/work" space-invaders-shots step-3-shooting 0.1 Left Left Left space
```

## Imbas sebelum push

Imbas pepohon kerja dengan opengrep dan betulkan setiap dapatan sebelum push.

```powershell
& "$HOME\.opengrep\cli\latest\opengrep.exe" scan --config auto --error .
```

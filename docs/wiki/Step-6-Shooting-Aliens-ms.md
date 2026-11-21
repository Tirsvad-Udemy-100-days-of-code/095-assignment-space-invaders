[English](Step-6-Shooting-Aliens) · [Dansk](Step-6-Shooting-Aliens-da) · **Bahasa Malaysia**

# Langkah 6: Menembak makhluk asing

![Ruang kosong pada baris bawah tempat makhluk asing ditembak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-6-hits.png)

## Apa yang kami bina

Peluru yang menyentuh makhluk asing menyingkirkannya. Tembakan mengena dikesan melalui jarak antara pusat, `is_hit`. Semakin sedikit makhluk asing yang tinggal, semakin pendek masa antara dua gerakan, sehingga had minimum, jadi permainan menjadi lebih sukar apabila anda menang.

## Apa yang kami pelajari

- Mengesan perlanggaran melalui jarak antara dua pusat
- Mengeluarkan item daripada senarai dengan selamat, tanpa mengubah senarai semasa melaluinya
- Menjadikan kesukaran meningkat dengan kemajuan (`move_interval`)
- Membiarkan satu peraturan, `is_hit`, melayani beberapa jenis perlanggaran

## Cubalah

Bergerak ke bawah makhluk asing dan tekan <kbd>Space</kbd>.

## Di mana kodnya

`src/fleet.py`: `remove_hit`; `src/rules.py`: `is_hit`, `move_interval`

Sebelumnya: [Pergerakan makhluk asing](Step-5-Alien-Movement-ms) · Seterusnya: [Penghadang](Step-7-Barriers-ms) · [Gambaran keseluruhan](Home-ms)

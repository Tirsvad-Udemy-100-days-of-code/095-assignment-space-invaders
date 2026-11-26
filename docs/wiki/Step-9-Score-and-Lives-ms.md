[English](Step-9-Score-and-Lives) · [Dansk](Step-9-Score-and-Lives-da) · **Bahasa Malaysia**

# Langkah 9: Skor dan nyawa

![Baris skor dan nyawa di atas armada](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-9-score-lives.png)

## Apa yang kami bina

`Scoreboard` dengan skor dan tiga nyawa. Makhluk asing menembak balas: setiap dua saat makhluk asing paling bawah dalam lajur rawak menembak peluru merah, yang dihentikan oleh penghadang dan dibayar oleh kapal dengan satu nyawa. Satu baris makhluk asing bernilai 50, 40, 30, 20 atau 10 mata.

## Apa yang kami pelajari

- Menyimpan skor dan nyawa dalam satu kelas kecil yang juga menulisnya
- Menggunakan semula `Bullet` untuk peluru yang terbang ke bawah (langkah negatif)
- Memilih penembak rawak, dengan sumber rawak diberikan dari luar supaya ujian boleh menetapkannya
- Mencari item paling bawah bagi setiap lajur dengan fungsi tulen (`lowest_per_column`)

## Cubalah

Main satu permainan penuh dan perhatikan skor dan nyawa.

## Di mana kodnya

`src/scoreboard.py`, `src/game.py`, `src/fleet.py`: `choose_shooter`

Sebelumnya: [Permainan tamat dan menang](Step-8-Game-Over-and-Win-ms) · Seterusnya: [Refleksi](Reflection-ms) · [Gambaran keseluruhan](Home-ms)

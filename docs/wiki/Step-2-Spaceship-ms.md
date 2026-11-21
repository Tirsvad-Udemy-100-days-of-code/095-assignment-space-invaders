[English](Step-2-Spaceship) · [Dansk](Step-2-Spaceship-da) · **Bahasa Malaysia**

# Langkah 2: Kapal angkasa

![Kapal angkasa digerakkan ke kiri](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-2-ship.png)

## Apa yang kami bina

Kelas `Ship`, segi tiga hijau di bahagian bawah skrin. Kekunci anak panah menggerakkannya satu langkah ke kiri atau kanan, dan ia berhenti di tepi skrin. Had itu ialah fungsi tulen, `clamp`, dalam `rules.py`.

## Apa yang kami pelajari

- Mewarisi `Turtle` untuk membuat objek permainan
- Mengikat kekunci dengan `listen` dan `onkeypress`
- Memastikan peraturan bebas daripada skrin (`clamp`) supaya ujian tidak memerlukan tetingkap
- Menguji objek skrin dalam bekas dan bukan pada desktop

## Cubalah

Tekan <kbd>Left</kbd> dan <kbd>Right</kbd>.

## Di mana kodnya

`src/ship.py`, `src/rules.py`: `clamp`

Sebelumnya: [Skrin permainan](Step-1-Game-Screen-ms) · Seterusnya: [Menembak](Step-3-Shooting-ms) · [Gambaran keseluruhan](Home-ms)

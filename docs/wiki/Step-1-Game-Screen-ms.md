[English](Step-1-Game-Screen) · [Dansk](Step-1-Game-Screen-da) · **Bahasa Malaysia**

# Langkah 1: Skrin permainan

![Tetingkap permainan hitam yang kosong](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-1-screen.png)

## Apa yang kami bina

Tetingkap hitam 800 kali 600 bertajuk "Space Invaders" dan gelung bingkai. Animasi dimatikan dengan `tracer(0)`, jadi permainan melukis bingkai sendiri dengan `update()`, dan `ontimer` memanggil bingkai seterusnya tanpa menyekat tetingkap.

## Apa yang kami pelajari

- Menyediakan `Screen` turtle: saiz, warna latar dan tajuk
- Mematikan animasi automatik dengan `tracer(0)` dan melukis dengan `update()`
- Menjalankan gelung dengan `ontimer` supaya tetingkap kekal responsif dan boleh ditutup
- Meletakkan setiap nombor dalam `constants.py` sejak baris pertama

## Cubalah

Mulakan permainan; tetingkap hitam kosong dibuka.

## Di mana kodnya

`src/main.py`: `create_screen`, `main`

Seterusnya: [Kapal angkasa](Step-2-Spaceship-ms) · [Gambaran keseluruhan](Home-ms)

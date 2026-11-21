[English](Step-8-Game-Over-and-Win) · [Dansk](Step-8-Game-Over-and-Win-da) · **Bahasa Malaysia**

# Langkah 8: Permainan tamat dan menang

![Mesej GAME OVER dengan makhluk asing di kapal](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-8-game-over.png)

![Mesej YOU WIN selepas makhluk asing terakhir ditembak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-8-win.png)

## Apa yang kami bina

Permainan kalah apabila makhluk asing menyentuh kapal atau sampai ke baris kapal, dan menang apabila makhluk asing terakhir ditembak. Fungsi tulen `game_state` memutuskannya, kelas `Banner` menulis GAME OVER atau YOU WIN, dan kekunci berhenti berfungsi. Tangkapan skrin langkah ini datang daripada situasi yang disediakan dalam `tools/scenarios/`.

## Apa yang kami pelajari

- Menghuraikan permainan sebagai keadaan: sedang bermain, kalah atau menang
- Membiarkan satu fungsi memutuskan keadaan, supaya peraturan berada di satu tempat
- Menghentikan gelung bingkai dan kekunci apabila permainan tamat
- Menyediakan situasi dalam skrip untuk mengambil tangkapan skrin detik yang jarang berlaku

## Cubalah

Biarkan makhluk asing sampai ke kapal, atau tembak semuanya.

## Di mana kodnya

`src/banner.py`, `src/game.py`: `check_state`, `src/rules.py`: `game_state`

Sebelumnya: [Penghadang](Step-7-Barriers-ms) · Seterusnya: [Skor dan nyawa](Step-9-Score-and-Lives-ms) · [Gambaran keseluruhan](Home-ms)

[English](Step-5-Alien-Movement) · [Dansk](Step-5-Alien-Movement-da) · **Bahasa Malaysia**

# Langkah 5: Pergerakan makhluk asing

![Armada selepas bergerak ke kanan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-5-movement.png)

## Apa yang kami bina

Setiap saat armada bergerak satu langkah ke sisi. Apabila langkah seterusnya akan membawa makhluk asing melepasi tepi, armada turun lebih dekat dan berpusing. Masa dibaca dengan `time.monotonic`, dan keputusan dibuat oleh fungsi tulen `is_due` dan `next_fleet_move`.

## Apa yang kami pelajari

- Bergerak mengikut masa dan bukan dengan mengira bingkai, supaya kelajuan tidak bergantung pada komputer
- Menulis keputusan gerakan seterusnya sebagai fungsi yang memulangkan perubahan dan arah baharu
- Turun dan berpatah balik di tepi
- Menguji peraturan masa dengan memberikan masa sebagai parameter

## Cubalah

Tunggu beberapa saat dan lihat armada bergerak.

## Di mana kodnya

`src/fleet.py`: `update`, `move`; `src/rules.py`: `is_due`, `next_fleet_move`

Sebelumnya: [Armada makhluk asing](Step-4-Alien-Fleet-ms) · Seterusnya: [Menembak makhluk asing](Step-6-Shooting-Aliens-ms) · [Gambaran keseluruhan](Home-ms)

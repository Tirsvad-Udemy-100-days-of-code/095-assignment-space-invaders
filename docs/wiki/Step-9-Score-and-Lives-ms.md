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

Sebelumnya: [Permainan tamat dan menang](Step-8-Game-Over-and-Win-ms) · Seterusnya: [[('Bagaimana saya mendekati projek ini?', 'Saya merancang sebelum menulis kod. Projek dibahagikan kepada tiga gateway: persediaan, permainan itu sendiri dan dokumentasi. Permainan dibina dalam sembilan langkah kecil, setiap satu pada cabangnya sendiri dengan pull request, ujian, tangkapan skrin dan rekod semakannya sendiri, supaya sejarah menunjukkan bagaimana permainan berkembang. Segala yang tidak memerlukan tetingkap, seperti penghadan, susun atur armada, perlanggaran, selang masa gerakan dan keadaan permainan, diletakkan dalam `rules.py` supaya boleh diuji tanpa paparan.'), ('Apa yang sukar?', 'Menguji permainan berasaskan tetingkap. `turtle` memerlukan Tk dan paparan, jadi ujian yang membuka tetingkap tidak boleh dijalankan pada pelari integrasi berterusan atau pada desktop saya. Saya menyelesaikannya dengan imej Docker yang menjalankan permainan dan ujian pada paparan maya. Masa juga rumit: mengambil tangkapan skrin peluru yang sedang terbang atau armada yang telah bergerak memerlukan tekanan kekunci dan masa menunggu sepadan dengan gelung bingkai.'), ('Apa yang mudah?', 'Setelah peraturan dipisahkan daripada lukisan, logiknya pendek dan mudah diuji. Mewarisi `Turtle` untuk kapal, peluru, makhluk asing dan blok penghadang memberi setiap benda kelas kecilnya sendiri, dan pemalar dalam `constants.py` menjadikan penalaan permainan satu perubahan baris.'), ('Bagaimana saya boleh menambah baik untuk projek seterusnya?', 'Mulakan dengan persekitaran tangkapan skrin dan ujian sebelum baris pertama kod permainan, dan tulis ujian untuk sesuatu peraturan sebelum peraturan itu. Saya juga akan menjalankan peraturan imbasan saluran paip secara tempatan dengan cara yang sama seperti pelayan, supaya dapatan ditemui lebih awal.'), ('Apakah pembelajaran terbesar saya?', 'Memastikan peraturan permainan bebas daripada skrin adalah yang menjadikan projek grafik boleh diuji, dan gelung berasaskan masa (satu gerakan setiap saat) lebih ringkas dan lebih adil daripada mengira bingkai.'), ('Apa yang akan saya lakukan secara berbeza?', 'Saya akan melukis makhluk asing dan kapal sebagai bentuk khas dan bukan bentuk terbina dalam `turtle`, menambah bunyi dan senarai skor tertinggi, dan membiarkan armada menembak mengikut corak. Saya juga akan mengambil tangkapan skrin daripada permainan yang dirakam dan bukan daripada tekanan kekunci tunggal.')]](Reflection-ms) · [Gambaran keseluruhan](Home-ms)

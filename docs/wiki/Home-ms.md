[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Space Invaders

Permainan menembak Space Invaders klasik untuk seorang pemain dengan grafik turtle Python: gerakkan kapal angkasa anda, tembak makhluk asing sebelum mereka sampai kepada anda, dan berlindung di sebalik penghadang.

![Baris skor dan nyawa di atas armada](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-9-score-lives.png)

## Apakah ini?

Hari ke-95 kursus Udemy *100 Days of Code: The Complete Python Pro Bootcamp*. Tetingkap hitam 800 kali 600 bertajuk "Space Invaders" dibuka dengan sebuah kapal angkasa hijau di bahagian bawah, empat penghadang di atasnya dan lima baris makhluk asing di bahagian atas. <kbd>Left</kbd> dan <kbd>Right</kbd> menggerakkan kapal dan <kbd>Space</kbd> menembak satu peluru pada satu masa. Setiap saat makhluk asing bergerak lebih dekat, mereka berpusing dan turun di tepi, dan mereka bergerak lebih laju apabila semakin sedikit yang tinggal. Mereka menembak balas; satu tembakan mengena menyebabkan kehilangan satu nyawa. Permainan kalah apabila makhluk asing menyentuh kapal, sampai ke barisnya atau nyawa habis, dan menang apabila makhluk asing terakhir ditembak. Permainan ini dibina dalam sembilan langkah, satu pull request bagi setiap langkah, dan setiap langkah mempunyai halamannya sendiri dengan tangkapan skrin serta apa yang kami pelajari.

## Sembilan langkah

1. [Skrin permainan](Step-1-Game-Screen-ms)
2. [Kapal angkasa](Step-2-Spaceship-ms)
3. [Menembak](Step-3-Shooting-ms)
4. [Armada makhluk asing](Step-4-Alien-Fleet-ms)
5. [Pergerakan makhluk asing](Step-5-Alien-Movement-ms)
6. [Menembak makhluk asing](Step-6-Shooting-Aliens-ms)
7. [Penghadang](Step-7-Barriers-ms)
8. [Permainan tamat dan menang](Step-8-Game-Over-and-Win-ms)
9. [Skor dan nyawa](Step-9-Score-and-Lives-ms)

## Seterusnya

- [Bermula](Getting-Started-ms)
- [[('Bagaimana saya mendekati projek ini?', 'Saya merancang sebelum menulis kod. Projek dibahagikan kepada tiga gateway: persediaan, permainan itu sendiri dan dokumentasi. Permainan dibina dalam sembilan langkah kecil, setiap satu pada cabangnya sendiri dengan pull request, ujian, tangkapan skrin dan rekod semakannya sendiri, supaya sejarah menunjukkan bagaimana permainan berkembang. Segala yang tidak memerlukan tetingkap, seperti penghadan, susun atur armada, perlanggaran, selang masa gerakan dan keadaan permainan, diletakkan dalam `rules.py` supaya boleh diuji tanpa paparan.'), ('Apa yang sukar?', 'Menguji permainan berasaskan tetingkap. `turtle` memerlukan Tk dan paparan, jadi ujian yang membuka tetingkap tidak boleh dijalankan pada pelari integrasi berterusan atau pada desktop saya. Saya menyelesaikannya dengan imej Docker yang menjalankan permainan dan ujian pada paparan maya. Masa juga rumit: mengambil tangkapan skrin peluru yang sedang terbang atau armada yang telah bergerak memerlukan tekanan kekunci dan masa menunggu sepadan dengan gelung bingkai.'), ('Apa yang mudah?', 'Setelah peraturan dipisahkan daripada lukisan, logiknya pendek dan mudah diuji. Mewarisi `Turtle` untuk kapal, peluru, makhluk asing dan blok penghadang memberi setiap benda kelas kecilnya sendiri, dan pemalar dalam `constants.py` menjadikan penalaan permainan satu perubahan baris.'), ('Bagaimana saya boleh menambah baik untuk projek seterusnya?', 'Mulakan dengan persekitaran tangkapan skrin dan ujian sebelum baris pertama kod permainan, dan tulis ujian untuk sesuatu peraturan sebelum peraturan itu. Saya juga akan menjalankan peraturan imbasan saluran paip secara tempatan dengan cara yang sama seperti pelayan, supaya dapatan ditemui lebih awal.'), ('Apakah pembelajaran terbesar saya?', 'Memastikan peraturan permainan bebas daripada skrin adalah yang menjadikan projek grafik boleh diuji, dan gelung berasaskan masa (satu gerakan setiap saat) lebih ringkas dan lebih adil daripada mengira bingkai.'), ('Apa yang akan saya lakukan secara berbeza?', 'Saya akan melukis makhluk asing dan kapal sebagai bentuk khas dan bukan bentuk terbina dalam `turtle`, menambah bunyi dan senarai skor tertinggi, dan membiarkan armada menembak mengikut corak. Saya juga akan mengambil tangkapan skrin daripada permainan yang dirakam dan bukan daripada tekanan kekunci tunggal.')]](Reflection-ms)
- [Dokumen Projek](Project-Documents-ms)

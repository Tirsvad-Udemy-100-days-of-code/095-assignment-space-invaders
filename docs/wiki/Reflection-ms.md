[English](Reflection) · [Dansk](Reflection-da) · **Bahasa Malaysia**

# Refleksi

Jurnal refleksi kursus: bagaimana projek ini didekati dan apa yang diajarnya kepada saya.

## Bagaimana saya mendekati projek ini?

Saya merancang sebelum menulis kod. Projek dibahagikan kepada tiga gateway: persediaan, permainan itu sendiri dan dokumentasi. Permainan dibina dalam sembilan langkah kecil, setiap satu pada cabangnya sendiri dengan pull request, ujian, tangkapan skrin dan rekod semakannya sendiri, supaya sejarah menunjukkan bagaimana permainan berkembang. Segala yang tidak memerlukan tetingkap, seperti penghadan, susun atur armada, perlanggaran, selang masa gerakan dan keadaan permainan, diletakkan dalam `rules.py` supaya boleh diuji tanpa paparan.

## Apa yang sukar?

Menguji permainan berasaskan tetingkap. `turtle` memerlukan Tk dan paparan, jadi ujian yang membuka tetingkap tidak boleh dijalankan pada pelari integrasi berterusan atau pada desktop saya. Saya menyelesaikannya dengan imej Docker yang menjalankan permainan dan ujian pada paparan maya. Masa juga rumit: mengambil tangkapan skrin peluru yang sedang terbang atau armada yang telah bergerak memerlukan tekanan kekunci dan masa menunggu sepadan dengan gelung bingkai.

## Apa yang mudah?

Setelah peraturan dipisahkan daripada lukisan, logiknya pendek dan mudah diuji. Mewarisi `Turtle` untuk kapal, peluru, makhluk asing dan blok penghadang memberi setiap benda kelas kecilnya sendiri, dan pemalar dalam `constants.py` menjadikan penalaan permainan satu perubahan baris.

## Bagaimana saya boleh menambah baik untuk projek seterusnya?

Mulakan dengan persekitaran tangkapan skrin dan ujian sebelum baris pertama kod permainan, dan tulis ujian untuk sesuatu peraturan sebelum peraturan itu. Saya juga akan menjalankan peraturan imbasan saluran paip secara tempatan dengan cara yang sama seperti pelayan, supaya dapatan ditemui lebih awal.

## Apakah pembelajaran terbesar saya?

Memastikan peraturan permainan bebas daripada skrin adalah yang menjadikan projek grafik boleh diuji, dan gelung berasaskan masa (satu gerakan setiap saat) lebih ringkas dan lebih adil daripada mengira bingkai.

## Apa yang akan saya lakukan secara berbeza?

Saya akan melukis makhluk asing dan kapal sebagai bentuk khas dan bukan bentuk terbina dalam `turtle`, menambah bunyi dan senarai skor tertinggi, dan membiarkan armada menembak mengikut corak. Saya juga akan mengambil tangkapan skrin daripada permainan yang dirakam dan bukan daripada tekanan kekunci tunggal.

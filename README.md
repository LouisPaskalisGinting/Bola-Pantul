# Bola-Pantul
Proyek ini adalah permainan sederhana yang menggunakan OpenCV untuk mendeteksi wajah pemain dan menggerakkan paddle dalam permainan bola pantul. Game ini dilengkapi dengan fitur tombol "Start" untuk memulai permainan dan "Exit" untuk keluar setelah Game Over.

Fitur Utama
Deteksi Wajah: Paddle digerakkan menggunakan deteksi wajah dari kamera.
Tombol Start: Permainan hanya dimulai setelah pengguna menekan tombol "Start".
Tombol Exit: Ditampilkan setelah Game Over untuk keluar dari permainan.
Interaksi Sederhana: Gunakan mouse untuk mengklik tombol.
Skor: Menampilkan skor berdasarkan jumlah pantulan bola pada paddle.

## Prasyarat
1. Install python.
2. Install opencv.
   dengan cara :
   pip install opencv-python opencv-python-headless
3. Pastikan kamera berfungsi dengan baik.

## Cara menjalankan 
1. Clone atau Unduh Kode:
  - Clone repository atau unduh file Bola-Pantul.py.
2. Jalankan Script:
  - Buka terminal atau command prompt.
  - Jalankan perintah:
    -bash
    -python paddle_game.py

3. Mulai Bermain:
  - Layar akan menampilkan tombol "Start". Klik tombol untuk memulai permainan.
  - Gerakkan paddle dengan menggerakkan wajah di depan kamera.
4. Game Over:
  - Jika bola jatuh ke bawah, layar Game Over akan muncul.
  - Klik tombol "Mulai Lagi" untuk memulai kembali permainan, dan klik tombol "Exit" untuk keluar permainan.

    
## Struktur Kode
1. Konfigurasi Awal
  - Mengatur dimensi layar permainan, paddle, bola, dan kecepatan bola.

2. Deteksi Wajah
  - Menggunakan Haar Cascade untuk mendeteksi wajah pemain dan menggerakkan paddle secara horizontal.

3. Tombol Start dan Exit
  - tombol ditampilkan untuk interaksi:
    - Start: Memulai permainan.
    - Exit: Mengakhiri permainan setelah Game Over.
      
4. Gameplay
  - Bola memantul pada dinding dan paddle.
  - Skor bertambah setiap kali bola memantul pada paddle.

5. Game Over
  - Jika bola jatuh ke bawah layar, layar Game Over ditampilkan dengan skor akhir.

## Kontrol
  - Paddle: Gerakkan kepala di depan kamera.
  - Tombol:
    - Klik "Start" untuk memulai.
    - Klik "Exit" untuk keluar setelah Game Over.
  - Tombol Keyboard:
    - Tekan q untuk keluar kapan saja.
## Catatan
  - Pastikan kamera tidak terhalang agar deteksi wajah berjalan dengan baik.
  - Resolusi layar disesuaikan untuk tampilan optimal, tetapi dapat diubah sesuai kebutuhan.


   

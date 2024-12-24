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
  - Clone repository atau unduh pada branch master, file yang bernama Main.py.
2. Jalankan Script:
  - Buka terminal atau command prompt.
  - Jalankan perintah:
    python paddle_game.py

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
## Contributors 
| Full Name                    |     NIM   | Github Username                |
| Maleakhi Pratama Tobing      | 121140225 | LouisPaskalisGinting_121140066 |
| Louis Paskalis Ginting       | 121140066 | Male27                         |

## Logbook
| Date & Time                    | Project Progress and Updates    |
| ------------------------------ | ------------------------------- |
| December 11, 2024, at 08:28 PM | Perencanaan                     |
| December 22, 2024, at 03:36 AM | Drawing with index finger tip   |
| December 22, 2024, at 10:10 PM | penambahan Fitur Score          |
| December 23, 2024, at 01:27 AM | Percobaan ulang code            |
| December 24, 2024, at 19.00 PM | Pembuatan laporan               |

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


   

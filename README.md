# Bola-Pantul
Proyek ini adalah permainan sederhana yang menggunakan OpenCV untuk mendeteksi wajah pemain dan menggerakkan paddle dalam permainan bola pantul. Game ini dilengkapi dengan fitur tombol "Start" untuk memulai permainan dan "Exit" untuk keluar setelah Game Over.

Fitur Utama
Deteksi Wajah: Paddle digerakkan menggunakan deteksi wajah dari kamera.
Tombol Start: Permainan hanya dimulai setelah pengguna menekan tombol "Start".
Tombol Exit: Ditampilkan setelah Game Over untuk keluar dari permainan.
Interaksi Sederhana: Gunakan mouse untuk mengklik tombol.
Skor: Menampilkan skor berdasarkan jumlah pantulan bola pada paddle.

## Library yang digunakan
1. OpenCV
   Fungsi: Library ini digunakan untuk pengolahan citra dan video, serta akses kamera.
   Contoh penggunaan:
      - Membuka kamera dengan cv2.VideoCapture().
      - Menampilkan jendela permainan dengan cv2.imshow().
      - Menggambar elemen pada layar (seperti teks, rectangle, atau lingkaran) menggunakan cv2.rectangle(), cv2.circle(), dan cv2.putText().
      - Melakukan deteksi wajah dengan cv2.CascadeClassifier.
2. NumPy (numpy)
   Fungsi: Library ini digunakan untuk manipulasi array dan operasi numerik.
   Contoh penggunaan:
         - Membuat frame hitam (layar awal) dengan np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8).
   
## Contributors 
| Full Name                    |     NIM   | Github Username                |
|------------------------------| --------- | ------------------------------ |
| Maleakhi Pratama Tobing      | 121140225 | Male27                         |
| Louis Paskalis Ginting       | 121140066 | LouisPaskalisGinting_121140066 |

## Logbook
| Date & Time                    | Project Progress and Updates    |
| ------------------------------ | ------------------------------- |
| December 11, 2024, at 08:28 PM | Perencanaan                     |
| December 22, 2024, at 03:36 AM | Pembuatan code                  |
| December 22, 2024, at 10:10 PM | penambahan Fitur Score          |
| December 23, 2024, at 01:27 AM | Percobaan ulang code            |
| December 24, 2024, at 19.00 PM | Pembuatan laporan               |

## Instalasi 
1.Install dependencies dengan perintah berikut.
```sh
pip install -r requirements.txt
```
2. Jalankan program dengan perintah ini di terminal
```bash
   python main.py
```

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


   

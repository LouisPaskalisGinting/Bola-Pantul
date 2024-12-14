import cv2
import numpy as np

# Konfigurasi permainan
WIDTH, HEIGHT = 800, 600  # Dimensi layar game
paddle_width, paddle_height = 100, 20  # Dimensi paddle
paddle_y = HEIGHT - 50  # Posisi paddle (50 piksel dari bawah)
ball_radius = 10  # Jari-jari bola
ball_speed = 5  # Kecepatan bola

# Posisi awal paddle dan bola
paddle_x = WIDTH // 2 - paddle_width // 2
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = ball_speed, ball_speed

# Kamera     
cap = cv2.VideoCapture(3)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Warna
BLUE = (255, 0, 0)  # Warna balok
RED = (0, 0, 255)  # Warna bola
WHITE = (255, 255, 255)  # Warna teks

# Fungsi untuk menggambar elemen permainan
def draw_game(frame, paddle_x, paddle_y, ball_x, ball_y):
    # Gambar paddle
    cv2.rectangle(frame, (paddle_x, paddle_y), (paddle_x + paddle_width, paddle_y + paddle_height), BLUE, -1)
    # Gambar bola
    cv2.circle(frame, (ball_x, ball_y), ball_radius, RED, -1)
    return frame

# Loop permainan
while True:
    # Ambil frame dari kamera
    ret, frame = cap.read()
    if not ret:
        print("Kamera tidak tersedia!")
        break

    # Ubah ukuran frame agar sesuai dengan resolusi layar
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    
    # Balikkan frame (mirroring) agar gerakan pemain sesuai
    frame = cv2.flip(frame, 1)

    # Deteksi wajah
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Perbarui posisi paddle berdasarkan wajah
    if len(faces) > 0:
        x, y, w, h = faces[0]
        paddle_x = int((x + w // 2) * (WIDTH / frame.shape[1]) - paddle_width // 2)

    # Pastikan paddle tetap berada dalam batas layar
    paddle_x = max(0, min(WIDTH - paddle_width, paddle_x))

    # Perbarui posisi bola
    ball_x += ball_dx
    ball_y += ball_dy

    # Pantulan bola di dinding
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx = -ball_dx
    if ball_y - ball_radius <= 0:
        ball_dy = -ball_dy

    # Pantulan bola di paddle
    if (paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height and
            paddle_x <= ball_x <= paddle_x + paddle_width):
        ball_dy = -ball_dy

    # Game over jika bola jatuh ke bawah
    if ball_y > HEIGHT:
        cv2.putText(frame, "Game Over!", (WIDTH // 3, HEIGHT // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)
        cv2.imshow("Game", frame)
        cv2.waitKey(2000)
        break

    # Gambar elemen permainan di frame
    frame = draw_game(frame, paddle_x, paddle_y, ball_x, ball_y)

    # Tampilkan frame
    cv2.imshow("Game", frame)

    # keluar menggunakan tombol "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela
cap.release()
cv2.destroyAllWindows()

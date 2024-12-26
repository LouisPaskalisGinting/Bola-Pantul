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
cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Warna
BLUE = (255, 0, 0)  # Warna paddle
RED = (0, 0, 255)  # Warna bola
WHITE = (255, 255, 255)  # Warna teks
GREEN = (0, 255, 0)  # Warna tombol Start dan Exit

# Skor
score = 0
start_button_rect = (WIDTH // 2 - 60, HEIGHT // 2 - 50, 120, 50)  # Tombol Start di tengah layar
exit_button_rect = (WIDTH // 2 - 60, HEIGHT // 2 + 50, 120, 50)  # Tombol Exit di tengah layar
replay_button_rect = (WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)  # tombol main lagi


# Fungsi untuk menggambar layar Start
def draw_start_screen(frame):
    # Teks judul
    cv2.putText(frame, "Selamat Datang Di Game Bola Pantul!", (WIDTH // 6, HEIGHT // 3), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)

    # Tombol Start
    x, y, w, h = start_button_rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, -1)
    cv2.putText(frame, "Start", (x + 20, y + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)
    return frame

# Fungsi untuk menggambar elemen permainan
def draw_game(frame, paddle_x, paddle_y, ball_x, ball_y, score):
    # Gambar paddle
    cv2.rectangle(frame, (paddle_x, paddle_y), (paddle_x + paddle_width, paddle_y + paddle_height), BLUE, -1)
    # Gambar bola
    cv2.circle(frame, (ball_x, ball_y), ball_radius, RED, -1)
    # Tampilkan skor
    cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)
    return frame

# Fungsi untuk menggambar layar Game Over
def draw_game_over(frame, score):
    # Teks Game Over
    cv2.putText(frame, "Game Over!", (WIDTH // 3, HEIGHT // 3), cv2.FONT_HERSHEY_SIMPLEX, 2, WHITE, 3)
    # Skor akhir
    cv2.putText(frame, f"Score Anda: {score}", (WIDTH // 3, HEIGHT // 3 + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)

    # Tombol Exit
    x, y, w, h = exit_button_rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), RED, -1)
    cv2.putText(frame, "Exit", (x + 20, y + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)

    # Tombol Main Lagi
    replay_x, replay_y, replay_w, replay_h = replay_button_rect
    cv2.rectangle(frame, (replay_x, replay_y), (replay_x + replay_w, replay_y + replay_h), BLUE, -1)
    cv2.putText(frame, "Main Lagi", (replay_x + 5, replay_y + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)

    return frame

# Fungsi untuk memeriksa klik pada tombol
def is_button_clicked(event, x, y, flags, param):
    global running, game_started, game_over
    if event == cv2.EVENT_LBUTTONDOWN:
        # Cek klik tombol Start
        btn_x, btn_y, btn_w, btn_h = start_button_rect
        if not game_started and btn_x <= x <= btn_x + btn_w and btn_y <= y <= btn_y + btn_h:
            game_started = True

        # Cek klik tombol Exit
        btn_x, btn_y, btn_w, btn_h = exit_button_rect
        if game_over and btn_x <= x <= btn_x + btn_w and btn_y <= y <= btn_y + btn_h:
            running = False

        # Cek klik tombol Main Lagi
        replay_x, replay_y, replay_w, replay_h = replay_button_rect
        if game_over and replay_x <= x <= replay_x + replay_w and replay_y <= y <= replay_y + replay_h:
            restart_game()

# Fungsi untuk mereset permainan
def restart_game():
    global paddle_x, ball_x, ball_y, ball_dx, ball_dy, score, game_over, game_started
    paddle_x = WIDTH // 2 - paddle_width // 2  # Reset posisi paddle
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Reset posisi bola
    ball_dx, ball_dy = ball_speed, ball_speed  # Reset kecepatan bola
    score = 0  # Reset skor
    game_over = False  # Hapus status Game Over
    game_started = True  # Mulai ulang permainan

# Loop permainan
running = True
game_started = False
game_over = False
cv2.namedWindow("Game")
cv2.setMouseCallback("Game", is_button_clicked)

while running:
    if not game_started:
        # Tampilkan layar Start
        frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        frame = draw_start_screen(frame)
        cv2.imshow("Game", frame)

        # Tunggu input
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    if game_over:
        # Tampilkan layar Game Over
        frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        frame = draw_game_over(frame, score)
        cv2.imshow("Game", frame)

        # Tunggu input
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

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
        score += 1  # Tambah skor setiap kali bola memantul pada paddle

    # Game over jika bola jatuh ke bawah
    if ball_y > HEIGHT:
        game_over = True
        continue

    # Gambar elemen permainan di frame
    frame = draw_game(frame, paddle_x, paddle_y, ball_x, ball_y, score)

    # Tampilkan frame
    cv2.imshow("Game", frame)

    # keluar menggunakan tombol "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela
cap.release()
cv2.destroyAllWindows()

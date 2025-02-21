import cv2 as cv
import numpy as np
import random
import time

cap = cv.VideoCapture(0)

colors_ranges = {
    "red": ([0, 100, 100], [10, 255, 255]),
    "oranye": ([11, 100, 100], [25, 255, 255]),
    "kuning": ([26, 100, 100], [35, 255, 255]),
    "hijau": ([36, 100, 100], [85, 255, 255]),
    "biru": ([96, 100, 100], [130, 255, 255]),
    "putih": ([0, 0, 200], [180, 30, 255]),
    "hitam": ([0, 0, 0], [180, 255, 50]),
}

colors_list = [i for i in colors_ranges.keys()]
target_color = colors_list[random.randint(0, 100)%7]
already_detected_color = []
tidak_memiliki_warna = []
found = False
start_time = None
next_color = None

while cap.isOpened():
    # Membaca webcam
    success, frame = cap.read()

    # Mengatur ulang ukuran webcam yang akan ditampilkan
    resize = cv.resize(frame, (1280, 720))

    if not success:
        print("Tidak dapat merender frame!")
        break
    
    # Merubah format warna dari BGR ke HSV
    hsv_frame = cv.cvtColor(resize, cv.COLOR_BGR2HSV)

    colors_remaining = [color for color in colors_list if color not in already_detected_color and color not in tidak_memiliki_warna]

    # Menyimpan nilai array pertama dan kedua dari dictionary
    lower_value, upper_value = np.array(colors_ranges[target_color][0]), np.array(colors_ranges[target_color][1])

    # Masking
    mask = cv.inRange(hsv_frame, lower_value, upper_value)
    masking_result = cv.bitwise_and(resize, resize, mask=mask)

    if target_color:
        cv.putText(resize, f"Find = {target_color}", (50, 50), cv.FONT_HERSHEY_COMPLEX, 1.1, (255, 0, 0), 2, cv.LINE_AA)
    else:
        cv.putText(resize, "Semua warna sudah pernah terdeteksi", (50, 50), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2, cv.LINE_AA)
        break

    # Mendeteksi batas-batas (kontur) dari objek yang ada dalam gambar biner (mask).
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Jika terdapat kontur
    if contours:
        for contour in contours:
            area = cv.contourArea(contour) # Hitung luas kontur
            if area > 1000: #Jika luas benda lebih dari 1000px

                # Menggambar semua kontur yang ada di dalam frame
                cv.drawContours(resize, contours, -1, (0, 255, 0), 3)
                cv.putText(resize, "Warna Ditemukan!", (1280 - 350, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)

                # Warna sesuai (sudah ditemukan)
                found = True
                already_detected_color.append(target_color)
                
                # Catat waktu awal saat berhasil ditemukan
                start_time = time.time() 

    if found and start_time is not None:
        # Hitung waktu yang sudah jalan sejak waktu awal dicatat
        elapsed_time = time.time() - start_time

        # Waktu tersisa sebelum berganti secara otomatis ke warna yang lain
        remaining_time = max(10 - int(elapsed_time), 0)
        cv.putText(resize, f"Next color in: {remaining_time}s", (50, 100), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)

        # Jika waktu yang dijalani lebih dari 10 detik, maka akan mengubah warna yang harus dicari dan mereset beberapa kondisi
        if elapsed_time >= 10:
            if len(colors_remaining) > 0:
                next_color = random.choice(colors_remaining)
                target_color = next_color
            else:
                print("tidak ada warna tersisa")
                break

            # Reset kondisi ditemukannya warna
            found = False

            # Reset waktu ditemukannya warna
            start_time = None
    
    # Menampilkan frame webcam
    cv.imshow("Cari Warna", resize)

    # Menampilkan frame hasil masking
    cv.imshow("Hasil Masking", masking_result)

    # Jika pemain stuck dan tidak dapat menemukan benda yang sesuai warnanya, maka dapat menekan tombol n untuk pilihan warna yang lain
    if cv.waitKey(1) & 0xFF == ord("n"):
        tidak_memiliki_warna.append(target_color)
        if len(colors_remaining) > 0:
            next_color = random.choice(colors_remaining)
            target_color = next_color
        else:
            print("Tidak ada warna tersisa")
            break
    
    # Keluar dari program
    elif cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
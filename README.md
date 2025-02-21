# Permainan Mencari Warna

## Gambaran Permainan

Merupakan permaian di mana pemain ditugaskan untuk menggunakan barang disekitar mereka atau hal-hal yang memiliki warna yang telah ditentukan oleh program.

## Tujuan Proyek

Proyek ini dibuat sebagai sarana pendalaman dan pembiasaan dalam penggunaan library [OpenCV](https://opencv.org/). Sekaligus salah satu syarat dalam open recruitment ROBOTIIK FILKOM UB. Segala kritik dan saran sangat diterima dalam proyek ini.

## Instalasi

Proyek dapat di install dengan cara

```bash
git clone https://github.com/MadutttYa/Challenge-Programming-OPREC-RnD.git
```

Sebelumnya pastikan sudah menginstall library yang dibutuhkan yaitu :

1. OpenCV ([link dokumentasi installasi](https://opencv.org/get-started/?utm_source=opcv&utm_medium=home))

```bash
pip3 install opencv-python
```

2. Numpy ([link dokumentasi installasi](https://numpy.org/install/))

```bash
pip3 install numpy
```

Setelahnya anda hanya perlu mengetikan kode di bawah ini untuk menjalankan kode.

```bash
python3 cari_warna.py
```

## Cara Bermain

1. Run file python **`cari_warna.py`**, tunggu hingga webcam laptop/komputer anda muncul. Jika ternyata webcam anda tidak terdeteksi, anda bisa mengubah variabel **`cap`** dengan angka sampai webcam anda terdeteksi.

2. Setelahnya akan ada text Find : ..., artinya anda diminta untuk mencari benda dengan warna tersebut. Untuk saat ini belum ada implementasi time limit sehingga ada dapat menggunakan waktu anda sampai menemukan barang dengan warna terkait. Akan ada timer 10 detik sebelum warna selanjutnya jika anda berhasil menemukan barang dengan warna tersebut.
   \*Perlu diperhatikan, saat sudah terdeteksi warnanya, agar timer berjalan anda perlu menyingkirkan barang tersebut sampai tidak terdeteksi oleh program.

3. Game akan diloop sampai semua warna terdeteksi atau tidak ada sisa warna lagi yang perlu dideteksi.

## Demonstrasi Kode



https://github.com/user-attachments/assets/426645a5-1cf8-4053-bc00-060d5260d851

Jika video tidak dapat terputar anda dapat mendowloadnya dari folder Dokumentasi dan Demonstrasi


## Kontrol

- Tekan "n" untuk skip warna jika diinginkan, program akan langsung menganggap anda tidak memiliki benda dengan warna terkait sehingga warna tersebut tidak akan muncul lagi.

- Tekan "q" untuk keluar dari program.

## Kontribusi

Anda dapat memperbaharui atau menambahkan fitur dalam proyek ini dengan cara mem-fork repository ini dan membuat pull request.

## Kontak

Segala kritik dan masukan dapat disampaikan pada michaeladitya006@gmail.com

## Lisensi

[MIT](LICENSE.txt)

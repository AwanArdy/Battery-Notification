## Battery Monitor Notification🔋

**Battery Monitor Notification** adalah program Python sederhana yang memantau status baterai laptop dan menampilkan pop-up peringatan ketika baterai sudah penuh (100%) dan charger masih terpasang. Program ini membantu pengguna untuk menjaga kondisi baterai dengan mengingatkan mereka agar mencabut charger ketika baterai penuh.

### Fitur
- Memantau level baterai dan status pengisian daya setiap menit
- Menampilkan pop-up notifikasi tanpa tombol "Close" ketika baterai penuh dan charger masih terpasang
- Pop-up akan otomatis tertutup ketika charger dicabut
- Dapat berjalan otomatis saat laptop dinyalakan (dengan konfigurasi startup)

### Prasyarat
Program ini membutuhkan Python versi 3.x dan dua library tambahan:
1. **psutil:** untuk memantau status baterai dan pengisian daya
2. **tkinter:** library GUI bawaan Python, digunakan untuk membuat pop-up

### Instalasi library
Untuk menginstal `psutil`, gunakan perintah pip berikut:
`pip install psutil`

**Catatan:** `tkinter` biasanya sudah tersedia secara default di instalasi Python pada Windows dan MacOS. Namun, jika kamu menggunakan Linux dan tkinter belum terpasang. Kamu dapat menginstalnya melalui package manager dengan perintah berikut:

**Ubuntu/Debian:**
`sudo apt-get install python3-tk`

**Fedora:**
`sudo dnf install python3-tkinter`

### Cara menjalankan program
1. `git clone https://github.com/`
2. Jalankan program dengan perintah berikut:
`python3 main.py`
Program akan berjalan di latar belakang dan memantau status baterai laptop setiap 1 menit
3. Menambah ke startup (Opsional)
Agar program ini berjalan otomatis saat laptop dinyalakan, kamu bisa menambhkan ke folder Startup di Windows atau membuat file .desktop di Linux
  - **Windows:** Pindahkan shortcut program ke folder `shell:startup`
  - **Linux:** Buat file .desktop di `~/./config/autostart/`

### Catatan tambahan
- Program ini memantau status baterai setiap 1 menit secara default. Interval ini dapat diubah dengan mengedit nilai pada `time.sleep(60)` di bagian akhir kode.
- Pop-up hanya muncul jika baterai mencapai 100% dan charger masih terpasang

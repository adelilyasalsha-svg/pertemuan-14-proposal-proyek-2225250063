# PROPOSAL PROYEK
# Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Latar Belakang

Pengolahan nilai siswa merupakan salah satu kegiatan yang dilakukan oleh guru matematika untuk mengetahui hasil belajar siswa. Proses pengolahan nilai secara manual membutuhkan waktu dan berpotensi menimbulkan kesalahan dalam perhitungan. Oleh karena itu, diperlukan program sederhana menggunakan Python untuk membantu membaca data nilai, menghitung statistik, menentukan ketuntasan, dan menyimpan hasil analisis ke dalam file.

## 2. Pengguna dan Tujuan

**Pengguna:** Guru matematika.

**Tujuan:**
1. Mempermudah proses rekapitulasi nilai siswa.
2. Memvalidasi nilai siswa agar berada pada rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan maksimum.
4. Menentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM.
5. Menyimpan hasil analisis dalam file teks.

## 3. Ruang Lingkup

Fitur wajib:
1. Membaca data nilai siswa dari file teks.
2. Memvalidasi nilai dalam rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan maksimum.
4. Menentukan status ketuntasan berdasarkan KKM.
5. Menyimpan laporan hasil analisis ke file teks.

Batasan proyek:
- Program berbasis terminal atau console.
- Menggunakan bahasa pemrograman Python.
- Data disimpan dalam file teks sederhana.
- Tidak menggunakan antarmuka web atau grafis.

## 4. Kebutuhan Proyek

### A. Kebutuhan Fungsional
- Program dapat membaca data nilai siswa dari file.
- Program dapat memeriksa format dan rentang nilai.
- Program dapat menghitung statistik nilai.
- Program dapat menentukan status ketuntasan siswa.
- Program dapat menyimpan laporan hasil analisis.

### B. Kebutuhan Nonfungsional
- Program mudah dijalankan melalui terminal VS Code.
- Pesan kesalahan mudah dipahami.
- Nama fungsi dan variabel jelas.
- Data contoh tidak menggunakan informasi pribadi nyata.
- Hasil program dapat diperiksa menggunakan test case yang sama.

## 5. Input, Proses, dan Output

**Input:**
- File berisi nama dan nilai siswa.
- Nilai Kriteria Ketuntasan Minimal (KKM).

**Proses:**
1. Membaca data dari file.
2. Memeriksa format dan rentang nilai.
3. Memisahkan data valid dan data tidak valid.
4. Menghitung rata-rata, minimum, dan maksimum.
5. Menentukan status ketuntasan berdasarkan KKM.
6. Menyusun dan menyimpan laporan.

**Output:**
- Rata-rata nilai kelas.
- Nilai minimum dan maksimum.
- Jumlah siswa tuntas.
- Jumlah siswa belum tuntas.
- File laporan hasil analisis.

## 6. Algoritma atau Pseudocode

MULAI

1. Baca data nilai dari file.
2. Jika file tidak ditemukan, tampilkan pesan kesalahan.
3. Periksa format dan rentang setiap nilai.
4. Simpan data yang valid.
5. Jika tidak ada data valid, tampilkan pesan.
6. Hitung rata-rata, minimum, dan maksimum.
7. Tentukan status ketuntasan berdasarkan KKM.
8. Hitung jumlah siswa tuntas dan belum tuntas.
9. Tampilkan hasil analisis.
10. Simpan laporan ke file teks.

SELESAI

## 7. Struktur Program dan Modularisasi

Program dirancang menjadi beberapa modul dengan tanggung jawab berbeda.

- `main.py`: mengatur alur utama program.
- `data_io.py`: membaca data dan menyimpan laporan.
- `analisis.py`: memvalidasi nilai, menghitung statistik, dan menentukan ketuntasan.
- `utilitas.py`: menyediakan fungsi pendukung.

Pembagian modul bertujuan agar program lebih terstruktur, mudah diuji, dan mudah dikembangkan.

## 8. Struktur Data

- **List:** menyimpan kumpulan nilai siswa.
- **Dictionary:** menyimpan data siswa yang terdiri atas nama dan nilai.
- **String:** menyusun pesan dan laporan.
- **File teks:** menyimpan data masukan dan laporan keluaran.

Struktur data tersebut dipilih karena sesuai dengan kebutuhan pengolahan data siswa yang sederhana.

## 9. Rancangan Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | Invalid | File tidak ditemukan | Kesalahan ditangani |
| TC06 | Normal | Semua nilai lebih besar atau sama dengan KKM | Semua siswa dinyatakan tuntas |

Test case dirancang sebelum implementasi penuh dan akan digunakan untuk memeriksa hasil program pada tahap pengembangan berikutnya.

## 10. Pembagian Tugas

Pembagian tugas dilakukan berdasarkan tanggung jawab masing-masing anggota kelompok.

- **Koordinator:** mengawasi rancangan dan integrasi proyek.
- **Programmer Data I/O:** menangani rancangan pembacaan data dan penyimpanan laporan.
- **Programmer Logika:** menangani rancangan perhitungan statistik dan ketuntasan.
- **Tester/QA:** menyusun serta memeriksa test case.
- **Dokumentasi:** menyusun README dan proposal proyek.

Nama penanggung jawab atau PIC disesuaikan dengan anggota kelompok yang sebenarnya. Satu anggota dapat memegang lebih dari satu peran sesuai kebutuhan kelompok.

## 11. Jadwal Pelaksanaan

- **Pertemuan 14:** menyusun proposal, struktur folder, pseudocode, test case, dan pembagian tugas.
- **Pertemuan 15:** mengimplementasikan program, melakukan integrasi, pengujian, debugging, dan dokumentasi.
- **Pertemuan 16:** melakukan presentasi, demonstrasi program, dan evaluasi.

## 12. Repository GitHub

Nama repository: `pertemuan-14-proposal-proyek-2225250063`

URL repository: isi dengan URL GitHub yang sebenarnya setelah repository dibuat.

## Penutup

Rancangan proyek ini diharapkan menjadi pedoman dalam pengembangan program rekap dan analisis nilai matematika kelas. Dengan adanya pembagian modul, struktur data yang sesuai, serta test case sejak tahap perancangan, proses implementasi dan pengujian diharapkan dapat dilakukan secara lebih terarah.
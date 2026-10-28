# Program Rekap dan Analisis Nilai Matematika Kelas

## Deskripsi Proyek

Proyek ini merupakan rancangan program sederhana menggunakan Python untuk membantu guru matematika mengolah dan menganalisis nilai siswa. Program dirancang untuk membaca data nilai dari file, memvalidasi data, menghitung statistik nilai, menentukan ketuntasan, dan menyimpan laporan hasil analisis.

Proyek ini dibuat untuk memenuhi tugas Algoritma dan Pemrograman Pertemuan 14, yaitu perancangan proyek program sederhana menggunakan VS Code dan GitHub.

## Tujuan

- Mempermudah rekapitulasi nilai siswa.
- Memvalidasi nilai dalam rentang 0–100.
- Menghitung rata-rata, nilai minimum, dan maksimum.
- Menentukan status ketuntasan berdasarkan KKM.
- Menyimpan hasil analisis ke dalam file teks.

## Fitur yang Direncanakan

1. Membaca data nilai siswa.
2. Memvalidasi data dan rentang nilai.
3. Menghitung statistik nilai kelas.
4. Menghitung jumlah siswa tuntas dan belum tuntas.
5. Menyimpan laporan hasil analisis.

## Teknologi

- Python 3
- Visual Studio Code
- Git
- GitHub

## Struktur Folder

```text
pertemuan-14-proposal-proyek-2225250063/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

## Data Contoh

File `data/nilai_contoh.txt` menggunakan format nama dan nilai yang dipisahkan tanda koma.

```text
Ayu,85
Budi,78
Citra,90
Deni,65
Eka,100
```

## Pembagian Modul

- `main.py`: mengatur alur utama program.
- `data_io.py`: membaca data dan menyimpan laporan.
- `analisis.py`: memvalidasi nilai, menghitung statistik, dan menentukan ketuntasan.
- `utilitas.py`: menyediakan fungsi pendukung.

## Pengujian

Rancangan pengujian disimpan pada `tests/test_case.md` dan mencakup kondisi normal, batas, serta input tidak valid.

## Cara Menjalankan

Setelah implementasi program selesai, buka terminal pada folder utama proyek dan jalankan:

```bash
python -m src.main
```

Pastikan Python 3 sudah terpasang dan struktur folder sesuai dengan dokumentasi.

## Status Proyek

**Tahap perancangan — Pertemuan 14.**

Implementasi, pengujian aktual, debugging, dan penyempurnaan dokumentasi dilanjutkan pada Pertemuan 15.

## Repository

URL GitHub: isi dengan tautan repository proyek yang sebenarnya.
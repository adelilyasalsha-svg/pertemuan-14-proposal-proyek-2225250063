from data_io import baca_data, simpan_laporan
from analisis import (
    validasi_nilai,
    hitung_statistik,
    tentukan_status
)


def main():
    try:
        data = baca_data("data/nilai_contoh.txt")
    except FileNotFoundError:
        print("File data tidak ditemukan.")
        return

    data_valid = [
        siswa for siswa in data
        if validasi_nilai(siswa["nilai"])
    ]

    if not data_valid:
        print("Tidak ada data nilai yang valid.")
        return

    nilai = [siswa["nilai"] for siswa in data_valid]
    statistik = hitung_statistik(nilai)
    kkm = 75

    tuntas = sum(
        tentukan_status(n, kkm) == "Tuntas"
        for n in nilai
    )

    belum_tuntas = len(nilai) - tuntas

    laporan = (
        "REKAP NILAI MATEMATIKA\n"
        f"Rata-rata: {statistik['rata_rata']:.2f}\n"
        f"Minimum: {statistik['minimum']}\n"
        f"Maksimum: {statistik['maksimum']}\n"
        f"Jumlah tuntas: {tuntas}\n"
        f"Jumlah belum tuntas: {belum_tuntas}\n"
    )

    print(laporan)
    simpan_laporan("output/laporan.txt", laporan)


if __name__ == "__main__":
    main()

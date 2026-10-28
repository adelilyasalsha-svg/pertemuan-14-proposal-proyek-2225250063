def baca_data(path):
    data = []

    with open(path, "r", encoding="utf-8") as file:
        for baris in file:
            bagian = baris.strip().split(",")

            if len(bagian) != 2:
                continue

            nama, nilai = bagian

            try:
                nilai = float(nilai)
                data.append({
                    "nama": nama,
                    "nilai": nilai
                })
            except ValueError:
                continue

    return data


def simpan_laporan(path, isi):
    with open(path, "w", encoding="utf-8") as file:
        file.write(isi)

def validasi_nilai(nilai):
    return 0 <= nilai <= 100


def hitung_statistik(nilai):
    if not nilai:
        return {}

    return {
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai)
    }


def tentukan_status(nilai, kkm):
    if nilai >= kkm:
        return "Tuntas"
    return "Belum Tuntas"

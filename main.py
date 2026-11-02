data_inti = [5, 8, 11, 14, 18, 22, 27, 9, 16, 24,
            12, 30, 7, 20, 15]
data_tambahan = [3, 10, 19, 20, 35]
data_snr = data_inti + data_tambahan


def rata_rata(data):
    if not data:
        return 0.0

    total = 0
    for nilai in data:
        total += nilai
    return total / len(data)


def kualitas_sinyal(snr):
    if snr < 10:
        return "RENDAH"
    elif 10 <= snr < 20:
        return "BAIK"
    else:
        return "SANGAT BAIK"


def hitung_kategori(data):
    rendah = 0
    baik = 0
    sangat_baik = 0

    for snr in data:
        status = kualitas_sinyal(snr)
        if status == "RENDAH":
            rendah += 1
        elif status == "BAIK":
            baik += 1
        else:
            sangat_baik += 1

    return rendah, baik, sangat_baik


def main():
    print("---TELECOMMUNICATION SIGNAL MONITORING---")

    for i in range(len(data_snr)):
        snr = data_snr[i]
        status = kualitas_sinyal(snr)
        print(i + 1, "-", snr, "dB ->", status)

    rendah, baik, sangat_baik = hitung_kategori(data_snr)
    average = rata_rata(data_snr)

    print()
    print("=== RINGKASAN ===")
    print("Total Data:", len(data_snr))
    print("RENDAH:", rendah)
    print("BAIK:", baik)
    print("SANGAT BAIK:", sangat_baik)
    print("Rata_rata SNR:", round(average, 2), "dB")
    print("Minimum:", min(data_snr), "dB")
    print("Maksimum:", max(data_snr), "dB") 
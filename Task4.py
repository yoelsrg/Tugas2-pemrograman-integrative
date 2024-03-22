def main():
    # Inisialisasi list kosong untuk menyimpan nilai-nilai
    nilai = []

    # Masukkan nilai-nilai hingga ditemukan -1
    while True:
        nilai_saat_ini = input("Masukkan sebuah nilai (atau -1 untuk mengakhiri): ")
        if nilai_saat_ini == '-1':
            break
        nilai.append(int(nilai_saat_ini))

    # Hitung rata-rata dari nilai-nilai
    rata_rata = sum(nilai) // len(nilai)

    # Output rata-rata
    print(rata_rata)

    # Output nilai-nilai dalam urutan yang dimasukkan
    for nilai_satu in nilai:
        print(nilai_satu)

if __name__ == "__main__":
    main()

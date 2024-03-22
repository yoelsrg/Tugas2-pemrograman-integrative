def main():
    total = 0

    # Membuat array untuk menyimpan angka
    numbers = []

    # Meminta pengguna untuk memasukkan angka dalam satu baris
    input_string = input("Masukkan angka (dipisahkan spasi, atau ketik -1 untuk mengakhiri): ")

    # Memisahkan string masukan menjadi angka-angka individu
    num_list = input_string.split()

    # Mengkonversi setiap angka dalam list menjadi float dan menambahkannya ke dalam array
    for num in num_list:
        if num == '-1':
            break
        numbers.append(float(num))

    # Menghitung total dari semua angka dalam array
    for num in numbers:
        total += num

    # Cetak total dengan dua digit setelah koma
    print("Total:", "{:.2f}".format(total))

if __name__ == "__main__":
    main()

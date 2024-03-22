from datetime import datetime, timedelta

def main():
    # Masukkan jumlah hari
    num_days = int(input("Masukkan jumlah hari dari sekarang: "))

    # Dapatkan tanggal saat ini
    tanggal_sekarang = datetime.now()

    # Hitung tanggal di masa depan
    tanggal_mendatang = tanggal_sekarang + timedelta(days=num_days)

    # Format tanggal di masa depan sesuai dengan format yang ditentukan
    tanggal_terformat = tanggal_mendatang.strftime("%A, %d %B %Y")

    # Cetak tanggal yang diformat
    print("Tanggal", num_days, "hari dari sekarang adalah:", tanggal_terformat)

if __name__ == "__main__":
    main()

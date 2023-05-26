from tabulate import tabulate
daftarBelanja = []
nomor = 1
total = 0

print("KASIR SEDERHANA")

while True:
    namaBarang = input(f"Masukan nama barang ke {nomor} : ")
    hargaBarang = int(input("Masukan harga barang : "))
    jumlahBarang = int(input("Masukan jumlah barang : "))
    totalHarga = hargaBarang * jumlahBarang
    diskon = totalHarga - (0.25 * totalHarga)
    daftarBelanja.append([nomor, namaBarang, hargaBarang, jumlahBarang, totalHarga, diskon])
    nomor += 1
    total += diskon
    lanjut = input("\nmau tambah belanjaan [Y/t]? ").lower()
    if lanjut != 'y':
        break

header = ["Nomor", "Nama", "Harga", "Jumlah", "total harga", "harga diskon"]
print(tabulate(daftarBelanja, headers=header))
print(f"\nTotal Harga : {total}")
# print(daftarBelanja)
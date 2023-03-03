# deklarasi variabel
dataMahasiswa = [
    ["Yoga Agustiansyah", "Udin Gambut"], #data berisi nama
    ["2206050", "2101234"], #data berisi NIM
    ["Teknik INformatika", "Teknik Informatika"], #data berisi prodi
    ["Garut", "Sumedang"], #data berisi tempat lahir
    ["22 Agustus 2002", "25 Desember 2002"] #data berisi tanggal lahir
]
# menampilkan data mahasiswa default
print("\t\t---Daftar Mahasiswa---")
for i in range(len(dataMahasiswa[0])):
    print(f"""{i+1}
    Nama\t\t\t: {dataMahasiswa[0][i]}
    NIM\t\t\t\t: {dataMahasiswa[1][i]}
    Program Studi\t\t: {dataMahasiswa[2][i]}
    Tempat, tanggal lahir\t: {dataMahasiswa[3][i]}, {dataMahasiswa[4][i]}
    """)
# konfirmasi apakah data mahasiswa ingin ditambah atau tidak
tambah = input("Ingin menambah daftar mahasiswa(Y/t)? ").lower()
# penambahan data mahasiswa jika ingin ditambah
while tambah =="y":
    nama = input("Masukan Nama\t\t: ")
    nim = input("Masukan NIM\t\t: ")
    prodi = input("Masukan Program Studi\t: ")
    tempatLahir = input("Masukan Tempat Lahir\t: ")
    tanggalLahir = input("Masukan Tanggal lahir\t: ")
    dataMahasiswa[0].append(nama)
    dataMahasiswa[1].append(nim)
    dataMahasiswa[2].append(prodi)
    dataMahasiswa[3].append(tempatLahir)
    dataMahasiswa[4].append(tanggalLahir)
# konfirmasi apakah data mahasiswa ingin ditambah lagi atau tidak
    tambah = input("\nIngin menambah daftar mahasiswa lagi(Y/t)? ").lower()
# menampilkan data mahasiswa terbari
print("\n\t---Daftar Mahasiswa Akhir---")
for i in range(len(dataMahasiswa[0])):
    print(f"""{i+1}
    Nama\t\t\t: {dataMahasiswa[0][i]}
    NIM\t\t\t\t: {dataMahasiswa[1][i]}
    Program Studi\t\t: {dataMahasiswa[2][i]}
    Tempat, tanggal lahir\t: {dataMahasiswa[3][i]}, {dataMahasiswa[4][i]}
    """)
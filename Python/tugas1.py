print ("\tTugas 1 Praktikum Dasar Dasar Pemrograman")
print("\t"+"_"*41)
nama = input("Masukan nama anda \t\t: ")
nim = input("Masukan nama NIM \t\t: ")
kelas = input("Masukan kelas anda \t\t: ")
angkatan = input("Masukan tahun angkatan anda \t: ")
alamat = input("Masukan alamat anda \t\t: ")
hidup = input("Apakah anda masih hidup ? (Y/n)")

if hidup == "Y" or hidup == "y" : greeting = "Semoga hari anda menyenangkan"
else: greeting = "semoga anda tenang di alam sana"

# data = ("Hallo {}".format(nama))
print("\t"+"_"*41)
dataDiri = (f"Hallo {nama} dengan NIM {nim} dari kelas {kelas} angkatan tahun {angkatan}.\nAlamat anda berada di {alamat}. {greeting}")
print(dataDiri)
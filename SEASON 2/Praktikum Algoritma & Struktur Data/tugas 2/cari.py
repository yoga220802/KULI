nilai = [7, 12 ,19, 97, 23]
ketemu = False
urutan = 0

for i in nilai:
    print(i, end=" | ")

cari = int(input("\nMasukan angka yang ingin dicari : "))

for i in range(len(nilai)):
    if nilai[i] == cari:
        ketemu = True
        urutan = i
    
if ketemu:
    print(f"nilai yang anda cari ditemukan pada index ke - {urutan}")
else:
    print("nilai yang anda cari tidak ditemukan")
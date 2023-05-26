nilai = [7, 12, 19, 97, 23]

print("Data lama", end=" : ")

for i in nilai:
    print(i, end=" | ")

hapus = int(input("\ndata yang ingin dihapus : "))
nilai.remove(hapus)

# for i in range(hapus-1, len(nilai) -1):
#     nilai[i] = nilai[i+1]

print("data baru", end=" : ")
for i in range(len(nilai)):
    print(nilai[i], end=" | ")
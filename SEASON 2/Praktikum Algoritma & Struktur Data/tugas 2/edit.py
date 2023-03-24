nilai = [7, 12, 19, 97, 23]

print("Sebelum diubah", end=" : ")
for i in nilai:
    print(i, end=" | ")

# print("\n\nInput ubah nilai")
# for i in range(len(nilai)):
#     nilai[i] = int(input(f"Masukan data baru untuk nilai di index ke {i} : "))

indexInput = int(input("masukan index array yang ingin diubah"))
nilai[indexInput] = int(input(f"Masukan nilai baru untuk data di index ke - {indexInput}"))
    
print("\n\nSetelah diubah", end=" : ")
for i in nilai:
    print(i, end=" | ")
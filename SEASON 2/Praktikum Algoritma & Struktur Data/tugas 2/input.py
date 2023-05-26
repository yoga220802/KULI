nilai = [7, 12, 19]

print("Sebelum ditambah")
for i in range(len(nilai)):
    print(f"nilai pada index ke-{i} = {nilai[i]}")

nilai.append(int(input("\nMasukan nilai untuk index ke 3 ")))
nilai.append(int(input("\nMasukan nilai untuk index ke 4 ")))

print("Setelah ditambah")
for i in range(len(nilai)):
    print(f"nilai pada index ke-{i} = {nilai[i]}")

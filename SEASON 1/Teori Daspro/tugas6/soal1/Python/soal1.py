jml = 0
for angka in range(1, 300):
    n = 0
    for i in range(2, angka):
        if int(angka % i) == 0:
            n += 1
            break

    if n == 0 and angka != 1:
        print(angka, end=", ")
        jml += angka

print("Jumlah total = ", jml)

# Bagian Nama Program
namaProgram = "Kalkulator Sederhana"
print(f"\t{namaProgram}")
print("\t"+"-"*len(namaProgram))
# Bagian Inti Kalkulator
AKAR_DUA = 0.5
angka1 = int(input("Masukan angka "))
print("\nT = tambah, K = kurang, X = kali, B = bagi, M = modulus, P = pangkat, A = akar")
modeKalkulator = input("Operasi matematika apa yang ingin anda lakukan? ")
if modeKalkulator == "T" or modeKalkulator == "t":
    angka2 = int(input("\ningin ditambah berapa? "))
    print(f"hasil dari perhitungan {angka1} tambah {angka2} adalah ", end=""); angka1 += angka2; print(angka1)
elif modeKalkulator == "K" or modeKalkulator == "k":
    angka2 = int(input("\ningin dikurang berapa? "))
    print(f"hasil dari perhitungan {angka1} kurang {angka2} adalah ", end=""); angka1 -= angka2; print(angka1)
elif modeKalkulator == "X" or modeKalkulator == "x":
    angka2 = int(input("\ningin dikali berapa? "))
    print(f"hasil dari perhitungan {angka1} kali {angka2} adalah ", end=""); angka1 *= angka2; print(angka1)
elif modeKalkulator == "B" or modeKalkulator == "b":
    angka2 = int(input("\ningin dibagi berapa? "))
    print(f"hasil dari perhitungan {angka1} bagi {angka2} adalah ", end=""); angka1 /= angka2; print(angka1)
elif modeKalkulator == "M" or modeKalkulator == "m":
    angka2 = int(input("\ningin dibagi berapa? "))
    print(f"hasil dari perhitungan {angka1} modulus {angka2} adalah ", end=""); angka1 %= angka2; print(angka1)
elif modeKalkulator == "P" or modeKalkulator == "p":
    angka2 = int(input("\ningin dipangkat berapa? "))
    print(f"hasil dari perhitungan {angka1} pangkat {angka2} adalah ", end=""); angka1 **= angka2; print(angka1)
elif modeKalkulator == "A" or modeKalkulator == "a":
    print(f"hasil dari perhitungan akar {angka1} adalah ", end=""); angka1 **= AKAR_DUA; print(round(angka1, 2))
else: print("metode perhitungan yang anda masukan tidak valdi")
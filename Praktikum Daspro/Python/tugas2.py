#bagian judul program
judul = "Program Menghitung Sisi Miring Segitiga Siku-Siku Dengan Teorema Pythagoras"  
print("\t"+"-" * len(judul))
print(f"\t{judul}")
print("\t"+"-" * len(judul))  
# bagian patern segitiga
for x in range(1, 11):
    for y in range(x):
        if x == 10 and y == 0:
            print ("\tB", end="")
        elif x == 1 and y == 0:
            print ("\tA", end="")
        elif x == 10 and y == 9:
            print ("\tC", end="")
        elif y == 0 :
            print ("\ta", end="")
        elif x == 10:
            print ("\tb", end="")
        elif y == x-1:
            print ("\tc", end="")
        else:
            print("\t*", end="")
    print()
#bagian operasi matematika
print("\t"+"-" * len(judul))
a = int(input("input panjang sisi a "))
b = int(input("input panjang sisi b "))
c= float(((a**2)+(b**2))**0.5)
print(f"panjang sisi miring dari segitiga siku-siku dengan panjang a {a} dan b {b} adalah {round(c, 2)}")
print("\t"+"-" * len(judul))
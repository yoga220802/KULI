import math
print("\tmenghtung sisi miring segitiga siku-siku")
a = int(input("Masukan panjang sisi a "))
b = int(input("Masukan panjang sisi b "))
sisiMiring = math.sqrt((a**2)+(b**2))
print(f"Panjang sisi miring segitiga siku-siku dengan panjang sisi a {a} dan sisi b {b} adalah {round(sisiMiring, 2)}")
from math_calculating import math


nomorKode = int(input("Hello, tell us your number "))
if nomorKode == 1:
    math.luasTrapesium()
elif nomorKode == 2:
    math.volumeKubus()
elif nomorKode == 3:
    math.kelilingBalok()
elif nomorKode == 4:
    math.kelilingLayangLayang()
elif nomorKode == 5:
    math.luasJajarGenjang()
else:
    print("nomor yang anda masukan tidak tersedia")
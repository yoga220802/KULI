class math:
    # 1
    def luasTrapesium():
        a = int(input("masukan nilai sisi a "))
        b = int(input("masukan nilai sisi b "))
        t = int(input("masukan nilai tinggi "))
        print(f"luas trapesium adalah {float(0.5*(a+b)*t)}")
    # 2
    def volumeKubus():
        s = int(input("masukan panjang sisi kubus "))
        print(f"volume balok adalah {float(s**3)}")
    # 3
    def kelilingBalok():
        p = int(input("masukan panjang balok "))
        l = int(input("masukan lebar balok "))
        t = int(input("masukan tinggi balok "))
        print(f"keliling balok adalah {float(4*(p+l+t))}")
    # 4
    def kelilingLayangLayang():
        a = int(input("masukan nilai sisi a "))
        b = int(input("masukan nilai sisi b "))
        print(f"keliling layang layang adalah {2*(a+b)}")
    # 5
    def luasJajarGenjang():
        a = int(input("masukan panjang jajar genjang "))
        t = int(input("masukan tingi jajar genjang "))
        print(f"luas jajar genjang adalah {float(a*t)}")
    # 6
    def luasLayangLayang():
        d1 = float(input("masukan panjang diagonal d1 "))
        d2 = float(input("masukan panjang diagonal d2 "))
        print(f"luas layang layang adalah {0.5*d1*d2}")
    # 7
    def luasPersegiPanjang():
        p = int(input("masukan panjang persegi panjang"))
        l = int(input("masukan lebar persegi panjang "))
        print(f"luad perdegi panjang adalah {float(p*l)}")
    # 8
    def dataTunggalKuartilBawah():
        print("penulis sedang malas ngoding banyak percabangan")
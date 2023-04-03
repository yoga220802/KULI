takjil = [] # inisialisasi stack takjil kosong

while True:
    print("Selamat datang di program pembagian takjil!")
    print("1. Sumbangkan takjil")
    print("2. Ambil takjil")
    print("3. Lihat takjil yang tersedia")
    print("4. Keluar")

    # minta input dari user
    choice = int(input("Masukkan pilihan Anda: "))

    # pilihan 1: user ingin menyumbangkan takjil
    if choice == 1:
        sumbangan = input("Masukkan jenis takjil yang akan disumbangkan: ")
        takjil.append(sumbangan)
        print(f"Terima kasih atas sumbangan takjil {sumbangan}!")

    # pilihan 2: user ingin mengambil takjil
    elif choice == 2:
        if len(takjil) == 0:
            print("Maaf, takjil sudah habis!")
        else:
            ambil = takjil.pop()
            print(f"Anda berhasil mengambil takjil {ambil}. Selamat berbuka puasa!")

    # pilihan 3: user ingin melihat takjil yang tersedia
    elif choice == 3:
        if len(takjil) == 0:
            print("Maaf, takjil sudah habis!")
        else:
            print("Takjil yang tersedia:")
            for t in takjil:
                print("- " + t)

    # pilihan 4: user ingin keluar
    elif choice == 4:
        print("Terima kasih telah menggunakan program pembagian takjil. Sampai jumpa lagi!")
        break

    # pilihan tidak valid
    else:
        print("Masukkan pilihan yang valid!")

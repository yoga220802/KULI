class stack_takjil:
    def __init__(self):
        # inisialisasi stack kosong
        self.takjil = []
         # Pesan yang akan ditampilkan jika takjil kosong
        self.kosong_message = "hapunten takjilna kosong baraya"

    def sumbang_takjil(self, sumbang):
        # operasi push/append pada stack, untuk menambahkan sumbangan takjil
        self.takjil.append(sumbang)
        # menampilkan pesan terimakasih
        print (f"hatur nuhun kana sumbangan takjil {sumbang} na :) ")
    
    def ambil_takjil(self):
        # cek apakah takjil kosong
        if len(self.takjil) == 0:
            # menampilkan pesan jika takjil kosong
            print (self.kosong_message)
        else:
            # operasi pop pada stack, untuk mengeluarkan elemen yang terakhir kali masuk
            ambil = self.takjil.pop()
             # Menampilkan pesan takjil yang diambil
            print (f"Andah Telah Mendapatkan Takjil {ambil}, Selamat Berbuka :) ")
    
    def tampilkan_takjil(self):
        # cek apakah takjil kosong
        if len(self.takjil) == 0:
            # menampilkan pesan jika takjil kosong
            print (self.kosong_message)
        else:
            # Menampilkan daftar takjil yang tersedia
            print("daftar takjil yang tersedia".center(50))
            for i in range(len(self.takjil)):
                print(f"{i+1}. {self.takjil[i]}")

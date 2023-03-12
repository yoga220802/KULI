# Moch Nashrull Maulana Fazri (2206058)

import os
os.system('cls' if os.name == 'nt' else 'clear')

BOLD = "\033[1m"
RESET = "\033[0m"
PINK = "\033[95m"
BLUE = "\033[34m"
LIGHTGREY = "\033[37m"
LINE = f"{LIGHTGREY}={RESET}" * 70

header = f'''{BOLD}{PINK}
         SSSSSSSSS  TTTTTTTTTT  AAAAAAAA    CCCCCCCCC  KK    KK
        SS              TT     AA      AA  CC          KK   KK
        SS              TT     AA      AA  CC          KK  KK
         SSSSSSSS       TT     AAAAAAAAAA  CC          KKKKK
                SS      TT     AA      AA  CC          KK  KK
                SS      TT     AA      AA  CC          KK   KK
        SSSSSSSSS       TT     AA      AA   CCCCCCCCC  KK    KK
{RESET}
{LINE}
                    {BLUE}Algoritma & Struktur Data
                            Kelompok 6
            Yoga Agustiansyah\t\t: 2206050
            Moch Nashrull Maulana Fazri\t: 2206058
            Mutia Sri Lestari\t\t: 2206064{RESET}
{LINE}
'''
print(header)

# Membuat list kosong untuk menampung huruf-huruf dalam kalimat
stack = []

# Meminta inputan kalimat dari user
Teks = input("Masukkan Kalimat: ")

# Memasukkan setiap huruf dalam kalimat ke dalam list stack
for Huruf in Teks:
    stack.append(Huruf)

# Menghapus huruf-huruf dalam kalimat satu per satu dengan menarik huruf terakhir
while len(stack) > 0:
    Del = input("Apakah Anda Ingin Menarik Huruf Terakhir ? [y/t] ").lower()
    if Del == "y":
        Huruf_Akhir = stack.pop()
        print(f"Huruf Yang Ditarik : {Huruf_Akhir}")
    else:
        break

# Memeriksa apakah stack sudah kosong atau masih ada sisa
if len(stack) == 0:
    print("Seluruh Huruf Dalam Kalimat Sudah Terhapus.")
else:
    print("Sisa Huruf Pada Kalimat :", stack)
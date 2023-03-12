# Mutia Sri Lestari_2206064_TeknikInformatikaB

import os

# Clear console screen
os.system('cls' if os.name == 'nt' else 'clear')

# Deklarasi Konstanta
BOLD = "\033[1m"
RESET = "\033[0m"
YELLOW = "\033[93m"
LIGHTBLUE = "\033[94m"
RED = "\033[31m"
LINE = f"{YELLOW}={RESET}" * 70

# Header text
header = f'''{BOLD}{LIGHTBLUE}
         SSSSSSSSS  TTTTTTTTTT  AAAAAAAA    CCCCCCCCC  KK    KK
        SS              TT     AA      AA  CC          KK   KK
        SS              TT     AA      AA  CC          KK  KK
         SSSSSSSS       TT     AAAAAAAAAA  CC          KKKKK
                SS      TT     AA      AA  CC          KK  KK
                SS      TT     AA      AA  CC          KK   KK
        SSSSSSSSS       TT     AA      AA   CCCCCCCCC  KK    KK
{RESET}
{LINE}
                    {RED}Algoritma & Struktur Data
                            Kelompok 6
            Yoga Agustiansyah\t\t: 2206050
            Moch Nashrull Maulana Fazri\t: 2206058
            Mutia Sri Lestari\t\t: 2206064{RESET}
{LINE}
'''

# Print header
print(header)

# Stack untuk menyimpan huruf
stack = []

# Meminta inputan kalimat
kalimat = input("Masukkan Kalimat : ")

# Memecahkan kaliamat menjadi per-huruf
for huruf in kalimat:
    stack.append(huruf)

# Looping selama stack tidak kosong
while True:
    # Cek apakah stack kosong
    if len(stack) <= 0:
        break

    # Tanyakan apakah ingin menarik huruf terakhir atau tidak
    hapus = input("Akan tarik karakter ? [Y/t] ").lower()

    if hapus == "y":
        # Jika ingin menarik, hapus huruf terakhir dari stack dan print pesan
        print(f"Karakter yang ditarik adalah yang paling akhir --> {stack.pop()}")
    else:
        # Jika tidak ingin menarik, keluar dari loop
        break
    
# Cek apakah stack sudah kosong
if len(stack) == 0:
    print("\n\nHuruf dalam kalimat sudah habis")
else:
    # Jika stack masih berisi, print sisa huruf yang belum ditarik
    print("\n\nSisa huruf dari kalimat adalah : ", stack)
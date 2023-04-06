# import modul yang akan digunakan
import os # Mengimpor modul os yang nantinya untuk membersihkan layar konsol
from uts_kelompok6_Stack_Takjil import stack_takjil # Mengimpor class stack_takjil dari file uts_kelompok6_Stack_Takjil
import msvcrt # Mengimpor modul msvcrt untuk menerima input tanpa perlu menekan tombol enter

# fungsi untuk membaca input tanpa menunggu user menekan tombol enter, untuk menahan layar sebelum kembali ke pemilihan menu
def getch():
    return msvcrt.getch()

# fungsi untuk membuat garis pemisah dengan tipe tertentu
def line(line_type):
    return (f"{ORANGE}{line_type}{RESET}" * 70)

# deklarasi konstanta yang akan digunakan sebagai format output
BOLD = "\033[1m"
RESET = "\033[0m"
PINK = "\033[95m"
CYAN = "\033[34m"
ORANGE = "\033[33m"

# deklarasi header program, berisi informasi nama program dan anggota kelompok
header = f'''{BOLD}{PINK}
     SSSSSSSSS  TTTTTTTTTT  AAAAAAAA    CCCCCCCCC  KK    KK
    SS              TT     AA      AA  CC          KK   KK
    SS              TT     AA      AA  CC          KK  KK
     SSSSSSSS       TT     AAAAAAAAAA  CC          KKKKK
            SS      TT     AA      AA  CC          KK  KK
            SS      TT     AA      AA  CC          KK   KK
    SSSSSSSSS       TT     AA      AA   CCCCCCCCC  KK    KK

    TTTTTTTTTTT   AAAAAAAA   KK    KK  JJJJJJJJJJ  II  LLL
        TT       AA      AA  KK   KK       JJJ     II  LLL
        TT       AA      AA  KK  KK        JJJ     II  LLL
        TT       AAAAAAAAAA  KKKKK         JJJ     II  LLL
        TT       AA      AA  KK  KK        JJJ     II  LLL
        TT       AA      AA  KK   KK       JJJ     II  LLL
        TT       AA      AA  KK    KK  JJJJJJJ     II  LLLLLLLLL
{RESET}
{line("=")}
                    {CYAN}algoritma & struktur data
                            kelompok 6
            yoga agustiansyah\t\t: 2206050
            moch nashrull maulana fazri\t: 2206058
            mutia sri lestari\t\t: 2206064{RESET}
{line("=")}
'''

# membuat objek dari kelas stack_takjil
program_takjil = stack_takjil()

# loop utama program
while True:
    # membersihkan layar setiap iterasi perulangan
    os.system("cls" or "clear")

    # menampilkan header
    print(header)

    # menampilkan menu
    print (f"""{"wilujeng sumping di takjil ceria :)".center(65)}\n
    1. sedekah takjil
    2. ambil takjil
    3. keluar program\n""")

    # mencetak garis pembatas
    print(line("-"))

    # menampilkan daftar takjil yang tersedia dengan memanggil method tampilkan_takjil() dari objek program_takjil
    program_takjil.tampilkan_takjil()

    # membaca input dari user untuk memilih menu
    menu = int(input("\nmangga pilih progamna >> "))

    # kondisi jika user memilih 1, yaitu menyedekahkan takjil (push/append ke stack)
    if menu == 1:
        # meminta input dari user untuk dimasukan kedalam stack
        sumbang = input("lebetkeun wae takjil nu bade di sumbangkeun : ")
        # memanggil method sumbang_takjil() dari objek program_takjil dengan parameter variabel sumbang
        program_takjil.sumbang_takjil(sumbang)
    
    # kondisi jika user memilih 2, yaitu mengambil takjil (pop dari stack)
    elif menu == 2:
        # memanggil method ambil_takjil() dari objek program_takjil
        program_takjil.ambil_takjil()
    
    # kondisi jika user memilih 3, yaitu keluar dari program
    elif menu == 3:
        # menampilkan pesan terimakasih
        print ("hatur nuhun parantos nganggo program takjil ceria :) ")
        # menghentikan loop utama
        break
    
    # kondisi jika user memasukan menu yang salah
    else:
        print("lebetkeun pilihan nu leres :d ")

    # menampilkan pesan untuk menekan tombol apapun untuk kembali ke pemilihan menu
    print("\ntekan tombol apa saja untuk kembali ke menu...")
    # memanggil function getch() untuk menahan layar sebelum kembali ke pemilihan menu, dengan cara menunggu inputan keyboard apapun dari user
    getch()
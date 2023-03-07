from linkedList_methods import LinkedList
import os

linked_list = LinkedList()
garis = "="*70

def clear_screen():
    print("\nTekan tombol \"ENTER\" untuk melanjutkan...")
    input()
    os.system('cls' if os.name=='nt' else 'clear')

menu = [
    "Tampilkan linked list",
    "Tambah node di depan",
    "Tambah node di akhir",
    "Tambah node diantara node",
    "Cari node",
    "Hapus node",
    "Exit",
]

os.system('cls' if os.name=='nt' else 'clear')

while True:
    print(f'''
        LL         II  NNNN     MM  KK    KK  EEEEEEEE  DDDDDDD
        LL         II  NN NN    NN  KK   KK   EE        DD    DD
        LL         II  NN  NN   NN  KK  KK    EE        DD     DD
        LL         II  NN   NN  NN  KKKKK     EEEEEEEE  DD     DD
        LL         II  NN    NN NN  KK  KK    EE        DD     DD
        LL         II  NN     NNNN  KK   KK   EE        DD    DD
        LLLLLLLLL  II  NN      NNN  KK    KK  EEEEEEEE  DDDDDDD

                LL          II   SSSSSSSSS  TTTTTTTTTT
                LL          II  SS              TT
                LL          II  SS              TT
                LL          II   SSSSSSSS       TT
                LL          II          SS      TT
                LL          II          SS      TT
                LLLLLLLLLL  II  SSSSSSSSS       TT

{garis}
                    Algoritma & Struktur Data
                            Kelompok 6
            Yoga Agustiansyah\t\t: 2206050
            Moch Nashrull Maulana Fazri\t: 2206058
            Mutia Sri Lestari\t\t: 2206064
{garis}
''')
    print("\t\t\tMenu Linked List")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    
    choice = int(input(">> "))
    match choice:
        case 1:
            # print("Pilihan 1")
            if linked_list.head is None:
                print("List masih kosong, silahkan tambahkan elemen kedalam list...")
            else:
                print("Linked List: ", end="")
                linked_list.display()
            clear_screen()
        case 2:
            data = int(input("Masukan angka untuk ditambahkan di depan list : "))
            linked_list.insertAtBeginning(data)
            print("Data ditambahkan di depan list...")
            clear_screen()
        case 3:
            data = int(input("Masukan angka untuk ditambahkan di akhir list : "))
            linked_list.insertAtEnd(data)
            print("Data ditambahkan di akhir list...")
            clear_screen()
        case 4:
            if linked_list.head is not None:
                print("Linked List: ", end="")
                linked_list.display()
                node_data = int(input("Masukan data node mana yang ingin anda tambahkan data baru setelahnya : "))
                node = linked_list.searchNode(node_data)    
                if node:
                    data = int(input(f"Masukan angka yang anda ingin tambahkan setelah {node_data} : "))
                    linked_list.insertAfterNode(node, data)
                    print(f"Data baru ditambahkan setelah {node_data}")
                else: print(f"Node {node_data} tidak ditemukan di dalam linked list ini...")
            else:
                print("List masih kosong, silahkan tambahkan elemen kedalam list...")
            clear_screen()
        case 5:
            data = int(input("Masukan data yang ingin dicari : "))
            node = linked_list.searchNode(data)
            print("Node ditemukan dalam linked list" if node else "Node tidak ditemukan dalam list")
            clear_screen()
        case 6:
            if linked_list.head is None:
                print("List masih kosong, silahkan tambahkan elemen kedalam list...")
            else:
                print("Linked List: ", end="")
                linked_list.display()
                data = int(input("Masukan data yang ingin dihapus : "))
                linked_list.deleteNode(data)
            clear_screen()
        case 7:
            print("Exiting...")
            break
        case _:
            print("Pilihan tidak tersedia")
            clear_screen()
print ("program keluar")
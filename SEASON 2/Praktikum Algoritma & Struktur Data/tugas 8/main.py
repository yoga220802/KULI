from queue import Queue
import msvcrt
import os

class ToDoList(Queue):
    def add_task(self, data):
        self.enqueue(data)
        print(f"\nTask '{data}' telah ditambahkan.\n")
    
    def process_tasks(self):
        if len(self.queue) == 0:
            print("Tidak ada tugas dalam antrian.")
        else:
            task = self.dequeue()
            print(f"Menjalankan tugas '{task}'.")
    
    def show_task(self):
        if len(self.queue) > 0:
            print("\tDaftar Tugas")
            self.show_queue()
        else:
            print("\tDaftar Tugas Kosong") 

    def clear_tasks(self):
        self.clear_queue()
        print("Antrian tugas telah dikosongkan.")

def getch():
    msvcrt.getch()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

to_do_list = ToDoList()
lanjut = True

while lanjut == True:
    clear_screen()
    print('''\t\tProgram Queue To Do List

    1. Tambahkan Tugas
    2. Kerjakan Tugas
    3. Hapus Daftar
    4. Keluar
    ''')

    to_do_list.show_task()

    pilihan = int(input("\nMasukan Pilihan Anda >> "))

    match pilihan:
        case 1:
            tugas = input("\nMasukan Tugas >> ")
            to_do_list.add_task(tugas)
        case 2:
            to_do_list.process_tasks()
        case 3:
            to_do_list.clear_tasks()
        case 4:
            break
        case _:
            print("Pilihan tidak valid")
            
    print("Tekan Tombol Apapun Untuk Lanjut...")
    getch()
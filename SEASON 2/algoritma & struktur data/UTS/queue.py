from collections import deque
import time

# Membuat queue awal
queue = deque(["Orang 1", "Orang 2", "Orang 3", "Orang 4", "Orang 5"])
print(queue)

# Fungsi untuk mengurangi antrian
def decreaseQueue():
    # Menghapus elemen pertama dari queue
    dequeued = queue.popleft()
    print(f"Antrian {dequeued} telah keluar")

    # Menampilkan queue saat ini
    print(queue)

    # Memeriksa apakah antrian telah habis
    if len(queue) == 0:
        print("Antrian telah habis.")
        clearInterval(interval)

# Interval untuk mengurangi antrian setiap 3 detik
interval = 3
while queue:
    decreaseQueue()
    time.sleep(interval)

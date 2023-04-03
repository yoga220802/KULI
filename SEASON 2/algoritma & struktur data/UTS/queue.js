// Membuat queue awal
const queue = ["Orang 1", "Orang 2", "Orang 3", "Orang 4", "Orang 5"];

console.log(queue);

// Fungsi untuk mengurangi antrian
function decreaseQueue() {
  // Menghapus elemen pertama dari queue
  const dequeued = queue.shift();
  console.log(`Antrian ${dequeued} telah keluar`);

  // Menampilkan queue saat ini
  console.log(queue);

  // Memeriksa apakah antrian telah habis
  if (queue.length === 0) {
    console.log("Antrian telah habis.");
    clearInterval(interval);
  }
}

// Interval untuk mengurangi antrian setiap 10 detik
const interval = setInterval(decreaseQueue, 3000);

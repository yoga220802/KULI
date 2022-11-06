#include <iostream>
using namespace std;
int main(){
    int jenis, produk, harga, banyakBarang;
    string namaBarang;
    cout << "\t---Jenis produk---\n1. Makanan\n2. Minuman\npilih jenis produk : ";
    cin >> jenis;
    switch (jenis){
    case 1:
        cout<<"\n\t--Daftar Makanan--\n1. Kue = 5000\n2. Gorengan = 2000\n3. Bakso = 7000\nPilih Makanan : ";
        cin>>produk;
        switch (produk){
            case 1:
                namaBarang = "Kue";
                harga = 5000;
                break;
            case 2:
                namaBarang = "Gorengan";
                harga = 2000;
                break;
            case 3:
                namaBarang = "Bakso";
                harga = 7000;
                break;
            default:
                namaBarang = "tidak tersedia";
                harga = 0;
                break;
            }
            break;
    case 2:
        cout<<"\n\t--Daftar Minuman--\n1. Teh = 4000\n2. Kopi = 5000\n3. Air Mineral = 3000\nPilih Minuman : ";
        cin>>produk;
        switch (produk){
            case 1:
                namaBarang = "Teh";
                harga = 4000;
                break;
            case 2:
                namaBarang = "Kopi";
                harga = 5000;
                break;
            case 3:
                namaBarang = "Air Mineral";
                harga = 3000;
                break;
            default:
                namaBarang = "tidak tersedia";
                harga = 0;
                break;
            }
            break;
    default:
        namaBarang = "tidak tersedia";
        harga = 0;
        break;
        }
    cout<<"\nBerapa banyak barang yang ingin anda beli ?"; cin>>banyakBarang;
    cout<<"\nPesanan anda "<<namaBarang<<" sebanyak "<<banyakBarang<<" buah. Total harganya adalah "<<banyakBarang*harga;
}
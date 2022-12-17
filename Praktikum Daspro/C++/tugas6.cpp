#include <iostream>
using namespace std;
int main(){
    int jenis, produk, harga, banyakBarang;
    string namaBarang;
    cout << "\t---Jenis Processor---\n1. Intel Core i series\n2. AMD Ryzen series\npilih jenis processor : ";
    cin >> jenis;
    switch (jenis){
    case 1:
        cout<<"\n\t--Daftar Processor Intel--\n1. Intel Core i5-13600KF = $294\n2. Intel Core i7-13700K = $419\n3. Intel Core i9-13900K = $589\nPilih Processor : ";
        cin>>produk;
        switch (produk){
            case 1:
                namaBarang = "Intel Core i5-13600KF";
                harga = 294;
                break;
            case 2:
                namaBarang = "Intel Core i7-13700K";
                harga = 419;
                break;
            case 3:
                namaBarang = "Intel Core i9-13900K";
                harga = 589;
                break;
            default:
                namaBarang = "tidak tersedia";
                harga = 0;
                break;
            }
            break;
    case 2:
        cout<<"\n\t--DaftarProcessor AMD--\n1. AMD Ryzen 5 7600X = $299\n2. AMD Ryzen 7 7700X = $399\n3. AMD Ryzen 9 7950X= $699\nPilih Processor : ";
        cin>>produk;
        switch (produk){
            case 1:
                namaBarang = "AMD Ryzen 5 7600X";
                harga = 299;
                break;
            case 2:
                namaBarang = "AMD Ryzen 7 7700X";
                harga = 399;
                break;
            case 3:
                namaBarang = "AMD Ryzen 9 7950X";
                harga = 699;
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
    cout<<"\nBerapa banyak "<<namaBarang<<" yang ingin anda beli ?"; cin>>banyakBarang;
    cout<<"\nPesanan anda "<<namaBarang<<" sebanyak "<<banyakBarang<<" buah. Total harganya adalah $"<<banyakBarang*harga;
}
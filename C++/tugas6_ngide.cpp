#include <iostream>
using namespace std;
int main(){
    string makanan[] = {"Kue", "Gorengan", "Bakso"}, minuman[] = {"Teh", "Kopi", "Air Mineral"}, namaProduk;
    int hargaMakanan[] = {5000, 2000, 7000}, hargaMinuman[] = {4000, 5000, 3000}, hargaProduk;
    int jml_arr, jenis, produk, jumlah;
    cout<<"\t---Jenis Produk---\n1. Makanan\n2. Minuman\nPilih jenis produk : ";
    cin>>(jenis);
    switch (jenis){
    case 1:
        jml_arr = sizeof(makanan)/sizeof(*makanan);
        cout<<"\n\t--Daftar Makanan--"<<endl;
        for (int i = 0; i < jml_arr; i++){
                cout<<i+1<<". "<<makanan[i]<<" : "<<hargaMakanan[i]<<endl;}
        cout<<"Pilih makanan : ";
        cin>>(produk);
        switch (produk){
        case 1:
            namaProduk = makanan[0];
            hargaProduk = hargaMakanan[0];
            break;
        case 2:
            namaProduk = makanan[1];
            hargaProduk = hargaMakanan[1];
            break;
        case 3:
            namaProduk = makanan[2];
            hargaProduk = hargaMakanan[2];
            break;
        default:
            namaProduk = "tidak tersedia";
            hargaProduk = 0;
            break;}
        break;
    case 2:
        jml_arr = sizeof(minuman)/sizeof(*minuman);
        cout<<"\n\t--Daftar Minuman--"<<endl;
        for (int i = 0; i < jml_arr; i++){
                cout<<i+1<<". "<<minuman[i]<<" : "<<hargaMinuman[i]<<endl;}
        cout<<"Pilih minuman : ";
        cin>>(produk);
        switch (produk){
        case 1:
            namaProduk = minuman[0];
            hargaProduk = hargaMinuman[0];
            break;
        case 2:
            namaProduk = minuman[1];
            hargaProduk = hargaMinuman[1];
            break;
        case 3:
            namaProduk = minuman[2];
            hargaProduk = hargaMinuman[2];
            break;
        default:
            namaProduk = " tidak tersedia";
            hargaProduk = 0;
            break;}
        break;
    default:
        namaProduk = " tidak tersedia";
        hargaProduk = 0;
        break;}
    cout<<"Ingin berapa banyak? ";
    cin>>(jumlah);
    cout<<"\nProduk yang anda pilih "<<namaProduk<<" sebanyak "<<jumlah<<", Total harganya adalah "<<hargaProduk*jumlah;
}
#include <iostream>
using namespace std
int main(){
    int awal = 1, kelipatan = 1, akhir, jmlTotal = 0
    cout<<"\t---PROGRAM MENCARI DAN MENGHITUNG BARISAN BILANGAN---\n"
    cout << "Masukan nilai awal : " cin>>awal
    cout << "Ingin mencari kelipatan berapa? " cin>>kelipatan
    cout << "Ingin menampilkan sampai angka berapa? " cin>>akhir
    cout << "barisan aritmatika = "
    for (int i = awal i <= akhir i+=kelipatan)
    {
        if (i < akhir)
        {
            cout << i <<", "
        }else
        {
            cout << i
        }
        jmlTotal += i
    }
    cout << "Jumlah total dari barisan tersebut adalah "<<jmlTotal
    return 0   
}
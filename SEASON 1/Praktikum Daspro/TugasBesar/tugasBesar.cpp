#include <iostream>
#include <map>
#include <vector>
#include <fstream>
#include <conio.h>

#include "dataStorage.cpp"
#include "functions.cpp"

using namespace std;

int main() {
    int pilihKategori, pilihProduk, jumlahProduk, harga, counter = 1;
    string username, password, name, message, produk, kategori;
    bool found, loggedIn;
    vector<pair<string, pair<string, pair<int, int>>>> daftarBelanja = {};
    pair<string, pair<string, bool>> validation;
    do {
        clearScreen();
        cout << garis();
        cout << tab << tab << "PROGRAM TOKO"
             << "\n\t\tTB KELOMPOK 4" << endl;
        cout << garis();
        cout << "Silahkan Login untuk menjalankan program" << endl;
        do {
            cout << "Masukan username : ";
            cin >> username;
            cout << "Masukan password : ";
            cin >> password;
            cout << garis("-");
            validation = userValidation(users, username, password);
            name = validation.first;
            message = validation.second.first;
            found = validation.second.second;
            if (found) {
                cout << message << ", " << name << endl;
                break;
            }
            else {
                cout << message << endl;
            }
        } while (!found);
        while (true) {
            cout << "---Pilih Kategori Barang---" << endl;
            for (int i = 0; i < dataKategori.size(); i++) {
                cout << i + 1 << ". " << dataKategori[i] << endl;
            }
            do {
                cout << ">> ";
                cin >> pilihKategori;
                if (pilihKategori < 1 || pilihKategori > dataProduk.size()) {
                    cout << "Kategori tidak tersedia. Pilih kategori yang valid.\n";
                }

            } while (pilihKategori < 1 || pilihKategori > dataProduk.size());
            kategori = dataKategori[pilihKategori - 1];
            cout << "Data produk " << dataKategori[pilihKategori - 1] << ":" << endl;
            for (auto const &[namaProduk, hargaProduk] : dataProduk[pilihKategori - 1]) {
                cout << counter << ". " << namaProduk << tab << ": " << hargaProduk << endl;
                counter++;
            }

            do {
                cout << ">> ";
                cin >> pilihProduk;
                if (pilihProduk < 1 || pilihProduk > dataProduk[pilihKategori - 1].size()) {
                    cout << "Produk tidak tersedia. Pilih Produk yang valid.\n";
                }

            } while (pilihProduk < 1 || pilihProduk > dataProduk[pilihKategori - 1].size());
            cout << "Jumlah produk yang diinginkan : ";
            cin >> jumlahProduk;
            for (auto const &[namaProduk, hargaProduk] : dataProduk[pilihKategori - 1]) {
                if (--pilihProduk == 0) {
                    produk = namaProduk;
                    harga = hargaProduk;
                    break;
                }
            }
            daftarBelanja.push_back(make_pair(kategori, make_pair(produk, make_pair(harga, jumlahProduk))));
            cout << "Apakah ingin menambah produk lain? (y/n) ";
            char tambahProduk;
            cin >> tambahProduk;
            counter = 1;
            if (tambahProduk == 'n' || tambahProduk == 'N') {
                break;
            }
        }
        bubbleSort(daftarBelanja);
        cout << garis("-");
        cout << "Daftar belanja:" << endl;
        int totalBelanjaan = 0;
        for (int i = 0; i < daftarBelanja.size(); i++) {
            cout << i + 1 << ". " << daftarBelanja[i].first << " " << daftarBelanja[i].second.first << " : "
                 << "Rp. " << daftarBelanja[i].second.second.first
                 << "/item x " << daftarBelanja[i].second.second.second
                 << ", => Rp. " << daftarBelanja[i].second.second.first * daftarBelanja[i].second.second.second << endl;
            totalBelanjaan += daftarBelanja[i].second.second.first * daftarBelanja[i].second.second.second;
            cout << garis("-");
        }
        cout << "SUB TOTAL\t : " << totalBelanjaan << endl
             << endl;
        ofstream file("daftar_belanja.txt", ios::app);
        file << endl << name << endl;
        for (int i = 0; i < daftarBelanja.size(); i++) {
            file << i + 1 << ". " << daftarBelanja[i].first
            << " " << daftarBelanja[i].second.first << " : "
                 << "Rp. " << daftarBelanja[i].second.second.first
                 << "/item x " << daftarBelanja[i].second.second.second
                 << ", => Rp. " << daftarBelanja[i].second.second.first * daftarBelanja[i].second.second.second << endl;
        }
        file << garis();
        file << "SUB TOTAL\t: " << totalBelanjaan << endl
             << garis() << endl;
        file.close();
        cout << "Data telah disimpan" << endl
             << "\tTERIMA KASIH TELAH BERBELANJA\n"
             << garis();
        loggedIn = false; 
        daftarBelanja.clear();
        getch();
    } while (!loggedIn);
}
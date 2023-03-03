#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
    // deklarasi variabel
    vector<vector<string>> dataMahasiswa = {
        {"Yoga Agustiansyah", "Udin Gambut"},
        {"2206050", "2101234"},
        {"Teknik Informatika", "Teknik Informatika"},
        {"Garut", "Sumedang"},
        {"22 Agustus 2002", "25 Desember 2002"}};
    string tambah, nama, nim, prodi, tempatLahir, tanggalLahir;
    // menampilkan data mahasiswa default
    cout << "\t---Daftar Mahasiswa---" << endl;
    for (int i = 0; i < dataMahasiswa[0].size(); i++)
    {
        cout << i + 1 << endl;
        cout << "Nama\t\t\t:" << dataMahasiswa[0][i] << endl;
        cout << "NIM\t\t\t:" << dataMahasiswa[1][i] << endl;
        cout << "Program Studi\t\t:" << dataMahasiswa[2][i] << endl;
        cout << "Tempat, Tanggal Lahir\t:" << dataMahasiswa[3][i] << ", " << dataMahasiswa[4][i] << endl;
        cout << endl;
    }
    // konfirmasi apakah data mahasiswa ingin ditambah atau tidak
    cout << "Ingin menambah daftar mahasisaw(Y/t)? ";
    getline(cin, tambah);
    tambah = tolower((tambah[0]));
    // penambahan data mahasiswa jika ingin ditambah
    while (tambah == "y")
    {
        cout << "Masukan Nama\t\t: ";
        getline(cin, nama);
        cout << "Masukan Nim\t\t: ";
        getline(cin, nim);
        cout << "Masukan Program Studi\t: ";
        getline(cin, prodi);
        cout << "Masukan Tempat Lahir\t: ";
        getline(cin, tempatLahir);
        cout << "Masukan Tanggal Lahir\t: ";
        getline(cin, tanggalLahir);
        dataMahasiswa[0].push_back(nama);
        dataMahasiswa[1].push_back(nim);
        dataMahasiswa[2].push_back(prodi);
        dataMahasiswa[3].push_back(tempatLahir);
        dataMahasiswa[4].push_back(tanggalLahir);
        // konfirmasi apakah data mahasiswa ingin ditambah lagi atau tidak
        cout << "\nIngin menambah daftar mahasiswa lagi(Y/t)? ";
        getline(cin, tambah);
        tambah = tolower((tambah[0]));
    }
    // menampilkan data mahasiswa terbaru
    cout << "\n\t---Daftar Mahasiswa Baru---" << endl;
    for (int i = 0; i < dataMahasiswa[0].size(); i++)
    {
        cout << i + 1 << endl;
        cout << "Nama\t\t\t:" << dataMahasiswa[0][i] << endl;
        cout << "NIM\t\t\t:" << dataMahasiswa[1][i] << endl;
        cout << "Program Studi\t\t:" << dataMahasiswa[2][i] << endl;
        cout << "Tempat, Tanggal Lahir\t:" << dataMahasiswa[3][i] << ", " << dataMahasiswa[4][i] << endl;
        cout << endl;
    }
}
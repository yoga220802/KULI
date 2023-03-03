#include <iostream>
#include <vector>
#include <cctype>
using namespace std;

vector<int> sorting(vector<int> arr) {
    int key, j;
    for (int i = 1; i < arr.size(); i++) {
        key = arr[i];
        j = i;
        while (j >= 0 && arr[j - 1] > key) {
            arr[j] = arr[j - 1];
            j--;
            arr[j] = key;
        }
    }
    return arr;
}

int main() {
    vector<int> numbers = { 1, 3, 5 };
    numbers = sorting(numbers);
    bool found = false;
    int add, left, right, mid;
    string ask;
    cout << "\tProgram Menggunakan Binary Search" << endl;
    cout << "=================================================" << endl;
    cout << "Daftar Angka : ";
    for (int i = 0; i < numbers.size(); i++) {
        cout << numbers[i] << ", ";
    }
    cout << endl;
    cout << "Ingin menambahkan angka (Y/t) ? ";
    cin >> ask;ask = tolower(ask[0]);
    while (ask == "y") {
        found = false;
        cout << "\ningin tambah angka berapa ? ";cin >> add;
        left = 0;
        right = numbers.size() - 1;
        while (left <= right) {
            mid = (left + right) / 2;
            if (numbers[mid] == add) {
                found = true;
                break;
            }
            else if (numbers[mid] < add) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        if (found) {
            cout << "angka " << add << " sudah ada" << endl;
            cout << "Ingin menambahkan angka yang lain (Y/t) ? ";
            cin >> ask; ask = tolower(ask[0]);
        }
        else {
            numbers.push_back(add);
            numbers = sorting(numbers);
            cout << "Angka berhasil ditambahkan : ";
            for (int i = 0; i < numbers.size(); i++) {
                cout << numbers[i] << ", ";
            }
            cout << endl;
            cout << "Ingin menambahkan angka lagi (Y/t) ? ";
            cin >> ask; ask = tolower(ask[0]);
        }
    }
    cout << "=================================================" << endl;
    cout << "Data akhir : ";
    for (int i = 0; i < numbers.size(); i++) {
        cout << numbers[i] << ", ";
    }
    cout << endl;
    return 0;
}

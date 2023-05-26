#include <iostream>
#include <string>
#include <limits>
#include <conio.h>

using namespace std;

const int MAX_SIZE = 1000;

struct Stack {
    string data[MAX_SIZE];
    int top;

    Stack() : top(-1) {}

    void Push(const string& searchData) {
        if (top == MAX_SIZE - 1) {
            cout << "Riwayat pencarian penuh. Tidak dapat menambahkan riwayat pencarian."<< endl;
            return;
        }
        data[++top] = searchData;
    }

    void Pop() {
        if (IsEmpty()) {
            cout << "Riwayat pencarian kosong. Tidak ada riwayat untuk dihapus." << endl;
            return;
        }
        top--;
    }

    bool IsEmpty() const {
        return (top == -1);
    }

    string Top() const {
        if (IsEmpty()) {
            return "";
        }
        return data[top];
    }

    void PrintStack() const {
        if (IsEmpty()) {
            cout << "Belum ada riwayat pencarian." << endl;
            return;
        }
        cout << "Riwayat pencarian:" << endl;
        for (int i = top; i >= 0; i--) {
            cout << data[i] << endl;
        }
    }
};

int getInputChoice() {
    int choice;
    cout << "Pilihan Anda: ";
    if (!(cin >> choice)) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    return choice;
}

void performSearch(Stack& historyStack) {
    string keyword;
    cout << "Masukkan keyword pencarian: ";
    cin.ignore();
    getline(cin, keyword);
    historyStack.Push(keyword);
    cout << "Anda berhasil melakukan pencarian \"" << keyword << "\", history pencarian sudah disimpan" << endl;
}

void removeLastSearch(Stack& historyStack) {
    if (historyStack.IsEmpty()) {
        cout << "Tidak ada riwayat pencarian yang dapat dihapus." << endl;
    } else {
        historyStack.Pop();
        cout << "Riwayat pencarian terakhir telah dihapus." << endl;
    }
}

void viewSearchHistory(const Stack& historyStack) {
    historyStack.PrintStack();
}

int main() {
    Stack historyStack;
    int choice;
    do {
        system("cls");
        cout << "========== Browsing History Manager ==========" << endl;
        cout << "1. Lakukan Pencarian" << endl;
        cout << "2. Hapus history pencarian terakhir" << endl;
        cout << "3. Lihat riwayat pencarian" << endl;
        cout << "4. Keluar" << endl;

        choice = getInputChoice();

        switch (choice) {
            case 1:
                performSearch(historyStack);
                break;
            case 2:
                removeLastSearch(historyStack);
                break;
            case 3:
                viewSearchHistory(historyStack);
                break;
            case 4:
                cout << "Terima kasih! Program selesai." << endl;
                break;
            default:
                cout << "Pilihan tidak valid. Silakan coba lagi." << endl;
        }

        cout << "Tekan tombol apapun untuk melanjutkan...";
        getch();
    } while (choice != 4);

    return 0;
}
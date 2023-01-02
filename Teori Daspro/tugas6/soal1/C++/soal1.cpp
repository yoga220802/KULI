#include <iostream>
using namespace std;

int main() {
    int jml = 0 , i, n, angka;
    for (angka = 1; angka <= 300; angka++){
        n = 0;
        for (i = 2; i <= angka / 2; i++) {
            if (angka % i == 0) {
                n++;
                break;
            }
        }
        if (n == 0 && angka != 1) {
            cout << angka << ", ";
            jml += angka;
        }
    }
    cout << "Jumlah total = " << jml;
}

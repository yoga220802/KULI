#include <map>
#include <vector>
#include <iostream>
using namespace std;

pair<string, pair<string, bool>> userValidation(vector<map<string, string>> userData, string username, string password) {
    string name = "kosong", message;
    bool found = false;
    int i = 0;
    for (i; i < userData.size(); i++) {
        if (userData[i]["nim"] == username && userData[i]["password"] == password) {
            found = true;
            break;
        }
    }
    if (found) {
        message = "welcome";
        name = userData[i]["nama"];
    }
    else {
        message = "username atau password yang anda masukan salah!!!";
    }
    pair<string, bool> returnData = make_pair(message, found);
    pair<string, pair<string, bool>> results = make_pair(name, returnData);
    return results;
}

string garis(string tipeGaris = "=") {
    string _garis;
    for (int i = 1; i <= 50; i++) {
        _garis += tipeGaris;
    }
    _garis += "\n";
    return _garis;
}

void bubbleSort(vector<pair<string, pair<string, pair<int, int>>>> &daftarBelanja) {
    for (int i = 0; i < daftarBelanja.size() - 1; i++) {
        for (int j = 0; j < daftarBelanja.size() - i - 1; j++) {
            if (daftarBelanja[j].second.second.second > daftarBelanja[j + 1].second.second.second) {
                swap(daftarBelanja[j], daftarBelanja[j + 1]);
            }
        }
    }
}

void clearScreen() {
    cout << "\033[2J\033[1;1H";
}

string tab = "\t";
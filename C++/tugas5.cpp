#include <iostream>
using namespace std;
int main(){
    // deklarasi variabel
    float tugas1, tugas2, tugas3, tugas4, uts, uas, total;
    string grade, status;
    // input untuk value variabel
    cout << ("Masukan nilai tugas 1 : "); cin >> (tugas1);
    cout << ("Masukan nilai tugas 2 : "); cin >> (tugas2);
    cout << ("Masukan nilai tugas 3 : "); cin >> (tugas3);
    cout << ("Masukan nilai tugas 4 : "); cin >> (tugas4);
    cout << ("Masukan nilai UTS : "); cin >> (uts);
    cout << ("Masukan nilai UAS : "); cin >> (uas);
    // assignment untuk menghitung rata-rata tugas dan total nilai
    total = (((tugas1+tugas2+tugas3+tugas4)/4)*0.4) + (uas*0.3) + (uts*0.3);
    // percabangan untuk menetukan grade
    if (total > 80){
        grade = "A";
        status = "lulus";
    }else if (total > 70){
       grade = "B";
        status = "lulus";
    }else if (total > 60){
       grade = "C";
        status = "lulus";
    }else{
       grade = "D";
        status = "tidak lulus";
    }
    // menampilkan hasil kalkulasi dan grading
    cout << "Mahasiswa mendapat nilai "<<total<<" , "<<status<<" dengan predikat "<<grade;
}
// #include <stdio.h>
// #include <string>
// using namespace std;
// int main(){
//     // deklarasi variabel
//     float tugas1, tugas2, tugas3, tugas4, uts, uas, total, rataTugas;
//     char grade;
//     string nama, nim;
//     // input untuk value variabel
//     printf("Masukan nama anda : "); scanf("%[^\n]s", &nama);
//     printf("Masukan NIM anda : "); scanf("%d", &nim);
//     printf("Masukan nilai tugas 1 : "); scanf("%f", &tugas1);
//     printf("Masukan nilai tugas 2 : "); scanf("%f", &tugas2);
//     printf("Masukan nilai tugas 3 : "); scanf("%f", &tugas3);
//     printf("Masukan nilai tugas 4 : "); scanf("%f", &tugas4);
//     printf("Masukan nilai UTS : "); scanf("%f", &uts);
//     printf("Masukan nilai UAS : "); scanf("%f", &uas);
//     // assignment untuk menghitung rata-rata tugas dan total nilai
//     rataTugas = (tugas1+tugas2+tugas3+tugas4)/4;
//     total = (rataTugas*0.4) + (uas*0.3) + (uts*0.3);
//     // percabangan untuk menetukan grade
//     if (total > 80){
//         grade = 'A';
//     }else if (total > 70){
//        grade = 'B';
//     }else if (total > 60){
//        grade = 'C';
//     }else{
//        grade = 'D';
//     }
//     // percabangan untuk menampilkan teks kelulusan
//     switch (grade)
//     {
//         case 'D':
//             printf("Mahasiswa dengan nama %s dan NIM %d mendapat nilai %f, tidak lulus dengan predikat %c",nama, nim, total, grade);
//             break;
//         default:
//             printf("Mahasiswa dengan nama %s dan NIM %d mendapat nilai %.2f, lulus dengan predikat %c",nama, nim, total, grade);
//             break;
//     }
// }
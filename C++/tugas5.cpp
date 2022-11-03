#include <stdio.h>
#include <string>
int main(){
    // deklarasi variabel
    float tugas1, tugas2, tugas3, tugas4, uts, uas, total, rataTugas;
    char grade;
    std::string nama, nim;
    // input untuk value variabel
    printf("Masukan nama anda : "); scanf("%[^\n]s", &nama);
    printf("Masukan NIM anda : "); scanf("%d", &nim);
    printf("Masukan nilai tugas 1 : "); scanf("%f", &tugas1);
    printf("Masukan nilai tugas 2 : "); scanf("%f", &tugas2);
    printf("Masukan nilai tugas 3 : "); scanf("%f", &tugas3);
    printf("Masukan nilai tugas 4 : "); scanf("%f", &tugas4);
    printf("Masukan nilai UTS : "); scanf("%f", &uts);
    printf("Masukan nilai UAS : "); scanf("%f", &uas);
    // assignment untuk value variabel
    rataTugas = (tugas1+tugas2+tugas3+tugas4)/4;
    total = (rataTugas*0.4) + (uas*0.3) + (uts*0.3);
    // percabangan untuk menetukan grade
    if (total > 80){
        printf("Mahasiswa dengan nama %s dan NIM %d mendapat nilai %f, lulus dengan predikat A",nama, nim, total);
        // grade = 'A';
    }else if (total > 70){
        printf("Mahasiswa dengan nama %s dan NIM %d mendapat nilai %f, lulus dengan predikat B",nama, nim, total);
    //    grade = 'B';
    }else if (total > 60){
        printf("Mahasiswa dengan nama %s dan NIM %d mendapat nilai %f, lulus dengan predikat C",nama, nim, total);
    //    grade = 'C';
    }else{
        printf("Mahasiswa dengan nama %s dan NIM %d mendapat nilai %f, tidak lulus dengan predikat D",nama, nim, total);
    //    grade = 'D';
    }
    // percabangan untuk menampilkan teks kelulusan
    // switch (grade)
    // {
    //     case 'D':
    //         printf("Mahasiswa dengan nama %s dan NIM %d mendapat nilai %f, tidak lulus dengan predikat %c",nama, nim, total, grade);
    //         break;
    //     default:
    //         printf("Mahasiswa dengan nama %s dan NIM %d mendapat nilai %.2f, lulus dengan predikat %c",nama, nim, total, grade);
    //         break;
    // }
}
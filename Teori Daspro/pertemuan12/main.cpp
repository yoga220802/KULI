#include <stdio.h>
#include <conio.h>
int main(int argc, char *argv[]){
    int x, i, k, l[10] = {20, 15, 22, 30, 60, 28, 17, 18, 21, 22};
    printf("Data yang dicari = ");scanf("%d", &x);
    k = 0;
    for (i = 0; i < 9; i++){
        if (l[i] == x){
            printf("Data ditemukan di elemen %d\n", i);
            k++;}}
    if (k == 0){
        printf("Data tidak ditemukan\n");}
    printf("Jumlah data yang ditemukan = %d", k);
    getch();
    return 0;}
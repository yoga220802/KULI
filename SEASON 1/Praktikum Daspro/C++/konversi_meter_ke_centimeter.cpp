#include <stdio.h>
int main(){
    int panjang;
    printf("Masukan panjang dalam satuan meter : ");
    scanf("%d", &panjang);
    printf("panjang %d m ", panjang);
    printf("dalam cm menjadi %d cm", panjang*=100);
}
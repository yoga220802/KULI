#include <stdio.h>
#include <math.h>
int main(){
    int v, m;
    float ek;
    printf("\tMenghitung Energi Kinetik\n");
    printf("Masukan masa benda (Kg) "); scanf("%d", &m);
    printf("Masukan kecepatan benda (m/s) "); scanf("%d", &v);
    ek = float(0.5*v*pow(m, 2));
    printf("Energi kinetik dari benda dengan massa %d Kg dan kecepatan %d m/s adalah %.2f joule", m, v, ek);
    return 0;
}
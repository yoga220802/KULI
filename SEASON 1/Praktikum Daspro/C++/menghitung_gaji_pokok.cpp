#include <stdio.h>
int main(){
    float tjg, mk, gapok, gatot;
    printf("Masukan masa kerja anda : "); scanf("%f", &mk);
    printf("Masukan gaji pokok anda anda : "); scanf("%f", &gapok);
    if (mk > 3) {
        tjg = 0.2*gapok;
    }else {
        tjg = 0.1*gapok;
    }
    gatot = gapok + tjg;
    printf("gaji total anda adalah %.2f", gatot); 
}
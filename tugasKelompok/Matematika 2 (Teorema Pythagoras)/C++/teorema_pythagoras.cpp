#include <stdio.h>
#include <math.h>
int main(){
    int a, b;
    double sisiMiring;
    printf("\tmenghtung sisi miring segitiga siku-siku");
    printf("Input panjang sisi a "); scanf("%d", &a);
    printf("Input panjang sisi b "); scanf("%d", &b);
    sisiMiring = sqrt(pow(a, 2)+pow(b, 2));
    printf("%.2f", sisiMiring);
    return 0;
}
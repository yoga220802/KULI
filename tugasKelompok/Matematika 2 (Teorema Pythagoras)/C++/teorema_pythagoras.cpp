#include <stdio.h>
#include <math.h>
int main(){
    int a, b;
    double sisiMiring;
    printf("\tmenghtung sisi miring segitiga siku-siku\n");
    printf("Input panjang sisi a "); scanf("%d", &a);
    printf("Input panjang sisi b "); scanf("%d", &b);
    sisiMiring = sqrt(pow(a, 2)+pow(b, 2));
    printf("Panjang sisi miring segitiga siku-siku dengan panjang sisi a %d dan panjang sisi b %d adalah %.2f",a, b, sisiMiring);
}
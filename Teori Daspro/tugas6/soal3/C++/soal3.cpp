#include <stdio.h>
using namespace std;
int main(){
    int bil1 = 0, bil2 = 1, n = bil1 + bil2, jml = 1;
    printf("Fibonacci = %d, %d, ", bil1, bil2);
    while (n<=500)
    {
        printf("%d, ",n);
        bil1 = bil2;
        bil2 = n;
        jml += n;
        n = bil1+bil2;
    }
    printf("Jumlah total = %d", jml);
}

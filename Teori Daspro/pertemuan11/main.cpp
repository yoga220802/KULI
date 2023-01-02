#include <stdio.h>
int main(){
    FILE*tulisData = fopen("belajar.bin", "w");
    fprintf(tulisData, "Nama: %s\n", "Andi");
    fprintf(tulisData, "Umur: %s\n", "25");
    fprintf(tulisData, "Alamat: %s\n", "Kampung Durian Runtuh");
    fclose(tulisData);

    // tulisData = fopen("belajar.txt", "a");
    // fprintf(tulisData, "\nNama: %s\n","Eka");
    // fprintf(tulisData, "Umur: %s\n","22");
    // fprintf(tulisData, "Alamat: %s\n","Kebon jeruk");
    // // fprintf(tulisData, "\nNama: %s\n","Abdul");
    // // fprintf(tulisData, "Umur: %s\n","101");
    // // fprintf(tulisData, "Alamat: %s\n","Kebon jeruk");
    // // fprintf(tulisData, "Hobi: %s\n","Bengong");
    // fclose(tulisData);
    
}
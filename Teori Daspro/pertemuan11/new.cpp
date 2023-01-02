#include <stdio.h>
#include <string.h>

int main(){
    FILE*bacaFile= fopen("belajar.txt", "r");
    char string[100]="";
    while (!feof(bacaFile))
    {
        fscanf(bacaFile, "%[^\n]\n", string);
        puts(string);
    }
    return 0;
}
#include <iostream>
using namespace std;
int main()
{
    int jml = 0;
    for (int i = 1; i <= 200; i++)
    {
        if (i % 2 == 0)
        {
            cout << i << ", ";
        }
        jml += i;
    }
    cout <<"Jumlah total = "<< jml;
}
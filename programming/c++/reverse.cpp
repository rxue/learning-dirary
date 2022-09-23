#include <iostream>
using namespace std;
int main() {
    char numb[6];
    cin>> numb;
    int i = 0;
    char reversed[6];
    for (i = 0; i < 6; i++) {
      reversed[i]=numb[5-i];
    }
    cout<<reversed;
    return 0;
}

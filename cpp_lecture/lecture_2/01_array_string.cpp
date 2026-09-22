#include <iostream>

using namespace std;

int main(){

    short month[12] = {1, 2, 3};    //꼭 12원소 다 안채워도 된다.
    short year[] = {4, 5, 6};       // 배열 year의 크기는 자동으로 3으로 지정된다.
    cout << month[0] << endl;
    cout << month[1] << endl;
    cout << year[4] << endl;

    char a[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    char b[] = "Hello";             // 큰따움표 ("")는 null (\0)문자를 담고있음

    cout << a << endl;
    cout << b << endl;
    
    

}

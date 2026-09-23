#include <iostream>

using namespace std;

void helloCPP(int, int);

int main(){

    int times, times2;
    cout << "정수를 입력하십시오. \n";
    cin >> times;

    cout << "정수를 한번 더 입력하십시오. \n";
    cin >> times2;

    helloCPP(times, times2);        // times, times2를 전달인자라 한다.

    return 0;
}

void helloCPP(int n, int m){        // int n, int m을 매개변수라 한다.
    for (int i = 0; i < n; i++)
        cout << "Hello, C++! \n";
    
    for (int i = 0; i < m; i++)
        cout << "Hello, C++! \n";
        
}
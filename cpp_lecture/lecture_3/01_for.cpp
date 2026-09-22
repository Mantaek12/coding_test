#include <iostream>


using namespace std;

int main()
{
    char a[10] = {'a', 'b' , 'c', 'd', 'e'};

     for(int i = 0; i < 5; i++){
        cout << i << "번째입니다."<< endl;
     }
    
    
    int c = 10;
    int d = 10;

    cout << "c는" << c << ", d는" << d << endl;
    cout << "c++는" << c++ << endl;
    cout << "c++는" << c << endl;           // 10에서 11로 증가됨 
    cout << "++d는" << ++d << endl;
    cout << "c는" << c << ", d는" << d << endl;

    for(int i = 5; i > 0; i--){     // i > 0 | 좌항이 크다면 true / 그렇지 않다면 False임. 즉, true일때만 for문이 돈다.
        // cout << "감소연산자" << endl;
        cout << i << "번째입니다."<< endl;
    }


    // 비교 연산자
    /*
    < : 좌항이 작다
    <= : 작거나 같다
    > : 크다
    >= : 크거나 같다
    == : 같다
    != : 같지 않다
    */


}
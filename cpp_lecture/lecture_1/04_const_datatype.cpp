/* 
상수 변수 선언 방법 1
*/

// #include <iostream>
// #define PIE 3.1415926535

// using namespace std;

// int main(){
//     // 원의 넓이를 구하는 프로그램

//     int r = 3;
//     // float s = r * r * 3.14;

//     float s = r * r * PIE;



//     cout << s << endl;

// }

/* 
상수 변수 선언 방법 2
*/

// #include <iostream>

// using namespace std;

// int main(){
//     // 원의 넓이를 구하는 프로그램

//     const float PIE = 3.1415926535;
//     // PIE = 10.0;      // 상수로 선언된 변수는 절대 변환불가. 초기화만 가능
//     int r = 3;
//     r = 5;
//     float s = r * r * PIE;

//     cout << s << endl;

// }


/*
데이터형 변환
*/

#include <iostream>

using namespace std;

int main(){

    int a = 3.141592;       // 3으로 출력됨
    cout << a << endl;

    // 강제적으로 데이터형 변환
    //typeName(a) (typeName)a

    char ch = 'M';
    cout << (int)ch << " " << int(ch) << endl;

    // static_cast<typeName>
    cout << static_cast<int>(ch) << " " << int(ch) << endl;


}

#include <iostream>

using namespace std;

int main(){

    // union Myunion       //서로 다른 데이터형을 한 번에 한 가지만 보관할 수 있음
    // {
    //     int intVal;
    //     long longVal;
    //     float floatVal;
    // };

    // Myunion test;
    // test.intVal = 3;
    // cout << test.intVal << endl;
    // test.longVal = 33;
    // cout << test.intVal << endl;
    // cout << test.longVal << endl;
    // test.floatVal = 3.3;
    // cout << test.intVal << endl;
    // cout << test.longVal << endl;
    // cout << test.floatVal << endl;

    enum spectrum {red, orange, yellow, green, blue, violet, indigo, ultraviolet}; // 기호 상수를 만드는 것에 대한 또 다른 방법

    /*
    1. spectrum을 새로운 데이터형 이름으로 만든다.
    2. red, orange, yellow .. 0에서부터 7까지 정수 값을 각각 나타내는 기호 상수로 만든다.
    */

    spectrum a = orange;
    cout << a << endl;
  
    // spectrum a = orange + yellow;       // 열거자들끼리는 사칙연산 불가. 다만 아래처럼 integer로 취급하여 연산 가능

    int b;
    b = blue;
    b = blue + 3;
    cout << b << endl;

    int c;
    c = orange + b;    
    cout << c << endl;


    // 초기화 하는 열거자들의 값은 반드시 int여야함. 특정 갑승ㄹ 지정하지 않은 열거자들은 마지막 값에서 1씩 증가함
    // 아래의 예제에서 green은 5, blue는 6, violet은 7 ... 을 가짐
    enum spectrum {red = 0, orange = 2, yellow = 4, green, blue, violet, indigo, ultraviolet}; 


    return 0;

}
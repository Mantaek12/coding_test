#include <iostream>

using namespace std;

int main(){

    // 배열 : 같은 데이터형의 집합
    // 구조체 : 다른 데이터형이 허용되는 데이터의 집합

    // 축구선수

    struct MyStruct
    {
        string name;            // 각각을 멤버 변수라함
        string position;
        float height;
        float weight;

    } C;

    MyStruct A;
    
    A.name = "Son";
    A.position = "Striker";
    A.height = 183;
    A.weight = 77;

    MyStruct B= {
            "Son",
            "Stricker",
            183, 
            77};
    
    cout << B.name << endl;
    cout << B.position << endl;
    cout << B.height << endl;
    cout << B.weight << endl;

    C = { };

    cout << C.name << endl;
    cout << C.position << endl;
    cout << C.height << endl;
    cout << C.weight << endl;

    MyStruct D[2] = {
        {"A", "A", 1, 1},
        {"B", "B", 2, 2}
    };


    cout << D[0].height << endl;
    cout << D[1].position << endl;

    return 0;

}
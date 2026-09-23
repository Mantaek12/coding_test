#include <iostream>

using namespace std;

const float PIE = 3.14;
void cheers(int n);             // 함수의 원형을 표시한다. main함수 상단에 입력해야함
float circle(float x);


int main(){

    /*
    1. 리턴값이 있는 타입

    typeName functionName(parameterList)
    {
        statements(s);
        return value;
    }

    2. 리턴값이 없는 타입
    void functionName(parameterList)
    {
        statemets(s);
        return; // 생략될 수 있음
    }
    */
    
    int a;
    cout << "하나의 수를 입력하십시오." << endl;
    cin >> a;
    cheers(a);

    float b;
    cout << "원의 반지름 길이를 입력하십시오." << endl;
    cin >> b;
    float c = circle(b);
    cout << "원의 넓이는 " << c <<"입니다. " << endl; 
    return 0;
}



void cheers(int n){             // void선언이라 return 없어도 됨
    for (int i = 0; i < n; i++){
        cout << "Cheers!" << endl;
    }
}

float circle(float x){
    return x * x * PIE;
}
#include <iostream>

using namespace std;

int main()
{
    // // for : 이미 정해진 횟수로 반복 | for문 선언 내부 ex. for(int i = 0; i < 3; i++)처럼 조건을 설계해야함
    // // while : 언제 끝날지 모르지만 특정 조건 만족할 때까지 반복

    // string str = "Panda";   //큰따옴표는 \0가 들어가있기에 아래와 같은 while문 작성 가능
    // int i = 0;
    // // while (str[i] != '\0'){
    // //     cout << str[i] <<endl;
    // //     i++;
    // // }

    // bool a = true;
    // bool b = false;

    // while (a){
    //     cout << "hello\n" ;   
    // }


    // while문은 조건을 검사하고 반복문을 실행함 | do-while문은 반복문을 실행하고 조건을 검사 따라서 한번은 무조건 실행됨 (아래 예제 참고)
    
    bool j = false;

    do{
        cout << "while문 입니다. \n";
        
    } while (j);

    return 0;

}
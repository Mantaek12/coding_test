#include <iostream>
#include <cstring>

using namespace std;

int main(){

    // const int Size = 15;
    // char name1[Size];
    // char name2[Size] = "C++programing";

    // cout << "안녕하세요! 저는 " << name2;
    // cout << "입니다! 성함이 어떻게 되시나요? \n";
    // // cin >> name1;                                   // 사용자의 입력을 name1에 저장하겠다.
    // cin.getline(name1, Size);
    // cout << "음, " << name1 << "씨, 당신의 이름은 ";
    // cout << strlen(name1) << " 자 입니다만\n";
    // cout << sizeof(name1) << " 바이트 크기의 배열에 저장되었습니다.\n";
    // cout << "이름이" << name1[0] << "자로 시작하는군요.\n";
    // name2[3] = '\0';
    // cout << "제 이름의 처음 세 문자는 다음과 같습니다: ";
    // cout << name2 << endl;

    // return 0;


    /*
    C++에서 문자열을 다루는 방법중 하나인 STRING
    */

    char char1[20];        
    char char2[20] = "jauar";
    string str1;
    string str2 = "panda";
    // char1 = char2;      // 오류 발생 (잘못됨) | 배열의 한계 -> 배열에 다른 배열을 넣을수 없다.
    str1 = str2;        // 가능한 표현

    cout << str1 << endl;
    cout << str1[0] << endl;

    return 0;
}
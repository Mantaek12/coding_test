#include <iostream>

using namespace std;

int main(){

    // int a[10] = {1, 3, 5, 7, 9};

    // // for (int i = 0; i < 5; i++){
    // //     cout << a[i];
    // // }
    // // cout << "\n";


    // // 배열 기반 반복문  | 배열 크기보다 값들 수가 작으면 0들이 찍힘 (아래 예제 참고)
    // for (int i : a){
    //     cout << i;
    // }
    

    // 중첩 루프 : 2차원 배열에서 가장 많이 활용됨
    
    // int temp[4][5];         // 총 배열 크기가 4인데, 각 배열은 5개의 값들을 가짐 | Table 표 같은 선언
    // for (int row = 0; row < 4; row++){
    //     for (int col = 0; col < 5; col++){
    //         cout << temp[row][col] << endl;
    //     }
    // }

    int temp[4][5] = 
    {
        {1, 2, 3, 4, 5},
        {11, 22, 33, 44, 55},
        {111, 222, 333, 444, 555},
        {1111, 2222, 3333, 4444, 5555},
    };

    for (int row = 0; row < 4; row++){
        for (int col = 0; col < 5; col++){
            cout << temp[row][col] << " ";
        }
        cout << "\n";
    }

    return 0;
}
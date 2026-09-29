// #include <string>
// #include <unordered_map>
// #include <vector>
// #include <iostream>

// using namespace std;

// int solution(vector<vector<string>> clothes) {
//     unordered_map<string, int> clothesCount;

//     for (const auto& cloth : clothes) {
//         clothesCount[cloth[1]]++;
//     }

//     int answer = 1;

//     for (const auto& clothesInfo : clothesCount) {
//         answer *= clothesInfo.second + 1;
//     }

//     return answer - 1;
// }

// int main() {
//     vector<vector<string>> clothes = {
//         {"yellow_hat", "headgear"},
//         {"blue_sunglasses", "eyewear"},
//         {"green_turban", "headgear"}
//     };

//     cout << solution(clothes) << '\n';  // Expected output: 5

//     vector<vector<string>> clothes2 = {
//         {"crow_mask", "face"},
//         {"blue_sunglasses", "face"},
//         {"smoky_makeup", "face"}
//     };

//     cout << solution(clothes2) << '\n';  // Expected output: 3

//     return 0;
// }


// #include <iostream>
// #include <string>
// #include <unordered_map>

// using namespace std;

// int main() {

//     // key는 string, value는 int
//     unordered_map<string, int> a;

//     // 1. 값 저장
//     a["headgear"] = 5;
//     a["eyewear"] = 3;
//     a["shoes"] = 2;


//     // 2. key를 이용해서 value 가져오기
//     cout << a["headgear"] << endl;
//     cout << a["eyewear"] << endl;



//     // 3. unordered_map 전체를 하나씩 확인
//     for (const auto& x : a) {

//         cout << "key: " << x.first << endl;
//         cout << "value: " << x.second << endl;

//     }

//     return 0;
// }
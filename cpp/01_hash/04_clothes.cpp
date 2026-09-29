#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_map<string, int> clothesCount;

    for (const auto& cloth : clothes) {
        clothesCount[cloth[1]]++;
    }

    int answer = 1;

    for (const auto& clothesInfo : clothesCount) {
        answer *= clothesInfo.second + 1;
    }

    return answer - 1;
}

int main() {
    vector<vector<string>> clothes = {
        {"yellow_hat", "headgear"},
        {"blue_sunglasses", "eyewear"},
        {"green_turban", "headgear"}
    };

    cout << solution(clothes) << '\n';  // Expected output: 5

    vector<vector<string>> clothes2 = {
        {"crow_mask", "face"},
        {"blue_sunglasses", "face"},
        {"smoky_makeup", "face"}
    };

    cout << solution(clothes2) << '\n';  // Expected output: 3

    return 0;
}

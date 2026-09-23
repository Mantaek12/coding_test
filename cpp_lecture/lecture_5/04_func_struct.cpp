#include <iostream>

using namespace std;

struct Time
{
    int hours;
    int mins;
};

const int minsPerHr = 60;

Time sum(Time*, Time*);

int main(){
    // 함수는 원본이 아닌 복사본을 대상으로 작업한다.

    Time day1 = {5, 45};
    Time day2 = {4, 55};



    return 0;
}

Time sum(Time* t1, Time* t2){
    Time total;

    total.mins = (t1 -> mins + t2 -> mins) % minsPerHr;
    total.hours = t1 -> hours + t2 -> hours + (t1->mins + t2 -> mins)/minsPerHr;

    return total;
}
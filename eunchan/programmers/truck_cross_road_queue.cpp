#include <iostream>
#include <vector>
#include <deque>
/*
cpp 에서는 pop 의 반환 값이 없음으로 front, back method를 사용해야함.

문제파악
1. 트럭은 1초에 1m 전진
2. 트럭의 크기는 1m인듯
3. 다리 위에 weight 이상 무게가 올라가면 다리가 무너짐
4. 그러면 도착할 때 바로 다음 트럭이 올라갈 수 있는지 확인 필요.
*/
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int weight_now = 0;
    deque<int> ready (truck_weights.begin(), truck_weights.end());
    deque<int> bridge ( bridge_length, 0 );
    while(!ready.empty()){
        answer += 1;
        weight_now += ready.front();
        if (bridge.front()){
            weight_now -= bridge.front();
        }
        if(weight_now > weight){
            weight_now -= ready.front();
            bridge.push_back(0);
        } else {
            bridge.push_back(ready.front());
            ready.pop_front();
        }
        bridge.pop_front();
    }
    while(weight_now){
        answer += 1;
        weight_now -= bridge.front();
        bridge.pop_front();
    }
    return answer;
}

// 풀이과정 :
/*
1. 다리를 건너는 트럭과 대기중인 트럭을 각각 bridge와 ready 라는 덱으로 표현한다.
2. bridge 덱의 크기는 다리의 길이인 bridge_length로 초기화한다.
3. ready 덱에서 트럭이 다리를 건너는 동안, bridge 덱의 맨 앞에 있는 트럭이 다리를 완전히 건넜는지 확인한다. 
   만약 맨 앞에 있는 트럭이 다리를 완전히 건넜다면, 해당 트럭을 bridge 덱에서 제거하고 weight_now 변수에서 해당 트럭의 무게를 빼준다.
4. 만약 ready 덱에서 트럭이 다리를 건너는 동안, bridge 덱의 맨 앞에 있는 트럭이 다리를 완전히 건넜다면, 
   해당 트럭을 bridge 덱에서 제거하고 weight_now 변수에서 해당 트럭의 무게를 빼준다.
5. ready 덱에서 트럭이 다리를 건너는 동안, bridge 덱의 맨 앞에 있는 트럭이 다리를 완전히 건넜는지 확인한다.
   만약 맨 앞에 있는 트럭이 다리를 완전히 건넜다면, 해당 트럭을 bridge 덱에서 제거하고 weight_now 변수에서 해당 트럭의 무게를 빼준다.
6. ready 덱이 빌때까지 반복하고, 이후에는 weight_now 변수가 0이 될 때까지 bridge 덱에서 트럭이 다리를 완전히 건넜는지 확인한다. 
   만약 맨 앞에 있는 트럭이 다리를 완전히 건넜다면, 해당 트럭을 bridge 덱에서 제거하고 weight_now 변수에서 해당 트럭의 무게를 빼준다.
*/
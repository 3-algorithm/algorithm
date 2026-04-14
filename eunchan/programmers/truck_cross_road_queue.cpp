#include <deque>
#include <vector>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int weight_now = 0;
    deque<int> ready(truck_weights.begin(), truck_weights.end());
    deque<int> bridge(bridge_length, 0);
    while (!ready.empty()) {
        answer += 1;
        weight_now += ready.front();
        if (bridge.front()) {
            weight_now -= bridge.front();
        }
        if (weight_now > weight) {
            weight_now -= ready.front();
            bridge.push_back(0);
        } else {
            bridge.push_back(ready.front());
            ready.pop_front();
        }
        bridge.pop_front();
    }
    while (weight_now) {
        answer += 1;
        weight_now -= bridge.front();
        bridge.pop_front();
    }
    return answer;
}

// 풀이과정 :
/*
1. 다리를 건너는 트럭과 대기 중인 트럭을 각각 bridge와 ready 덱으로 표현한다.
2. bridge 덱은 다리 길이인 bridge_length만큼 0으로 초기화해, 비어 있는 칸까지 함께 관리한다.
3. 매 초마다 bridge의 맨 앞 원소를 기준으로 다리에서 빠져나가는 트럭을 반영하고, weight_now에서 해당 무게를 빼준다.
4. 그 다음 대기 중인 트럭의 무게를 더해도 제한 무게를 넘지 않으면 bridge 뒤에 트럭을 넣고, 넘으면 0을 넣어 한 칸 전진만 시킨다.
5. ready 덱이 빌 때까지 위 과정을 반복한 뒤, 남아 있는 bridge의 트럭들이 모두 빠져나갈 때까지 시간을 추가로 계산한다.
*/

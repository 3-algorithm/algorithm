#include <deque>
#include <set>
#include <vector>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    deque<int> deq(priorities.begin(), priorities.end());
    multiset<int> priority_set(priorities.begin(), priorities.end());

    while (!deq.empty()) {
        int current_max = *priority_set.rbegin();
        if (deq.front() == current_max) {
            priority_set.erase(priority_set.find(deq.front()));
            deq.pop_front();
            ++answer;
            --location;
        } else {
            deq.push_back(deq.front());
            deq.pop_front();
            --location;
        }

        if (location < 0) {
            if (deq.empty()) {
                break;
            }
            location = static_cast<int>(deq.size()) - 1;
        }
    }

    return answer;
}

// 풀이과정 :
/*
1. 큐의 맨 앞 문서와 현재 문서들 중 최고 우선순위를 비교한다.
2. 최고 우선순위 문서라면 출력하고, 아니라면 큐의 뒤로 보낸다.
3. 출력될 때마다 answer를 증가시키고, location은 현재 큐 기준으로 함께 이동시킨다.
4. location이 음수가 되면 현재 큐의 마지막 인덱스로 보정해 같은 문서를 계속 추적한다.
*/

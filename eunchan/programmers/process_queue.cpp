#include <string>
#include <vector>
#include <deque>

using namespace std;

int find_max(deque<int> lst){
    int max = 0;
    for(int i=0; i<lst.size(); i++){
        if(lst[i] > max){
            max = lst[i];
        }
    }
    return max;
}

int solution(vector<int> priorities, int location) {
    int answer = 0;
    deque<int> deq (priorities.begin(), priorities.end());
    int max = find_max(deq);
    while(!deq.empty()){
        if(deq.front() == max){
            deq.pop_front();
            answer += 1;
            location -= 1;
            max = find_max(deq);
        } else {
            deq.push_back(deq.front());
            deq.pop_front();
            location -= 1;
            if(location < 0){
                location = deq.size() - 1;
            }
        }
        if(location < 0){
            break;
        }
    }
    return answer;
}

// 풀이과정 :
/*
1. 우선순위가 가장 높은 문서가 현재 큐의 맨 앞에 있는지 확인한다.
2. 만약 우선순위가 가장 높은 문서가 현재 큐의 맨 앞에 있다면, 해당 문서를 출력한다.
3. 만약 우선순위가 가장 높은 문서가 현재 큐의 맨 앞에 없다면, 해당 문서를 큐의 맨 뒤로 보낸다.
4. 문서가 출력될 때마다 location 변수를 1씩 감소시킨다
5. location 변수가 0이 되는 경우, 해당 문서가 출력된 것이므로 answer 변수를 1 증가시킨다.
*/
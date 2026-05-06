/* BFS and Search All 
    문제 
    N X M 의 공간을 0,0부터 탐색하기 시작한다.
    각 칸은 주소를 가지고 있는데, 예를 들어 2X5 공간이 있다면
    각 주소는
    1 2 3 4 5
    6 7 8 9 10
    이 된다.
    
    꼭 방문해야할 정점 n개가 주소 값으로 주어질 때, 
    각 정점을 모두 방문하는 최단 경로를 찾는 문제이다.

    입력예시 : 
    N = 3, M = 4 P = [1, 2, 6, 7]
    출력예시 : 6
    */
#include <string>
#include <vector>
#include <deque>
#include <iostream>

using namespace std;

vector<int> visit (10001, 0);

vector<vector<int>> bfs(vector<vector<int>> map, vector<int> P, int N, int M){
    deque<vector<int>> q;
    vector<vector<int>> visited (N, vector<int>(M, 0));
    vector<vector<int>> find (N, vector<int>(M, 0));
    vector<vector<int>> delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    q.push_back(P);
    while(!q.empty()){
        vector<int> now = q.front();
        q.pop_front();
        for(vector<int> d : delta){
            vector<int> next = {now[0] + d[0], now[1] + d[1]};
            if(next[0] < 0 || next[0] >= N || next[1] < 0 || next[1] >= M){
                continue;
            }
            int next_address = next[0] * M + next[1] + 1;
            // 방문해야할 정점이면서 아직 방문하지 않은 경우
            if(visit[next_address]){
                visit[next_address] = 0;
                return {next, {visited[now[0]][now[1]] + 1}};
            }
            if(!visit[next_address] && map[next[0]][next[1]] == 0){
                q.push_back(next);
                map[next[0]][next[1]] = map[now[0]][now[1]] + 1;
            }
        }
    }
}

int solution(int N, int M, vector<int> P){
    int answer = 0;
    vector<vector<int>> map (N, vector<int>(M, 0));
    for (int p : P){
        visit[p] = 1;
    }
    for (int p : P){
        vector<vector<int>> result = bfs(map, {p/M, p%M}, N, M);
        if(result.empty()){
            return -1;
        }
        answer += result[1][0];
    }
    
    return answer;
}

// main 함수는 테스트용입니다. 프로그램 제출 시 main 함수는 제거해주세요.
int main(){
    int N = 3, M = 4;
    vector<int> P = {1, 2, 6, 7};
    cout << solution(N, M, P) << endl;
}
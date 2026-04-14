#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int width = 0;
    int height = 0;
    for(vector<int> size : sizes){
        if(size[0] < size[1]){
            int tmp = size[0];
            size[0] = size[1];
            size[1] = tmp;
        }
        if(size[0] > width){
            width = size[0];
        }
        if(size[1] > height){
            height = size[1];
        }
    }
        
    answer = width * height;
    return answer;
}

// 풀이과정 :
/*
1. 명함의 가로와 세로 중 큰 값을 가로로, 작은 값을 세로로 생각한다.
2. 모든 명함의 가로 중 가장 큰 값을 전체 가로로, 
   세로 중 가장 큰 값을 전체 세로로 생각한다.
3. 전체 가로와 세로를 곱한 값을 반환한다.
PLUS. 명함의 가로와 세로를 비교하여 큰 값을 가로로, 작은 값을 세로로 생각하는 이유는 명함을 회전시킬 수 있기 때문이다.
*/
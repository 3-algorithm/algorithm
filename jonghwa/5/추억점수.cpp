#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    unordered_map<string, int> score_map;
    
    // 이름과 그리움 점수를 해시 맵에 저장 
    for (int i = 0; i < name.size(); i++) {
        score_map[name[i]] = yearning[i];
    }
    
    // 각 사진별로 추억 점수 계산
    for (int i = 0; i < photo.size(); i++) {
        int current_score = 0;
        
        // 해당 사진 속 인물들을 하나씩 확인
        for (int j = 0; j < photo[i].size(); j++) {
            string current_name = photo[i][j];
            
            // 맵에 해당 이름이 존재하는지 확인 
            if (score_map.find(current_name) != score_map.end()) {
                current_score += score_map[current_name]; // 존재하면 점수 합산
            }
        }
        
        // 계산된 현재 사진의 총점을 answer 배열에 추가
        answer.push_back(current_score);
    }
    
    return answer;
}
#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    int stack = 0;
    for(char c : s){
        if(c == '('){
            stack += 1;
        } else {
            stack -= 1;
        }
        if(stack < 0){
            answer = false;
            break;
        }
    }
    if(stack){
        answer = false;
    }
    return answer;
}
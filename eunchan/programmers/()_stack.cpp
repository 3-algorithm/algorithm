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
// 풀이 : 스택의 형식을 취해서 '(' 가 나오면 스택에 push 하는 대신 
// stack 변수에 1을 더하고, ')' 가 나오면 
// stack 변수에 1을 빼는 방식으로 구현하였다.
// stack 변수가 음수가 되는 경우는 ')' 가 '(' 보다 먼저 나오는 경우이므로 
// 올바르지 않은 괄호 문자열이 된다.
// 문자열이 모두 탐색된 후 stack 변수가 0이 아닌 경우는 
// '(' 가 ')' 보다 더 많이 나오는 경우이므로 올바르지 않은 괄호 문자열이 된다.
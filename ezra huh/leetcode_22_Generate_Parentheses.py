import copy
# 딥카피 + 약간의 다이나믹 프로그래밍을 활용한 재귀 풀이
# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        N = n*2
        ans = []
        def combs(left_cnt, right_cnt, comb): # 여는 괄호와 닫는 괄호의 수를 카운팅해서 인자로 넘기고, 지금까지 완성된 리스트도 넘김
            nonlocal N, ans # 함수 내에 존재하는 변수 호출이니 nonlocal로 불러옴
            if left_cnt + right_cnt == N: # 여는괄호 수 + 닫는괄호 수 합쳐서 N이라면 -> 완성된 것
                ans.append("".join(comb)) # 언패킹해서 정답에 join
                return

            if left_cnt < (N / 2):
                left_comb = copy.deepcopy(comb) # 딥카피로 새로운 조합 저장할 리스트 생성
                left_comb.append("(")           # 여는 괄호
                combs(left_cnt + 1, right_cnt, left_comb)
            if right_cnt < (N / 2) and right_cnt < left_cnt: # 성립 안되는 조합 방지 위한 조건식: 닫는 괄호는 절대 이미 존재하는 여는 괄호보다 수가 더 많아질 수 없다.
                right_comb = copy.deepcopy(comb) # 마찬가지.
                right_comb.append(")")
                combs(left_cnt, right_cnt + 1, right_comb)


        combs(0, 0, [])
        return ans
    


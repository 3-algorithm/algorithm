# 백트래킹을 활용한 풀이 (제미나이)
# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def backtrack(left_cnt, right_cnt, comb): # 마찬가지의 로직
            if len(comb) == n*2:
                ans.append(comb)
                return

            if left_cnt < n:
                backtrack(left_cnt + 1, right_cnt, comb + "(")
                
            if right_cnt < n and right_cnt < left_cnt:
                backtrack(left_cnt, right_cnt + 1, comb + ")")

        backtrack(0, 0, "")
        return ans
    


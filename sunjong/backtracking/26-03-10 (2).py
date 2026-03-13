import sys

# 입력을 빠르게 받기 위한 설정
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    path = [] # 현재 선택한 숫자들을 담을 리스트

    def backtrack(start, depth):
        # m개를 모두 선택했을 때 출력
        if depth == m:
            print(*(path))
            return

        # start부터 시작하여 중복 조합(자기 자신 포함)을 허용
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i, depth + 1) # 다음 단계에서도 현재 숫자(i)부터 선택 가능
            path.pop()

    backtrack(1, 0)

if __name__ == "__main__":
    solve()

import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    heights = list(map(int, input_data[1:]))
    
    # 각 탑의 결과를 담을 리스트 (0으로 초기화)
    answer = [0] * n
    # (높이, 1부터 시작하는 인덱스)를 담을 스택
    stack = []
    
    for i in range(n):
        current_h = heights[i]
        
        # 현재 탑보다 낮은 앞선 탑들은 무의미하므로 스택에서 제거
        while stack and stack[-1][0] < current_h:
            stack.pop()
            
        # 스택에 남아있는 게 있다면, 그게 바로 현재 탑의 신호를 받을 가장 가까운 왼쪽 탑
        if stack:
            answer[i] = stack[-1][1]
        
        # 현재 탑 정보를 스택에 추가 (높이, 1-based 인덱스)
        stack.append((current_h, i + 1))
    
    # 결과 출력
    print(*(answer))

if __name__ == "__main__":
    solve()
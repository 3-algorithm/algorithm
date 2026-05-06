import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().splitlines()
    
    for line in input_data:
        parts = list(map(int, line.split()))
        n = parts[0]
        
        # n이 0이면 종료
        if n == 0:
            break
            
        heights = parts[1:]
        stack = []
        max_area = 0
        
        for i in range(n):
            # Java 코드의 arr[stack.peek()] > num 로직
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                # 스택이 비어있으면 가로 길이는 i, 아니면 i - 1 - stack[-1]
                width = i if not stack else i - 1 - stack[-1]
                max_area = max(max_area, height * width)
            
            stack.append(i)
            
        # 반복문 종료 후 스택에 남은 기둥들 처리
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - 1 - stack[-1]
            max_area = max(max_area, height * width)
            
        print(max_area)

if __name__ == "__main__":
    solve()

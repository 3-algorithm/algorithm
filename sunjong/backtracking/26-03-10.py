import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.read

def solve():
    # 전체 데이터를 한 번에 읽어와서 나누기
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    nums = sorted(list(map(int, data[2:]))) # 숫자 정렬

    visited = [False] * n
    select = [0] * m
    result = []

    def backtrack(depth):
        if depth == m:
            # 결과 리스트에 현재 선택된 숫자들을 문자열로 합쳐서 저장
            result.append(" ".join(map(str, select)))
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                select[depth] = nums[i]
                backtrack(depth + 1)
                visited[i] = False

    backtrack(0)
    
    # 한 번에 출력 (자바의 StringBuilder와 같은 효과)
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    solve()

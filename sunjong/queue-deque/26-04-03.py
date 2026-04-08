from collections import deque
import sys

# 빠른 입출력을 위해 사용
input = sys.stdin.read

def solve():
    # 모든 데이터를 한 번에 읽어와 처리
    data = input().split()
    if not data:
        return
    
    n, m = map(int, data[:2])
    arr = list(map(int, data[2:]))

    dq = deque()  # 인덱스를 저장할 덱
    result = []

    for i in range(n):
        # 1. 범위를 벗어난 인덱스 제거 (윈도우 크기 m 유지)
        if dq and dq[0] <= i - m:
            dq.popleft()

        # 2. 현재 값보다 큰 값들은 뒤에서 제거 (나보다 큰 애들은 최솟값이 될 자격이 없음)
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()

        # 3. 현재 인덱스 추가
        dq.append(i)

        # 4. 덱의 맨 앞이 항상 최솟값의 인덱스임
        result.append(str(arr[dq[0]]))

    # 결과 한꺼번에 출력 (출력 속도 향상)
    sys.stdout.write(" ".join(result) + "\n")

solve()

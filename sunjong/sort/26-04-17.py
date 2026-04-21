# https://www.acmicpc.net/problem/15666

import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    n, m = map(int, input().split())
    # 2. 중복 제거 후 정렬 (이 문제의 핵심)
    arr = sorted(list(set(map(int, input().split()))))
    
    seq = []

    def backtracking(start, depth):
        # 3. 목표 길이에 도달하면 출력
        if depth == m:
            print(*seq)
            return

        # 4. start 인덱스부터 탐색하여 비내림차순 유지
        for i in range(start, len(arr)):
            seq.append(arr[i])
            # 다음 재귀에도 현재 인덱스(i)를 넘겨주어 중복 선택 허용
            backtracking(i, depth + 1)
            seq.pop()

    backtracking(0, 0)

solve()

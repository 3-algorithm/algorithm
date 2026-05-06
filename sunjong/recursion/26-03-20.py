# https://www.acmicpc.net/problem/1074

import sys

n, r, c = map(int, sys.stdin.readline().split())

def solve(n, r, c):
    if n == 0:
        return 0
    
    # 현재 단계에서 한 변의 길이의 절반
    half = 2**(n-1)
    # 한 사분면의 크기 (정사각형 넓이)
    area = half * half
    
    # 1사분면 (왼쪽 위)
    if r < half and c < half:
        return solve(n - 1, r, c)
    # 2사분면 (오른쪽 위)
    elif r < half and c >= half:
        return area + solve(n - 1, r, c - half)
    # 3사분면 (왼쪽 아래)
    elif r >= half and c < half:
        return 2 * area + solve(n - 1, r - half, c)
    # 4사분면 (오른쪽 아래)
    else:
        return 3 * area + solve(n - 1, r - half, c - half)

print(solve(n, r, c))

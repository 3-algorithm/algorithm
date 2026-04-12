# SWEA 차윤이의 알씨카 

import sys
sys.stdin = open(" rc_input.txt")


from collections import deque


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 필드의 크기
    graph = [list(input()) for _ in range(N)]
    Q = int(input())
    commands = [list(input().split()) for _ in range(Q)]

    for y in range(N):
        for x in range(N):
            if graph[y][x] =='X':
                sx, sy = x, y
            if graph[y][x] == 'Y':
                ex, ey = x, y

    dx = [0, 1, 0, -1] # x = 오른쪽으로 갈수록 증가 
    dy = [-1, 0, 1, 0]  # y = 아래로 갈수록 증가 

    result = []
  

    for command in commands:
        x, y = sx, sy
        dir = 0
        for c in command[1]:
            if c == 'A':
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < N and 0 <= ny <N and graph[ny][nx]!= 'T':
                    x, y = nx, ny

            if c == 'L':
                dir = (dir-1) % 4
            if c == 'R':
                dir = (dir +1) % 4
        if x == ex and y == ey:
            result.append(1)
        else:
            result.append(0)

    print(f'#{tc}', *result)
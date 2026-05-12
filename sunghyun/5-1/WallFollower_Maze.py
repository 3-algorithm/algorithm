'''벽 짚고 미로 탈출하기

90XP

평균 180분

29% 정답률

총 제출 3,325회

N×N 크기의 격자 안에서 주어진 위치에서 우측 방향을 바라보고 시작하여 오른쪽 벽을 짚고 쭉 따라가는 방식으로 미로를 탈출하는 프로그램을 작성해보세요. 규칙에 맞게 이동하다 격자 밖을 벗어났을 때 미로를 탈출 한 것으로 봅니다.

벽을 짚고 탈출하는 방식은 다음과 같습니다.

Step 1 : 바라보고 있는 방향으로 이동하는 것이 가능하지 않은 경우

반 시계 방향으로 90 ∘만큼 방향을 바꿉니다.

Step 2 : 바라보고 있는 방향으로 이동하는 것이 가능한 경우

Case 1 : 바로 앞이 격자 밖이라면 이동하여 탈출합니다.

Case 2 : 만약 그 방향으로 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 짚을 벽이 있다면 그 방향으로 한 칸 이동합니다.

Case 3 : 만약 그 방향으로 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 벽이 존재하지 않는다면, 현재 방향으로 한 칸 이동 후 방향을 시계 방향으로 90' 만큼 방향을 틀어 한 칸 더 전진하여 오른쪽에 벽이 있게끔 합니다.'''

import sys
sys.stdin = open('input.txt', 'r')

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


n = int(input())
x, y = map(int, input().split())
grid = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

stack = []
stack.append((x - 1, y - 1, 0))
rst = -1
cnt = 0
d = 0

running = True
while stack:
    i, j, d = stack.pop()
    cnt += 1
    visited[i][j] += 1
    if visited[i][j] > 4:
        break
    
    # 오른쪽에 벽 없으면
    if grid[i + dirs[(d + 1) % 4][0]][j + dirs[(d + 1) % 4][1]] != '#':
        new_d = (d + 1) % 4
        next_i = i + dirs[new_d][0]
        next_j = j + dirs[new_d][1]

    else:
        next_i = i + dirs[d][0]
        next_j = j + dirs[d][1]
        new_d = d
    

    if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
        rst = cnt
        break
    
    # 1. 다음칸 벽이냐 아니냐
    t = 0
    while grid[next_i][next_j] == '#':
        t += 1
        if t > 4:
            running = False
            break

        new_d = (new_d - 1) % 4
        next_i, next_j = i + dirs[new_d][0], j + dirs[new_d][1]
        # print(next_i, next_j)
        if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
            rst = cnt
            running = False
            break
    
    if running:
        stack.append((next_i, next_j, new_d))

print(rst)

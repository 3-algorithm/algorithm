'''뱀은 사과를 좋아해

80XP

평균 180분

40% 정답률

총 제출 1,560회

N×N 크기의 격자 안에서 사과들의 위치와 뱀의 움직임이 주어졌을 때, 게임이 끝나는데 몇 초가 걸리는지를 구하는 프로그램을 작성해보세요.

뱀은 처음에 좌측 상단 (1, 1)에서 길이 1의 상태로 있습니다.

일반적으로 뱀은 이동시에 머리를 특정 방향으로 한 칸 옮기게 되고, 가장 끝에 있던 꼬리가 사라지게 되며 이 과정은 동시에 일어납니다.

이때 만약 움직인 장소에 사과가 존재한다면 꼬리가 사라지지 않고 몸의 길이가 1 늘어나게 됩니다. 또, 사과는 먹는 즉시 사라지게 됩니다.

뱀이 움직이는 데에는 1초의 시간이 소요됩니다.

게임은 뱀이 전부 움직였거나, 움직이는 도중 격자를 벗어났거나, 움직이는 도중 몸이 꼬여 서로 겹쳐졌을 경우 종료됩니다.'''

from collections import deque
from copy import deepcopy

# 격자 크기, 사과 개수, 방향 전환 횟수
N, M, K = map(int, input().split())
grid = [[0] * (N + 1) for _ in range(N + 1)]

# 사과 위치
for _ in range(M):
    ax, ay = map(int, input().split())
    grid[ax][ay] = 1

dq = deque()
dq.append([1, 1])
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dir = {
    'U': 3,
    'D': 1,
    'L': 2,
    'R': 0
}

rst = 0
running = True
for _ in range(K):
    if running:
        d, t = input().split()
        t = int(t)
        while t:
            # print(dq)
            f = dq[0]
            way = dir[d]
            # 다음 자리
            next_x = f[0] + dirs[way][0]
            next_y = f[1] + dirs[way][1]
            # 격자 안벗어남
            if 0 < next_x <= N and 0 < next_y <= N:
                # 다음 자리에 사과 있으면
                if grid[next_x][next_y] == 1:
                    dq.appendleft([next_x, next_y])
                    grid[next_x][next_y] = 0
                # 사과 없으면
                else:
                    len_dq = len(dq)
                    if len_dq != 1:
                        # 몸통 이동시킬 때 deepcopy안하면 같이 바뀌는 문제발생
                        dq1 = deepcopy(dq)
                        # 몸통 한칸씩 이동
                        for idx in range(len_dq - 1, 0, -1):
                            dq[idx] = dq1[idx -1]
                        # 몸통에 부딪힘: 게임 종료
                        if [next_x, next_y] in dq:
                            running = False
                            rst += 1
                            t = 0
                            break
                    f[0] = next_x
                    f[1] = next_y
                rst += 1
                t -= 1
            # 격자 벗어남: 게임 종료
            else:
                rst += 1
                running = False 
                break

print(rst)

# 이동할 때 다 옮기지 말고 꼬리 제거, 머리 추가하는 방식으로

'''
direction_map = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3,
}

dirs = [
    (0, 1),   # R
    (1, 0),   # D
    (0, -1),  # L
    (-1, 0),  # U
]

dx, dy = dirs[direction_map[d]]
nx, ny = x + dx, y + dy
'''
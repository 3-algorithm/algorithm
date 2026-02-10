import sys
from pprint import pprint
sys.stdin = open('snail_input.txt')

T = int(input())

# for each test
for tc in range(T):
    # N 인풋 받음
    N = int(input())
    # N x N 0인 matrix 만들음
    matrix = [[0]*N for _ in range(N)]

    # 내가 이동할 방향을 파악하기 위한 델타를 만들자
    deltas = [
        [0, 1], # 오른쪽
        [1, 0], # 아래
        [0, -1], # 왼쪽
        [-1, 0] # 위
    ]
    # 내가 지금 진행하고 있는 이동방향을 지정할 변수를 만들자
    dir_idx = 0
    # 현재 detals[dir_idx] 방향으로 이동하다가
    # 만약 해당 방향으로 이동하지 못할 경우
    # dir_idx += 1 해준다. 그러면 방향이 바뀐다.

    # 내가 다음에 숫자를 작성할 칸을 기록할 변수를 만든다
    now = [0, -1]
    # N * N 만큼 반복해서 숫자를 작성한다
    for next_num in range(1, N*N + 1):
    # 진행방향으로 이동한다.
        now[0] += deltas[dir_idx][0]
        now[1] += deltas[dir_idx][1]

    # 이동한 위치에 다음 숫자를 작성한다.
        matrix[now[0]][now[1]] = next_num

    # 내 다음 위치가 막혀있는지 확인하고,
    # 만약 막혀있다면, 진행 방향을 바꿔준다.
    next_y = now[0] + deltas[dir_idx][0]
    next_x = now[1] + deltas[dir_idx][1]
    wall = not (0 <= next_y < N and 0 <= next_x < N)

    blocked = wall or matrix[next_y][next_x] != 0

    if blocked:
        dir_idx += 1
        dir_idx %= 4

    for row in matrix:
        print(row)
# 오른쪽(x+1)으로 가면서 칸에 숫자를 하나씩 늘림
# x = N이거나 다음 칸이 0이 아니면
# 아래로 내려가면서 칸에 숫자를 하나씩 늘림
# y = N이거나 다음 칸이 0이 아니면
# 왼쪽(x-1)으로 가면서 칸에 숫자를 하나씩 늘림
# x=0이거나 다음 칸이 0이 아니면
# 위로 올라가면서 칸에 숫자를 하나씩 늘림

# repeat

    pprint(matrix)

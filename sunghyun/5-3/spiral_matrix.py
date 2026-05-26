'''
빙빙 돌며 숫자 사각형 채우기


50XP

평균 28분

65% 정답률

총 제출 5,173회

N×M크기의 직사각형에 수 1부터 순서대로 증가시키며 달팽이 모양으로 채우는 코드를 작성해보세요.

달팽이 모양이란 왼쪽 위 모서리에서 시작해서, 오른쪽, 아래쪽, 왼쪽, 위쪽 순서로 더 이상 채울 곳이 없을 때까지 회전하는 모양을 의미합니다.
N : 행(row), M : 열(column)을 의미합니다.
'''


import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

i, j = 0, 0
d = 0
num = 1
stack = [(i, j)]
while num <= n * m:
    grid[i][j] = num
    di, dj = i + dirs[d][0], j + dirs[d][1]
    if 0 <= di < n and 0 <= dj < m and not grid[di][dj]:
        i, j = di, dj
    else:
        d = (d + 1) % 4
        i, j = i + dirs[d][0], j + dirs[d][1]
    num += 1

for row in grid:
    print(*row)
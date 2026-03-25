# 바킹독 - 재귀 - 쿼드트리
# https://www.acmicpc.net/problem/1992

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

temp = []
def quadtree(x, y, n):
    if n==1:
        temp.append(str(arr[y][x]))
        return

    first = arr[y][x]
    same = True
    for j in range(y, y+n):
        for i in range(x, x+n):
            if arr[j][i] != first:
                same = False
                break
    if same:
        temp.append(str(first))
        return
    size = n//2
    temp.append('(')

    for j in range(2):
        for i in range(2):
            quadtree(x+i*size, y+ j*size, size)

    temp.append(')')

quadtree(0, 0, N)
print(''.join(temp))

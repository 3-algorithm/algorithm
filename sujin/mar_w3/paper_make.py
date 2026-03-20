# 바킹독 - 재귀 - 색종이 만들기
# https://www.acmicpc.net/problem/2630

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

colours = [0, 0] # 인덱스 0: 흰색, 1: 파랑

def cut_paper(x, y, n):
    global colours

    # 칸이 1이면 끝
    if n == 1:
        colours[arr[y][x]] += 1
        return
    # 해당 칸 색이 다 똑같지 않으면 갯수 +1
    first = arr[y][x]
    same = True
    for j in range(y, y+n):
        for i in range(x, x+n):
            if arr[j][i] != first:
                same = False
                break
    if same:
        colours[first] += 1
        return
    # 안 같으면 가로 새로 2등부
    else:
        size = n//2
        for j in range(2):
            for i in range(2):
                cut_paper(x + i*size, y + j*size, size)

cut_paper(0,0, N)
print(colours[0])
print(colours[1])
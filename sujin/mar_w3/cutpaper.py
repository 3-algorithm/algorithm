# https://www.acmicpc.net/problem/1780
# 바킹독 - 재귀

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

number = [0, 0, 0]
same1 = 0
same2 = 0
same3 = 0
def cut_paper(x, y, n): # 엑스인덱스, 와이인덱스, 가로길이
    global number
    if n== 1:
        number[arr[y][x]] += 1
        return

    first = arr[y][x]
    same = True
    # 다 같은수면 컷페이퍼 +1
    for j in range(y, y+n):
        for i in range(x, x+n):
            if arr[j][i] != first:
                same = False
                break
    if same:
        number[first] +=1
        return


    # 아니면 종이를 9개로 자름름
    size = n//3
    for j in range(3):
        for i in range(3):
            cut_paper(x+i*size, y+j*size, size)

cut_paper(0, 0, N)
print(number[-1])
print(number[0])
print(number[1])

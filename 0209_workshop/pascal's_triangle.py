import sys
sys.stdin = open('pascal_input.txt')

T = int(input())

# for each case
for tc in range(1, T+1):
    N = int(input())

    # 0으로 채워진 메트릭스 만들음
    matrix = [[0]*i for i in range(1, N+1)]

    # 양 가쪽 1로 채움
    matrix[0][0] = 1
    y = 0

    for i in range(N):
        matrix[y][0] = 1
        matrix[y][i] = 1
        y +=1

    for y in range(2, N):
        for x in range(1, y):
            matrix[y][x] = matrix[y-1][x-1] + matrix[y-1][x]

    print(f'#{tc}')
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

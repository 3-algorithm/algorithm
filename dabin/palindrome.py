import sys
sys.stdin = open("input_pal.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]
    voca = []

    for i in range(N):
        for j in range(N - M + 1):
            x_bol = True
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:
                    x_bol = False
            if x_bol == True:
                for m in range(M):
                    voca.append(arr[i][j + m])

    for j in range(N):
        for i in range(N - M + 1):
            y_bol = True
            for k in range(M // 2):
                if arr[i + k][j] != arr[i + M - 1 - k][j]:
                    y_bol = False
            if y_bol == True:
                for m in range(M):
                    voca.append(arr[i + m][j])


    print(f"#{tc} {''.join(voca)}")

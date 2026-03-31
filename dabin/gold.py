import sys
sys.stdin = open("input_gold.txt")

def bfs(a, b):
    available_dir = []
    available_dir.append([a, b])
    visited[a][b] = 1
    global cnt
    cnt = 1
    gold = arr[a][b]

    while available_dir:
        x, y = available_dir.pop(0)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] != 0 and visited[nx][ny] == 0:
                    available_dir.append([nx, ny])
                    visited[nx][ny] = 1
                    gold += arr[nx][ny]
                    cnt += 1

    return gold, cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    gold_num = []
    max_gold = []

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == 0:
                gold_num.append(bfs(i, j))
                
    max_gold = gold_num[0]          
    for item in gold_num:
        if max_gold[0] < item[0]:
            max_gold = item
        elif max_gold[0] == item[0]:
            if max_gold[1] > item[1]:
                max_gold = item
        
    print(f"#{tc} {max_gold[0]} {max_gold[1]}")
        
import sys
sys.stdin = open("input_cabage.txt")

def bfs(i, j):
    available_dir = []
    available_dir.append([i, j])
    visited[i][j] = 1

    while available_dir:
        x, y = available_dir.pop(0)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                    available_dir.append([nx, ny])
                    visited[nx][ny] = 1

    return 0

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    cabage = [list(map(int, input().split())) for _ in range(K)]
    
    matrix = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for item in cabage:
        matrix[item[1]][item[0]] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    
    print(f"#{tc} {cnt}")       


import sys
sys.stdin = open("input_miro_distance.txt")

def bfs(i, j):
    
    available_dir = []
    available_dir.append([i, j])
    
    
    while available_dir:
        
        x, y = available_dir.pop(0)
        
        if arr[x][y] == 3:
            return visited[x][y] - 1
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and  0 <= ny < N :
                if arr[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    available_dir.append([nx, ny])
        
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _  in range(N)]
    
    visited = [[0] * N for _ in range(N)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                
    result = bfs(start[0], start[1])
    print(f"#{tc} {result}")
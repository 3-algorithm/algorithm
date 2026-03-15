import sys
sys.stdin = open("input_miro.txt")

def bfs(i, j):
    # 가능한 경로 좌표 저장할 배열 초기화
    available_dir = []
    # 처음에 받는 값 배열에 저장
    available_dir.append([i, j])
    # 해당 좌표 방문 표시
    visited[i][j] = 1
    
    # 가능한 경로가 있는 동안 돌기
    while available_dir:
        # 저장되어 있는 가능한 경로 중 첫번째 값의 좌표를 x, y에 꺼내오기
        x, y = available_dir.pop(0)
        
        # 만약에 꺼내온 좌표의 값이 3이면 도착했으므로 1 반환
        if arr[x][y] == 3:
            return 1
        
        # 델타 방향 돌면서 확인
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 상하좌우로 움직인 좌표가 인덱스 내에 있으면
            if 0 <= nx < N and 0 <= ny < N:
                # 해당 인덱스의 값이 1이 아니고 방문한 적도 없다면
                if arr[nx][ny] != 1 and visited[nx][ny] == 0:
                    # 방문 표시
                    visited[nx][ny] = 1
                    # 가능 경로에 저장
                    available_dir.append([nx, ny])
                    
    # 가능 경로를 다 돌았음에도 3을 만나지 못했기 때문에 0 반환
    return 0
    
T = int(input())   
 
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    
    visited = [[0] * N for _ in range(N)]
    
    # 방향 좌표 설정
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 행렬 돌면서 시작점 좌표 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                
    # bfs에 시작점 넣어서 결과값 받기
    result = bfs(start[0], start[1])    
        
        
    print(f"#{tc} {result}")
            
          
                
        
        
                    
import sys
sys.stdin = open("input_drawing.txt")

def bfs(i, j):
    # 델타 돌면서 각 방향으로 갈 수 있는 좌표를 저장할 리스트 초기화
    available_dir = []
    # 처음으로 들어온 좌표를 avaliable_dir 리스트에 저장
    available_dir.append([i, j])
    # 해당 좌표도 방문했기 때문에 방문 체크
    visited[i][j] = 1
    # 면적을 저장할 변수 초기화
    area = 0

    # available_dir에 저장된 게 있는 동안만(값이 1인 게 있는 경우만)
    while available_dir:
        # 리스트에서 첫번째 좌표 꺼내서 x, y에 저장
        x, y = available_dir.pop(0)
        # while을 도는 동안 available 리스트에서 값을 꺼낸다는 건 연속된 그림을 찾는다는 것이므로 면적 증가
        area += 1

        # 상하좌우 돌면서 좌표 nx, ny에 임시 저장
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 좌표가 인덱스 내에 있으면서
            if 0 <= nx < N and 0 <= ny < M:
                # 값이 1이고 방문한 적이 없다면
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    # available 리스트에 해당 좌표 저장 후 
                    available_dir.append([nx, ny])
                    # 방문 표시
                    visited[nx][ny] = 1
    # 면적 반환
    return area
        

# N x M 행렬값 입력 받기
N, M = map(int, input().split())

# 행렬 입력 받기
arr = [list(map(int, input().split())) for _ in range(N)]

# 델타 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방문 체크할 행렬 생성
visited = [[0] * M for _ in range(N)]
# 그림의 개수를 저장할 변수 초기화
cnt = 0
# 각 그림의 넓이를 저장할 리스트 초기화
drawing = []

# 행렬 돌면서
for i in range(N):
    for j in range(M):
        # 값이 1이고(그림이고) 방문한 적이 없으면
        if arr[i][j] == 1 and visited[i][j] == 0:
            # 그림이 있다는 뜻이므로 개수 하나 증가
            cnt += 1
            # BFS 함수 돌려서 구한 그림의 면적을 drawing 리스트에 저장
            drawing.append(bfs(i, j))

# 함수에서 구해서 불러들인 면적이 없다면 개수와 면적 둘 다 0으로 출력
if not drawing:
    print(0)
    print(0)
# 그림의 개수와 면적 리스트 중 최댓값 출력
else:
    print(cnt)
    print(max(drawing))

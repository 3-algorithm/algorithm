import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = int(1e9)

def dijkstra(N, arr):
    # 비용 저장할 2차원 배열 생성
    distance = [[INF] * N for _ in range(N)]
    # 거리, 좌표 임시 저장할 큐 초기화
    q = []
    # 시작점에 거리 0으로 초기화
    heapq.heappush(q, (0, 0, 0))
    # 시작점 비용 0 초기화
    distance[0][0] = 0

    # 큐가 차 있는 동안 돌면서
    while q:
        # 첫번째 값 빼서 dist, x, y에 저장
        dist, x, y = heapq.heappop(q)
        # 해당 좌표의 비용이 여태 저장된 비용보다 크다면 넘김
        if distance[x][y] < dist:
            continue
        # 상하좌우 돌면서
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 안에 있다면
            if 0 <= nx < N and 0 <= ny < N:
                # 현재 좌표에서 직전 좌표까지의 비용 차를 diff에 저장
                diff = arr[nx][ny] - arr[x][y]
                # 비용 차가 0보다 크다면 그 값과 1(이동비용)을 더해서 cost에 저장
                cost = 1 + max(0, diff)
                # 새로운 비용에 갱신
                new_cost = dist + cost
                # 만약 갱신된 비용값이 여태까지 저장된 것보다 작다면
                if new_cost < distance[nx][ny]:
                    # 새로 저장
                    distance[nx][ny] = new_cost
                    # 큐에 저장
                    heapq.heappush(q, (new_cost, nx, ny))

    return distance[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(N, arr)
    print(f"#{tc} {result}")


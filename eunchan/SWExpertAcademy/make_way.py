# swea 1249
"""
전투에서 승리하기 위해서는 기갑사단과 보급부대가 신속하게 이동하기 위한 도로가 있어야 한다.

공병대는 출발지(S) 에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행하려고 한다.

도로가 파여진 깊이에 비례해서 복구 시간은 증가한다.

출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오.


[입력]

가장 첫 줄은 전체 테스트케이스의 수이다.

각 테스트 케이스마다 지도의 크기(N x N)가 주어진다. 지도의 크기는 최대 100 x 100이다.

그 다음줄 부터 지도의 크기만큼 2차원 배열 형태의 지도 정보가 주어진다.
 

[출력]

각 테스트 케이스의 답을 순서대로 출력하며, 각 케이스마다 줄의 시작에 “#C”를 출력하여야 한다.

이때 C는 케이스의 번호이다.

같은 줄에 빈 칸을 하나 두고, 주어진 입력에서 출발지에서 도착지까지 가는 경로 중에 복구 작업에 드는 시간이 가장 작은 경로의 복구 시간을 출력하시오.
"""
# 이 문제의 경우에는 나는 dfs, gemini 추천 방식은 dijkstra여서 둘 다 구현하고
# 함수 호출 횟수를 트래킹 해봤는데, 이거 한번 해보세요!
# 겁나 신기함.
import collections
import heapq

t = int(input())


def dijkstra():
    global append_cnt_dks
    # 1. 우선순위 큐 생성: (누적비용, y, x)
    # 누적 비용이 작은 것부터 pop하기 위해 비용을 맨 앞에 둠
    pq = [(0, 0, 0)]
    min_dist[0][0] = 0

    while pq:
        dist, y, x = heapq.heappop(pq)

        # 2. 이미 기록된 거리보다 현재 꺼낸 거리가 더 크다면 (이미 최적화됨) 무시
        if min_dist[y][x] < dist:
            continue

        # 3. 도착점에 오면 바로 리턴해도 됨 (가장 작은 값부터 뽑으므로)
        if y == N - 1 and x == N - 1:
            return dist

        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                cost = dist + arr[ny][nx]
                # 4. 더 짧은 경로를 발견했을 때만 갱신하고 큐에 삽입
                if cost < min_dist[ny][nx]:
                    min_dist[ny][nx] = cost
                    heapq.heappush(pq, (cost, ny, nx))
                    append_cnt_dks += 1


def bfs(now, goal, visited, min_dist):
    global append_cnt_bfs
    q = collections.deque()
    q.append(now)
    while q:
        n = q.popleft()
        for d in delta:
            dy, dx = n[0] + d[0], n[1] + d[1]
            if 0 <= dx <N and 0 <= dy < N:
                if min_dist[n[0]][n[1]] + arr[dy][dx] < min_dist[dy][dx]:
                    min_dist[dy][dx] = min_dist[n[0]][n[1]] + arr[dy][dx]
                    q.append((dy, dx))
                    append_cnt_bfs += 1

for tes in range(1, t+1):
    N = int(input())
    append_cnt_bfs = 0
    append_cnt_dks = 0
    arr = [list(map(int, input())) for _ in range(N)]
    # min_dist = [[float('inf')] * N for _ in range(N)]
    # min_dist[0][0] = 0
    # visited = [[False] * N for _ in range(N)]
    # visited[0][0] = True
    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    # bfs((0, 0), (N-1, N-1), visited, min_dist)
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    min_dist = [[float('inf')] * N for _ in range(N)]
    ans = dijkstra()
    print(f"#{tes}", min_dist[N-1][N-1])

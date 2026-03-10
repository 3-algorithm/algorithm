import sys
sys.stdin = open("maze_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visited = []
    stack = []
    result = 0
# 2에서 출발, 3에서 도착
    for y in range(N):
        for x in range(N):
            if arr[y][x] ==2:
                visited.append((x,y))
                stack.append((x,y))
    delta = [(0,1), (1,0), (0,-1), (-1,0)]
# 출발지점에서 시계방향으로 탐색
    while stack:
        x_now, y_now = stack.pop()
        if arr[y_now][x_now] ==3:
            result = 1
            break
        for d in delta:
            x_go = x_now +d[0]
            y_go = y_now +d[1]
            # 인덱스 범위 안에 있고, 앞에 길이 있고, 간적이 없으면 갈 수 있는 곳임
            if 0<= x_go <=N-1 and 0<= y_go <=N-1 and (arr[y_go][x_go]==0 or arr[y_go][x_go]==3) and (x_go, y_go) not in visited:
                stack.append((x_go, y_go))
                visited.append((x_go, y_go))

    print(f'#{tc}', result)
s
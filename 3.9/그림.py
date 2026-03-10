from collections import deque
import sys
input = sys.stdin.readline
n,m=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

cnt=0
area=0
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y]=True

    area = 1

    while queue:
        cx,cy=queue.popleft()

        #상하좌우 탐색
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            #전체 범위 벗어났는지 확인
            if 0<=nx<n and 0<=ny<m:
                #만약 색칠 돼있고 방문을 안했다면 
                if graph[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    area+=1
    return area

for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and not visited[i][j]:
            cnt+=1
            current_area=bfs(i,j)
            area = max(current_area,area)

print(cnt)
print(area)


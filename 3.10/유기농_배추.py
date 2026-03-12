import sys 
input = sys.stdin.readline
from collections import deque

def bfs(r,c):
    queue = deque()
    queue.append((r,c))
    visited[r][c]=True
    while queue:
        cr,cc = queue.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<= nr < N  and 0<= nc<M:
                if not visited[nr][nc] and land[nr][nc]==1:
                    visited[nr][nc]=True
                    queue.append((nr,nc))


T=int(input())
for tc in range(1,T+1):
    M,N,K=map(int,input().split())

    land = [[0]*M for _ in range(N)]
    visited=[[False]*M for _ in range(N)]

    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    for i in range(K):
        c,r=map(int,input().split())
        land[r][c]=1
        
    cnt=0
    for i in range(N):
        for j in range(M):
            if land[i][j]==1 and not visited[i][j]:
                bfs(i,j)
                cnt+=1
    
    print(cnt)



    
    

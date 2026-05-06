import sys
from collections import deque
input=sys.stdin.readline

def dfs(n):
    visited_dfs[n]=True
    print(n,end=' ')
    for i in graph[n]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(start):
    q=deque([start])
    visited_bfs[start]=True

    while q:
        v=q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i]=True
                q.append(i)

   
N,M,V=map(int,input().split())

#인접리스트(그래프 생성)[][][][][][][][][][]
graph=[[] for _ in range(N+1)]

for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

visited_bfs=[False]*(N+1)
visited_dfs=[False]*(N+1)

dfs(V)
print()
bfs(V)
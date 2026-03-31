import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N,M=map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


count=0

for i in range(1,N+1):
    if not visited[i]:
        count+=1
        dfs(i)

print(count)
        

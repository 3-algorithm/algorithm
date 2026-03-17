N=int(input())
pairs=int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)


for _ in range(pairs):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)

dfs(1)

print(f'{sum(visited)-1}')
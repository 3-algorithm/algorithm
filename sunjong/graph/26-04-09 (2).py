# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, st = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())

    graph[u][v] = 1
    graph[v][u] = 1

s_visited = [0] * (n + 1)


def dfs(cur):
    if s_visited == 1:
        return
    print(cur, end=' ')
    s_visited[cur] = 1
    for nxt in range(n + 1):
        if s_visited[nxt] == 1 or graph[cur][nxt] == 0:
            continue
        dfs(nxt)


dfs(st)

print()

q = deque()
q_visited = [0] * (n + 1)

q.append(st)
q_visited[st] = 1

while q:
    cur = q.pop()
    print(cur, end=' ')
    for nxt in range(n + 1):
        if q_visited[nxt] == 1 or graph[cur][nxt] == 0:
            continue
        q.appendleft(nxt)
        q_visited[nxt] = 1

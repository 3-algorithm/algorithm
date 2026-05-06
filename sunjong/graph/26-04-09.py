# https://www.acmicpc.net/problem/11724

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

stack = []
visited = [0] * (n + 1)
cnt = 0
for i in range(1, n + 1):
    if visited[i] == 1:
        continue
    stack.append(i)
    visited[i] = 1

    while stack:
        cur = stack.pop()

        for nxt in graph[cur]:
            if visited[nxt] == 1:
                continue
            stack.append(nxt)
            visited[nxt] = 1
    cnt += 1

print(cnt)

# https://www.acmicpc.net/problem/11779

from heapq import heappush, heappop

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])


def dijkstra(st):
    dists = [float('inf')] * (n + 1)
    pq = [[0, st]]
    pre_node = [0] * (n + 1)
    dists[st] = 0

    while pq:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue

        for nxt_dist, nxt_node in graph[node]:
            new_dist = dist + nxt_dist
            if dists[nxt_node] < new_dist:
                continue
            pre_node[nxt_node] = node
            heappush(pq, [new_dist, nxt_node])
            dists[nxt_node] = new_dist

    return dists, pre_node


start, end = map(int, input().split())
result_dists, pre_node = dijkstra(start)

path = []
curr = end
while curr != 0:
    path.append(curr)
    curr = pre_node[curr]

path.reverse()

print(result_dists[end])
print(len(path))
print(' '.join(map(str,path)))

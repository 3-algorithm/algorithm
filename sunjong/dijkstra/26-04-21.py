# https://www.acmicpc.net/problem/1753

from heapq import heappush, heappop

V, E = map(int, input().split())
k = int(input())

graph = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])


def dijkstra(start_node):
    dists = [float('inf')] * (V + 1)
    pq = [[0, start_node]]
    dists[start_node] = 0

    while pq:
        dist, cur_node = heappop(pq)

        if dists[cur_node] < dist:
            continue

        for nxt_w, nxt_node in graph[cur_node]:
            nxt_dist = dist + nxt_w
            if nxt_dist < dists[nxt_node]:
                dists[nxt_node] = nxt_dist
                heappush(pq, [nxt_dist, nxt_node])

    return dists


l = dijkstra(k)

for i in range(1, V + 1):
    if l[i] == float('inf'):
        print('INF')
        continue
    print(l[i])

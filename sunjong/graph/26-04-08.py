from heapq import heappop, heappush


def dijkstra(start_node):
    pq = [[start_node, 0]]
    dists = [int(21e8)] * (n + 1)
    dists[start_node] = 0

    while pq:
        node, dist = heappop(pq)

        for nxt_node, nxt_dist in graph[node]:
            new_dist = dist + nxt_dist

            if dists[nxt_node] <= new_dist:
                continue

            dists[nxt_node] = new_dist
            heappush(pq, [nxt_node, new_dist])
    return dists


tc = int(input())

for t in range(1, tc + 1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    dists = dijkstra(0)

    print(f'#{t} {dists[n]}')
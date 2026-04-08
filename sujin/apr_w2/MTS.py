# [S/W 문제해결 구현] 7일차 - 최소 신장 트리

import sys
sys.stdin = open("MTS_input.txt")

from heapq import heappop, heappush

def MTS(start):
    pq = [(0, start)]
    visited = [0] * (V+1)
    min_weight = 0

    while pq:
        weight, node = heappop(pq)
        if visited[node]:
            continue

        visited[node] = 1
        min_weight +=weight

        for next_weight, next_node in tree[node]:
            if visited[next_node]:
                continue
            heappush(pq, (next_weight, next_node))
    return min_weight

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(E)]

    tree = [[] for _ in range(V+1)]
    for n1, n2, w in graph:
        tree[n1].append((w, n2))
        tree[n2].append((w, n1)) # 양방향

    result = MTS(0)
    print(f'#{tc}', result)
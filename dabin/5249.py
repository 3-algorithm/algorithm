def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    parent = [i for i in range(v+1)]

    edges = []
    result = 0

    for _ in range(e):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    edges.sort()

    for w, n1, n2 in edges:
        if find_parent(parent, n1) != find_parent(parent, n2):
            union_parent(parent, n1, n2)
            result += w

    print(f"#{tc} {result}")
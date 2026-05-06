# https://www.acmicpc.net/problem/2606
# 바이러스

N = int(input())
E = int(input()) # 연결된 페어 개수

graph = [list(map(int, input().split())) for _ in range(E)]

routes = [[] for _ in range(N+1)]

for start, end in graph:
    routes[start].append(end)
    routes[end].append(start) # 양방향

print(routes)
count = 0
def virus(node):
    global count
    count +=1
    for next_node in routes[node]:
        if visited[next_node]:
            continue
        visited[next_node]= 1
        virus(next_node)

visited = [0]*(N+1)
visited[1] =1

virus(1)

print(count -1)





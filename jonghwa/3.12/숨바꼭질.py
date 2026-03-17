import sys
input = sys.stdin.readline
from collections import deque
# 걷거나 (+-1) 순간이동 (2*x )

N,K=map(int,input().split())
visited = [-1]*100001
visited[N]=0

queue=deque()
queue.append(N)

while queue:
    x = queue.popleft()
    if x==K:
        print(visited[x])
        break
    for nx in (x-1,x+1,2*x):
        if 0<=nx<=100000 and visited[nx]==-1:
            visited[nx] = visited[x] + 1
            queue.append(nx)

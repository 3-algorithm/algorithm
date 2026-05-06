import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())

maze=[list(input().strip()) for _ in range(R)]

# R x C 크기의 배열을 -1로 초기화
fire_time = [[-1] * C for _ in range(R)]
jihun_time = [[-1] * C for _ in range(R)]

J_queue=deque()
F_queue=deque()

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for r in range(R):
    for c in range(C):
        if maze[r][c]=='J':
            jihun_time[r][c]=0
            J_queue.append((r,c))

for r in range(R):
    for c in range(C):
        if maze[r][c]=='F':
            fire_time[r][c]=0
            F_queue.append((r,c))

def solve():
    #불 퍼져나감
    while F_queue:
        r,c=F_queue.popleft()
        for i in range(4):
           nr = r + dr[i]
           nc = c + dc[i]

           if 0<=nr<R and 0<=nc<C:
               if maze[nr][nc]!='#' and fire_time[nr][nc]==-1:
                   fire_time[nr][nc]=fire_time[r][c]+1
                   F_queue.append((nr,nc))
    #지훈이 이동
    while J_queue:
        r,c=J_queue.popleft()
        if r==0 or r==R-1 or c==0 or c==C-1:
            return jihun_time[r][c] + 1

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if 0<=nr<R and 0<=nc<C:
                if maze[nr][nc]!='#' and jihun_time[nr][nc]==-1:
                # 대망의 불과의 시간 비교!
                # 불이 아예 도달할 수 없는 곳(-1)이거나, 
                # 지훈이가 도착하는 시간이 불보다 짧은 경우만 이동 가능
                    if fire_time[nr][nc]==-1 or fire_time[nr][nc]> jihun_time[r][c]+1:
                        jihun_time[nr][nc] = jihun_time[r][c]+1
                        J_queue.append((nr,nc))

    return "IMPOSSIBLE"

print(solve())



            


import sys
from collections import deque  
sys.stdin = open("미로1.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    N=int(input())
    maze=[list(map(int,input().strip())) for _ in range(16)]
    #플래그 사용
    found=False
    #델타탐색
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    #출발점 찾기
    start_x=0
    start_y=0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x=i
                start_y=j
                break
    #큐에 출발점 좌표 튜플 추가
    queue = deque()
    queue.append((start_x,start_y))
    #큐가 빌때까지 반복
    while queue:
        #
        x,y= queue.popleft()

        #상하좌우 방향 체크
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<16 and 0<=ny<16:
                if maze[nx][ny]==3:
                    found=True
                elif maze[nx][ny]==0:
                    queue.append((nx,ny))
                    maze[nx][ny]=1
    
    if found ==True:
        print(f'#{tc} {1}')
    elif found == False:
        print(f'#{tc} {0}')
    

    # ///////////////////////////////////////////////////////////////////////////////////
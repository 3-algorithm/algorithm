# 마을 구분하기
# 에듀트리 a형 대비: https://www.codetree.ai/ko/external-connection/classes/324/lectures/3470/curated-cards/challenge-seperate-village/description
# 마을 파티션을 나누는 기준: 벽 visited True로 세워놓고
# 벽 가기 전에 갈 수 있는 만큼 bfs. 
# 왜 dfs말고 bfs하냐 -> 칸 전체 다 따져봐야해서
# 마을 개수에 카운트 추가하고 첫번째 마을 인구수 카운트 추가
# 큐 다털어서 끝나면 이제 포문으로 탐색해서 visited[i][j] == False인 곳을 찾음
# 오름차순 정렬 한줄 하나 출력

from collections import deque
import sys

sys.stdin = open('edutree_village.txt')

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
village = []
cnt = 0

def bfs(x,y):
    global village
    global cnt
    queue = deque()
    queue.append([x,y])
    while queue:
        now = queue.popleft()
        crr_x = now[0]
        crr_y = now[1]

        if visited[crr_x][crr_y] == True:
            continue

        visited[crr_x][crr_y] = True
        cnt += 1

        for i in range(4):
            next_x = crr_x + di[i]
            next_y = crr_y + dj[i]
            if -1 < next_x < n and -1 < next_y < n and visited[next_x][next_y] == False:
                queue.append([next_x, next_y])
                
    village.append(cnt)
    cnt = 0



visited = [[False] * n for _ in range(n)] 

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 0:
            visited[i][j] = True

di = [0,1,0,-1]
dj = [1,0,-1,0]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i,j)

print(len(village))
ans = sorted(village)
for i in range(len(ans)):
    print(ans[i])
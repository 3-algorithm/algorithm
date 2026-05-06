# 덱 활용 + 멀티소스 bfs
# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        fresh_oranges = 0
        rotten_sources = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten_sources.append([i,j])

        def bfs(): # 멀티소스 bfs
            queue = deque()
            min_cnt = 0
            nonlocal rotten_sources, fresh_oranges

            for i in range(len(rotten_sources)):
                queue.append(rotten_sources[i])
            
            while queue:
                level_size = len(queue) # 멀티소스이므로 모든 오렌지는 한번에 썩어야 함
                rotted = False

                for _ in range(level_size): # 한번 썩는 싸이클
                    now = queue.popleft()
                    x = now[0]
                    y = now[1]

                    for i in range(4):
                        new_x = x + di[i]
                        new_y = y + dj[i]
                        if -1 < new_x < len(grid) and -1 < new_y < len(grid[new_x]) and grid[new_x][new_y] == 1:
                            grid[new_x][new_y] = 2
                            queue.append([new_x, new_y])
                            rotted = True
                            fresh_oranges -= 1
                            
                if rotted == True: # for 싸이클이 한번 끝나면
                    min_cnt += 1 # 분에 추가

            if fresh_oranges == 0:
                return min_cnt
            else:
                return -1
        
        return bfs()
        
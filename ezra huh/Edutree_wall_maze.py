# https://www.codetree.ai/ko/external-connection/classes/324/lectures/3486/curated-cards/challenge-escape-maze-with-wall-following/description
# counter clockwise: 0 1 -> -1 0 -> 0 -1 -> 1 0 -> 0 1
# 방향 처리를 해야한다. 우측 보고 있으면 x축 +1 벽이다
# 북쪽 보고 있으면 y축 +1 이 벽
# 왼쪽 보고 있으면 x축 -1이 벽
# 남쪽 보고 있으면 y축 -1 이 벽

# 벽 찾기 탐색 -> 이동을 한다 했을 때:
# 우측 이동했다면 & 벽 감지가 안되는 상황이라면 (코너인 경우)
# clockwise 무브 -> 한칸 전진

# 단순한 경로 탐색이고 최단 시간 구하기 이런 케이스도 아니니
# dfs로 가자

def dfs(x,y,dir):
    # 1. 일단 내가 바라보는 dir 기준 오른쪽 (dir + 1)을 먼저 확인하고 벽인지 확인한다
    # 2. 벽이면 앞으로 갈 준비를 하고 앞 방향을 본다.
    # 그리드를 벗어났다면? 정답이니 return
    # 앞이 막혀있다면? dir -1 하고 다음 dfs로 넘긴다
    # 앞이 뚫려있다면 앞으로 전진시키고 카운트 +1 하고 dfs 넘긴다
    # 3. 벽이 아니라면 dir +1로 회전시키고 다음 dfs로 넘긴다

    global cnt

    while True:
        if (x,y,dir) in visited_states:
            cnt = -1
            return
        visited_states.add((x,y,dir))

        wall_dir = (dir + 1) % 4
        left_dir = (dir - 1) % 4
        right_dir = (dir + 1) % 4
        # print(wall_dir)
        # print(f'current dir is {dir}')
        # print(f'current coor is {x,y}')
        wall_x = x + di[wall_dir]
        wall_y = y + dj[wall_dir]
        if -1 < wall_x < N and -1 < wall_y < N and grid[wall_x][wall_y] == '#':
            new_x = x + di[dir]
            new_y = y + dj[dir]
            # print(new_x, new_y)
            if new_x < 0 or N <= new_x or new_y < 0 or N <= new_y:
                # print('goal!')
                cnt += 1
                break
            elif grid[new_x][new_y] == '#':
                # print('another wall found... turning clockwise')
                dir = left_dir
                continue
            elif grid[new_x][new_y] == '.':
                cnt += 1
                # print(f'path found! current count is {cnt}')
                x = new_x
                y = new_y
                continue
        else:
            # print(f'no wall found... trying to move - current coor: {x,y}')
            new_dir = right_dir
            # print(new_dir)
            new_x = x + di[new_dir]
            new_y = y + dj[new_dir]
            if grid[new_x][new_y] == '#':
                cnt = -1
                break
            else:
                cnt += 1
                x = new_x
                y = new_y
                dir = new_dir

N = int(input())
x, y = map(int, input().split()) # starting point

grid = [list(input()) for _ in range(N)]

visited_states = set()

cnt = 0
di = [0,1,0,-1]
dj = [1,0,-1,0]
#     우,하,왼,상
# print(visited)
dfs(x-1,y-1,0)
# print(visited)
print(cnt)
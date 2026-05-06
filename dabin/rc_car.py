
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [list(input()) for _ in range(N)]

    for i in range(N):
            for j in range(N):
                if matrix[i][j] == 'X':
                        start = [i, j]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = []

    Q = int(input())

    for _ in range(Q):
        count, commands = input().split()
        count = int(count)

        flag = 0
        cur_dir = 0
        cur_x, cur_y = start[0], start[1]

        for cmd in commands:
            
            if cmd == 'R':
                cur_dir = (cur_dir + 1) % 4

            elif cmd == 'L':
                cur_dir = (cur_dir - 1) % 4

            elif cmd == 'A':
                nx = cur_x + dx[cur_dir]
                ny = cur_y + dy[cur_dir]

                if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 'T':
                    cur_x, cur_y = nx, ny
                    
        if matrix[cur_x][cur_y] == 'Y':
            flag = 1

        result.append(str(flag))
                    
    print(f"#{tc} {' '.join(result)}")
                    


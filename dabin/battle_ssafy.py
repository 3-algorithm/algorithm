T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

direction = {'U' : 0, 'D': 1, 'L': 2, 'R': 3}
tank_shape = ['^', 'v', '<', '>']

for tc in range(1, T+1):
    H, W = map(int, input().split())

    matrix = [list(input()) for _ in range(H)]

    x, y, d = -1, -1, -1

    for i in range(H):
        for j in range(W):
            if matrix[i][j] in tank_shape:
                x, y = i, j
                for idx in range(4):
                    if matrix[i][j] == tank_shape[idx]:
                        d = idx
                        break
                matrix[i][j] = '.'
                break
        if x != -1:
            break

    N = int(input())
    commands = input()

    for cmd in commands:
        if cmd == 'S':
            cur_x, cur_y = x + dx[d], y + dy[d]

            while 0 <= cur_x < H and 0 <= y < W:
                if matrix[cur_x][cur_y] == '*':
                    matrix[cur_x][cur_y] = '.'
                    break
                elif matrix[cur_x][cur_y] == '#':
                    break

                cur_x += dx[d]
                cur_y += dy[d]

        else:
            d = direction[cmd]
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < H and 0 <= ny < W:
                if matrix[nx][ny] == '.':
                    x, y = nx, ny

    matrix[x][y] = tank_shape[d]

    print(f"#{tc}", end = " ")
    for row in matrix:
        print("".join(row))

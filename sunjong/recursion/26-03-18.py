# https://www.acmicpc.net/problem/2448
# 혼자 못 품

n = int(input())

board = [[' '] * (n * 2) for _ in range(n)]


def recur(n, l, r):
    if n == 3:
        board[l][r] = '*'
        board[l + 1][r - 1] = '*'
        board[l + 1][r + 1] = '*'
        board[l + 2][r - 2] = '*'
        board[l + 2][r - 1] = '*'
        board[l + 2][r] = '*'
        board[l + 2][r + 1] = '*'
        board[l + 2][r + 2] = '*'
        return
    next_n = n // 2
    recur(next_n, l, r)
    recur(next_n, l + next_n, r - next_n)
    recur(next_n, l + next_n, r + next_n)


recur(n, 0, n - 1)

for row in board:
    print(''.join(row))

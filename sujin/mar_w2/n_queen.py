
def check(row):
    for prev_row in range(row):
        # 세로 체크
        if visited[row] == visited[prev_row]:
            return False

       # 대각선 체크
        if abs(row - prev_row) == abs(visited[row] - visited[prev_row]):
            return False

    return True


def recur(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        visited[row] = col  # 현재 row 의 col 에 놓았다 라고 가정하고
        if not check(row):  # 세로와 대각선을 체크해준다.
            continue

        recur(row + 1)

N = int(input())
visited = [0] * N
cnt = 0

recur(0)
print(cnt)

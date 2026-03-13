
n = int(input())

# 상태를 저장할 배열들
col = [False] * n
dr = [False] * (2 * n)  # i + row
dl = [False] * (2 * n)  # i - row + n

cnt = 0

def queen(row):
    global cnt
    if row == n:
        cnt += 1
        return

    for i in range(n):
        # 대각선 및 열 충돌 확인
        if not (col[i] or dr[i + row] or dl[i - row + n]):
            # 퀸 배치
            col[i] = dr[i + row] = dl[i - row + n] = True
            
            queen(row + 1)
            
            # 백트래킹 (상태 복구)
            col[i] = dr[i + row] = dl[i - row + n] = False

queen(0)
print(cnt)

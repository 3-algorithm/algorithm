import sys

# 입력 속도 향상을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    q = []
    # CCTV 위치와 종류 저장
    for i in range(n):
        for j in range(m):
            if 1 <= board[i][j] <= 5:
                q.append((i, j, board[i][j]))
                
    # 0: 상, 1: 우, 2: 하, 3: 좌 (시계 방향)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # 1~5번 CCTV의 회전 가능한 경우의 수
    spin_cnt = [0, 4, 2, 4, 4, 1]
    
    # 파이썬에서는 전역 변수 대신 리스트에 담아 참조하는 방식이 편합니다.
    min_m = [float('inf')]

    def watch(x, y, d, current_board):
        d %= 4  # 방향이 0~3을 순환하도록
        nx, ny = x + dx[d], y + dy[d]
        
        while 0 <= nx < n and 0 <= ny < m:
            if current_board[nx][ny] == 6:  # 벽을 만나면 중단
                break
            if current_board[nx][ny] == 0:  # 빈 칸이면 감시 영역(-1)으로 표시
                current_board[nx][ny] = -1
            nx += dx[d]
            ny += dy[d]

    def back(idx, current_board):
        # 기저 조건: 모든 CCTV를 다 확인한 경우
        if idx == len(q):
            blind_spot_count = sum(row.count(0) for row in current_board)
            min_m[0] = min(min_m[0], blind_spot_count)
            return

        x, y, cctv_type = q[idx]

        # 해당 CCTV 타입이 가질 수 있는 모든 방향 회전
        for d in range(spin_cnt[cctv_type]):
            # 1. 현재 맵 상태 복사 (파이썬의 리스트 컴프리헨션 활용)
            next_board = [row[:] for row in current_board]

            # 2. CCTV 타입에 맞춰 감시 영역 칠하기
            if cctv_type == 1:
                watch(x, y, d, next_board)
            elif cctv_type == 2:
                watch(x, y, d, next_board)
                watch(x, y, d + 2, next_board)
            elif cctv_type == 3:
                watch(x, y, d, next_board)
                watch(x, y, d + 1, next_board)
            elif cctv_type == 4:
                watch(x, y, d, next_board)
                watch(x, y, d + 1, next_board)
                watch(x, y, d + 2, next_board)
            elif cctv_type == 5:
                watch(x, y, 0, next_board)
                watch(x, y, 1, next_board)
                watch(x, y, 2, next_board)
                watch(x, y, 3, next_board)

            # 3. 다음 CCTV 탐색 진행 (재귀)
            back(idx + 1, next_board)

    # 0번째 CCTV부터 탐색 시작
    back(0, board)
    print(min_m[0])

if __name__ == "__main__":
    solve()
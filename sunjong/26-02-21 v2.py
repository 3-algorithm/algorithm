import sys

# 입력 속도 최적화
input = sys.stdin.readline

# 0: 상, 1: 우, 2: 하, 3: 좌 (시계 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve():
    n, m = map(int, input().split())
    
    arr = []
    q = [] # CCTV 정보 담을 리스트
    no_cnt = 0 # 벽과 CCTV의 총 개수
    
    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
        for j in range(m):
            # CCTV(1~5)인 경우 리스트에 추가
            if 1 <= row[j] <= 5:
                q.append((i, j, row[j]))
                no_cnt += 1
            # 벽인 경우
            elif row[j] == 6:
                no_cnt += 1

    # 특정 방향으로 감시하며 새로 감시된 칸의 수를 반환하는 함수
    def watch(x, y, mx, my, visit):
        cnt = 0
        zx, zy = x + mx, y + my
        while True:
            # 범위를 벗어나거나 벽(6)을 만나면 종료
            if zx < 0 or zx >= n or zy < 0 or zy >= m or arr[zx][zy] == 6:
                return cnt
            # 아직 방문하지 않은 빈 칸(0)이라면 카운트 증가
            if visit[zx][zy] == 0 and arr[zx][zy] == 0:
                cnt += 1
            visit[zx][zy] = 1 # 방문 처리
            zx += mx
            zy += my

    max_cnt = 0
    # 경우의 수 세팅 -> 4진수로 바꾸기 (4의 CCTV 개수 제곱)
    sq = 4 ** len(q)

    # 0부터 sq-1까지 모든 경우의 수 탐색
    for i in range(sq):
        temp = i
        cnt = 0
        visit = [[0] * m for _ in range(n)]
        
        # 각 CCTV마다 방향 할당
        for idx in range(len(q)):
            head = temp % 4 # 4로 나눈 나머지로 방향 결정 (0~3)
            temp //= 4      # 💡 수정된 부분: 다음 자릿수를 위해 4로 나눔 (파이썬은 몫 구하기 // 사용)
            
            cx, cy, c_type = q[idx]
            
            if c_type == 1:
                cnt += watch(cx, cy, dx[head], dy[head], visit)
            elif c_type == 2:
                cnt += watch(cx, cy, dx[(head + 1) % 4], dy[(head + 1) % 4], visit)
                cnt += watch(cx, cy, dx[(head + 3) % 4], dy[(head + 3) % 4], visit)
            elif c_type == 3:
                cnt += watch(cx, cy, dx[(head + 1) % 4], dy[(head + 1) % 4], visit)
                cnt += watch(cx, cy, dx[(head + 2) % 4], dy[(head + 2) % 4], visit)
            elif c_type == 4:
                cnt += watch(cx, cy, dx[(head + 1) % 4], dy[(head + 1) % 4], visit)
                cnt += watch(cx, cy, dx[(head + 2) % 4], dy[(head + 2) % 4], visit)
                cnt += watch(cx, cy, dx[(head + 3) % 4], dy[(head + 3) % 4], visit)
            elif c_type == 5:
                cnt += watch(cx, cy, dx[(head + 1) % 4], dy[(head + 1) % 4], visit)
                cnt += watch(cx, cy, dx[(head + 2) % 4], dy[(head + 2) % 4], visit)
                cnt += watch(cx, cy, dx[(head + 3) % 4], dy[(head + 3) % 4], visit)
                cnt += watch(cx, cy, dx[(head + 4) % 4], dy[(head + 4) % 4], visit)
                
        max_cnt = max(max_cnt, cnt)

    # 전체 칸 수 - (벽과 CCTV 개수) - (최대 감시 가능 구역) = 최소 사각지대
    print((n * m) - no_cnt - max_cnt)

if __name__ == '__main__':
    solve()
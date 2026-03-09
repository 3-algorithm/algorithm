import sys
from collections import deque

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    n = int(input())
    board = []
    max_height = 0
    
    for _ in range(n):
        row = list(map(int, input().split()))
        board.append(row)
        # 맵에서 가장 높은 지점 찾기
        max_height = max(max_height, max(row))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 아무 지역도 잠기지 않을 수 있으므로 초기 최댓값은 1 (전체가 하나의 영역)
    max_cnt = 1
    
    # 높이 1부터 max_height까지 시뮬레이션
    # 주의: 높이가 0일 때(비가 안 올 때)부터 비교할 수도 있지만 보통 1부터 시작해도 무방합니다.
    for height in range(1, max_height + 1):
        is_visited = [[False] * n for _ in range(n)]
        cnt = 0
        
        for i in range(n):
            for j in range(n):
                # 물에 잠기지 않고(height 이상), 방문한 적 없는 경우 BFS 시작
                if board[i][j] > height and not is_visited[i][j]:
                    cnt += 1
                    q = deque([(i, j)])
                    is_visited[i][j] = True
                    
                    while q:
                        x, y = q.popleft()
                        for z in range(4):
                            nx, ny = x + dx[z], y + dy[z]
                            
                            if 0 <= nx < n and 0 <= ny < m: # m은 n과 같으므로 n 사용
                                if not is_visited[nx][ny] and board[nx][ny] > height:
                                    is_visited[nx][ny] = True
                                    q.append((nx, ny))
                                    
        max_cnt = max(max_cnt, cnt)

    print(max_cnt)

# n x n 맵이므로 nx < n, ny < n으로 수정해서 실행하세요.
if __name__ == "__main__":
    # 작성하신 자바 코드의 로직(nx, ny 범위 체크)에 맞게 n으로 통일합니다.
    solve()
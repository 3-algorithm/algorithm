import sys
from collections import deque

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

def solve():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    ans = 0

    # 4방향 이동 함수
    def move(direction, cur_board):
        new_board = [[0] * n for _ in range(n)]
        
        # 상(0), 하(1), 좌(2), 우(3)
        if direction == 0:  # 상 (자바 코드의 else 블록 로직)
            for j in range(n):
                q = deque()
                for i in range(n):
                    if cur_board[i][j] != 0:
                        q.append(cur_board[i][j])
                
                idx = 0
                while q:
                    num = q.popleft()
                    if q and q[0] == num:
                        new_board[idx][j] = num * 2
                        q.popleft()
                    else:
                        new_board[idx][j] = num
                    idx += 1
                    
        elif direction == 1:  # 하 (자바 코드의 head == 2 로직)
            for j in range(n):
                q = deque()
                for i in range(n - 1, -1, -1):
                    if cur_board[i][j] != 0:
                        q.append(cur_board[i][j])
                
                idx = n - 1
                while q:
                    num = q.popleft()
                    if q and q[0] == num:
                        new_board[idx][j] = num * 2
                        q.popleft()
                    else:
                        new_board[idx][j] = num
                    idx -= 1

        elif direction == 2:  # 좌 (자바 코드의 head == 3 로직)
            for i in range(n):
                q = deque()
                for j in range(n):
                    if cur_board[i][j] != 0:
                        q.append(cur_board[i][j])
                
                idx = 0
                while q:
                    num = q.popleft()
                    if q and q[0] == num:
                        new_board[i][idx] = num * 2
                        q.popleft()
                    else:
                        new_board[i][idx] = num
                    idx += 1

        elif direction == 3:  # 우 (자바 코드의 head == 1 로직)
            for i in range(n):
                q = deque()
                for j in range(n - 1, -1, -1):
                    if cur_board[i][j] != 0:
                        q.append(cur_board[i][j])
                
                idx = n - 1
                while q:
                    num = q.popleft()
                    if q and q[0] == num:
                        new_board[i][idx] = num * 2
                        q.popleft()
                    else:
                        new_board[i][idx] = num
                    idx -= 1
                    
        return new_board

    # 4^5 (1024)가지 모든 방향 조합 탐색
    for i in range(1024):
        temp_board = [row[:] for row in board]  # 깊은 복사
        case = i
        for _ in range(5):
            head = case % 4
            case //= 4
            temp_board = move(head, temp_board)
        
        # 최댓값 갱신
        for row in temp_board:
            ans = max(ans, max(row))
            
    print(ans)

solve()

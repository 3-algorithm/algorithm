import sys
from collections import deque
from itertools import permutations, product

# 방향 벡터 (상, 하, 좌, 우, 앞, 뒤)
dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

def rotate(matrix):
    """시계 방향으로 90도 회전"""
    new_matrix = [[0]*5 for _ in range(5)]
    for r in range(5):
        for c in range(5):
            new_matrix[c][4-r] = matrix[r][c]
    return new_matrix

def bfs(maze):
    """3차원 공간에서 최단 경로 찾기"""
    # 입구나 출구가 벽(0)이면 바로 종료
    if maze[0][0][0] == 0 or maze[4][4][4] == 0:
        return float('inf')
    
    q = deque([(0, 0, 0, 0)]) # (z, x, y, dist)
    visited = [[[False]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True
    
    while q:
        z, x, y, d = q.popleft()
        
        if z == 4 and x == 4 and y == 4:
            return d
        
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            
            if 0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5:
                if not visited[nz][nx][ny] and maze[nz][nx][ny] == 1:
                    visited[nz][nx][ny] = True
                    q.append((nz, nx, ny, d + 1))
                    
    return float('inf')

def solve():
    # 데이터 입력
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    # 3차원 배열 생성 (5층, 5행, 5열)
    boards = []
    idx = 0
    for _ in range(5):
        board = []
        for _ in range(5):
            board.append(list(map(int, input_data[idx:idx+5])))
            idx += 5
        boards.append(board)

    # 각 판의 4가지 회전 상태를 미리 만들어 둠
    all_rotations = []
    for b in boards:
        rotations = [b]
        for _ in range(3):
            rotations.append(rotate(rotations[-1]))
        all_rotations.append(rotations)

    min_dist = float('inf')

    # 1. 판을 쌓는 순서 결정 (순열: 5! = 120)
    for p in permutations(range(5)):
        # 2. 각 판의 회전 상태 결정 (중복순열: 4^5 = 1024)
        for rot_indices in product(range(4), repeat=5):
            # 현재 조합으로 미로 생성
            maze = [all_rotations[p[i]][rot_indices[i]] for i in range(5)]
            
            dist = bfs(maze)
            if dist < min_dist:
                min_dist = dist
            
            # 이론상 최단거리 12(칸수 기준 13)가 나오면 즉시 종료
            if min_dist == 12:
                print(12)
                return

    if min_dist == float('inf'):
        print(-1)
    else:
        print(min_dist)

if __name__ == "__main__":
    solve()
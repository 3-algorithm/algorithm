import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.read() 사용
    input = sys.stdin.read().split()
    if not input:
        return
    
    idx = 0
    n = int(input[idx]); idx += 1
    m = int(input[idx]); idx += 1
    k = int(input[idx]); idx += 1
    
    notebook = [[0] * m for _ in range(n)]
    
    def rotate(sticker, r, c):
        """스티커를 시계방향으로 90도 회전"""
        new_sticker = [[0] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                new_sticker[j][r - 1 - i] = sticker[i][j]
        return new_sticker, c, r

    def can_attach(sticker, r, c, x, y):
        """(x, y) 위치에 스티커를 붙일 수 있는지 확인"""
        for i in range(r):
            for j in range(c):
                if sticker[i][j] == 1 and notebook[x + i][y + j] == 1:
                    return False
        return True

    def attach(sticker, r, c, x, y):
        """스티커를 실제로 노트북에 붙임"""
        count = 0
        for i in range(r):
            for j in range(c):
                if sticker[i][j] == 1:
                    notebook[x + i][y + j] = 1
                    count += 1
        return count

    total_max = 0

    for _ in range(k):
        sn = int(input[idx]); idx += 1
        sm = int(input[idx]); idx += 1
        sticker = []
        for _ in range(sn):
            row = []
            for _ in range(sm):
                row.append(int(input[idx]))
                idx += 1
            sticker.append(row)
        
        # 4번의 회전 방향에 대해 시도 (0, 90, 180, 270)
        attached = False
        curr_sticker, r, c = sticker, sn, sm
        
        for _ in range(4):
            if attached: break
            
            # 노트북의 모든 좌표를 돌며 확인
            for i in range(n - r + 1):
                if attached: break
                for j in range(m - c + 1):
                    if can_attach(curr_sticker, r, c, i, j):
                        total_max += attach(curr_sticker, r, c, i, j)
                        attached = True
                        break
            
            if not attached:
                curr_sticker, r, c = rotate(curr_sticker, r, c)

    print(total_max)

if __name__ == "__main__":
    solve()
import sys
from collections import deque

# 입출력 속도를 높이기 위해 sys.stdin.readline 사용
input = sys.stdin.read

def solve():
    # 모든 입력을 한꺼번에 읽어와서 처리 (속도 향상)
    data = input().split()
    if not data:
        return

    n = int(data[0])
    dq = deque()
    
    # 명령어 처리를 위한 인덱스
    idx = 1
    results = []

    for _ in range(n):
        cmd = data[idx]
        idx += 1
        
        if cmd == "push_front":
            num = data[idx]
            idx += 1
            dq.appendleft(num)
        
        elif cmd == "push_back":
            num = data[idx]
            idx += 1
            dq.append(num)
            
        elif cmd == "pop_front":
            results.append(dq.popleft() if dq else "-1")
            
        elif cmd == "pop_back":
            results.append(dq.pop() if dq else "-1")
            
        elif cmd == "size":
            results.append(str(len(dq)))
            
        elif cmd == "empty":
            results.append("0" if dq else "1")
            
        elif cmd == "front":
            results.append(dq[0] if dq else "-1")
            
        elif cmd == "back":
            results.append(dq[-1] if dq else "-1")

    # 결과들을 한 번에 출력 (BufferedWriter와 비슷한 역할)
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

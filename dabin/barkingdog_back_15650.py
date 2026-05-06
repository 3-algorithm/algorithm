def recur(cnt, prev):

    if cnt == M+1:
        print(*path)
        return
    # 이전에 선택했던 것 다음 것부터 탐색
    for i in range(prev+1, N+1):
        
        path.append(i)
        recur(cnt+1, i)
        path.pop()

N, M = map(int, input().split())

path = []

recur(1, 0)

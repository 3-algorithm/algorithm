def recur(cnt, prev):
    if cnt == M+1:
        print(*path)
        return
    
    for i in range(prev, N+1):
        path.append(i)
        recur(cnt + 1, i)
        path.pop()

N, M = map(int, input().split())

path = []


recur(1, 1)
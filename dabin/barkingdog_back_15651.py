def recur(cnt):
    if cnt == M+1:
        print(*path)
        return 
    for i in range(1, N+1):
        path.append(i)
        recur(cnt + 1)
        path.pop()

N, M = map(int, input().split())

path = []

recur(1)
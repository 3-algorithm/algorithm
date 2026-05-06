def recur(cnt):
    global N, M

    if cnt == M+1:
        print(*path)
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue

        visited[i] = 1
        path.append(i)
        recur(cnt+1)
        path.pop()
        visited[i] = 0

N, M = map(int, input().split())

path = []
visited = [0] * (N+1) 

recur(1)
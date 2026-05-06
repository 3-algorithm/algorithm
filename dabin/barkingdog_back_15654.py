def recur(cnt):
    if cnt == M:
        print(*path)
        return
    
    for i in range(N):
        if visited[i]:
            continue
        
        visited[i] = 1
        path.append(arr[i])
        recur(cnt + 1)
        path.pop()
        visited[i] = 0
        
        
    
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

path = []
visited = [0] * (N+1)

recur(0)
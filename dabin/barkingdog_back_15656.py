def recur(cnt):
    if cnt == M:
        print(*path)
        return
    
    for i in range(N):
        path.append(arr[i])
        recur(cnt + 1)
        path.pop()
    
N, M = map(int, input().split())

arr =  list(map(int, input().split()))
path = []

arr.sort()

recur(0)
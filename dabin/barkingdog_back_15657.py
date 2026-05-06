def recur(cnt, prev):
    if cnt == M:
        print(*path)
        return
    
    for i in range(prev, N):
        path.append(arr[i])
        recur(cnt + 1, i)
        path.pop()

N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

path = []

recur(0, 0)
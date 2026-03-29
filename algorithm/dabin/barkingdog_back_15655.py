def recur(cnt, prev):
    global numbers

    if cnt == M:
        print(*path)
        return
    
    for i in range(prev+1, N):
        
        path.append(numbers[i])
        recur(cnt + 1, i)
        path.pop()
        
        
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

path = []

recur(0, -1)
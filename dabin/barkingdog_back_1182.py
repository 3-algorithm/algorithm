def recur(cur_sum, prev):
    global result
    
    if cur_sum == S:
        result += 1

    for i in range(prev, N):
       
        recur(cur_sum + arr[i], i + 1)
        
    

N, S = map(int, input().split())

arr = list(map(int, input().split()))

result = 0

recur(0, 0)

if S == 0:
    print(result - 1)
else:
    print(result)
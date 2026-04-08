import sys
sys.stdin = open("input_subset.txt")

def subset(cnt, prev):

    global result
    
    if cnt == N:
        if sum(path) == M:
            result += 1
        return 
        
    for i in range(prev, 12):
        
        path.append(A[i])
        subset(cnt + 1, i+1)
        path.pop()
        
        

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    path = []
    result = 0

    subset(0, 0)
    print(f"#{tc} {result}")
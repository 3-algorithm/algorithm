import sys
sys.stdin = open("input_rangesum.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    range_sum = []
  
    for i in range(N-M+1):
        hap = 0
        for j in range(M):
            hap += arr[i+j]
        range_sum.append(hap)
        

    max_sum = max(range_sum)
    min_sum = min(range_sum)
    result = max_sum - min_sum
    
    print(f"#{tc} {result}")
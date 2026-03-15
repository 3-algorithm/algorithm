import sys
sys.stdin = open("input_minmax.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    min_num = max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
        
        if arr[i] < min_num:
            min_num = arr[i]
            
    result = max_num - min_num
    print(f"#{tc} {result}")
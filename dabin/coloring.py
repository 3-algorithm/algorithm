import sys
sys.stdin = open("input_coloring.txt")

T = int(input())

for tc in range(1, T+1):
    arr = []
    N = int(input())
    matrix = [[0] * 10 for _ in range(10)]
    cnt = 0
    
    for i in range(N):
        arr.append(list(map(int,input().split())))
        
    for item in arr:
        for j in range(item[0], item[2]+1):
            for k in range(item[1], item[3]+1):
                if matrix[j][k] == 0:
                    matrix[j][k] = item[4]
                elif matrix[j][k] != item[4] and matrix[j][k] != 3:
                    matrix[j][k] = 3
                    cnt += 1
                    
                
    print(f"#{tc} {cnt}")


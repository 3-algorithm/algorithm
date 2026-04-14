import sys
sys.stdin = open("input_rect.txt")

matrix = [[0] * 100 for _ in range(100)]

arr = []
for i in range(4):
    arr.append(list(map(int, input().split())))
    
for item in arr:
    for i in range(item[0], item[2]):
        for j in range(item[1], item[3]):
            matrix[i][j] = 1
cnt = 0     
for i in range(100):
    for j in range(100):
        if matrix[i][j] == 1:
            cnt += 1

print(cnt)
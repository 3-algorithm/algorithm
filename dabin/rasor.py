N = int(input())

arr = list(map(int, input().split()))
result = [0] * N
cnt = 0

i = N-1
j = 1
while i-j >= 0:
    if arr[i] < arr[i-j]:
        result[i] = i-j+1
        i -= 1
        j = 1
    else:
        j += 1

print(*result)

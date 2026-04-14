import sys

# 빠른 입력을 위해 sys.stdin.read 사용
input_data = sys.stdin.read().split()
    
n = int(input_data[0])
arr = list(map(int, input_data[1:]))

# a[i]: i번째 원소를 끝으로 하는 가장 긴 증가하는 부분 수열의 길이
# b[i]: i번째 원소를 시작으로 하는 가장 긴 감소하는 부분 수열의 길이
a = [1] * n
b = [1] * n

# LIS (왼쪽 -> 오른쪽)
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            a[i] = max(a[i], a[j] + 1)

# LDS (오른쪽 -> 왼쪽)
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            b[i] = max(b[i], b[j] + 1)

# 결과 계산: 각 위치에서 (증가 길이 + 감소 길이 - 1) 중 최댓값
# (i번째 원소가 중복 계산되므로 1을 빼줍니다)
result = 0
for i in range(n):
    result = max(result, a[i] + b[i] - 1)

print(result)
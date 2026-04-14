import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# dp[i]: arr[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 처음에는 모두 자기 자신만 포함하므로 1로 초기화
dp = [1] * N 

for i in range(N):
    for j in range(i):
        # 현재 원소(arr[i])가 이전 원소(arr[j])보다 크다면
        if arr[i] > arr[j]:
            # 이전 원소의 수열 길이에 1을 더한 값과 현재 길이를 비교하여 최댓값 갱신
            dp[i] = max(dp[i], dp[j] + 1)

# dp 배열에 저장된 값 중 가장 큰 값이 전체 수열의 LIS 길이
print(max(dp))

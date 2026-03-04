# 수열
# https://www.acmicpc.net/problem/2559

N, K = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]*(N+1)

answer = (N+1) * -100

# 누적 합 구하기
for i in range(1, N+1):
  prefix_sum[i] += prefix_sum[i-1]+arr[i-1]

# K 구간 합 구하기
for i in range(1, N-K+2):
  temp_sum = prefix_sum[i+K-1] - prefix_sum[i-1]

  # 최댓값 구하기
  if temp_sum > answer:
    answer = temp_sum

print(answer)
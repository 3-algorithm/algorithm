import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

arr.sort()

sum=0
for i in range(N):
    for j in range(i+1):
        sum+=arr[j]

print(sum)



# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()

# total_time = 0  # 총 필요한 시간의 합
# current_sum = 0 # 현재 사람까지 걸린 누적 시간

# for time in arr:
#     current_sum += time          # 앞사람들 시간 + 내 시간
#     total_time += current_sum    # 총합에 누적

# print(total_time)



# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()

# # arr[i]는 (N - i)번 더해지게 됨
# total_time = sum(arr[i] * (N - i) for i in range(N))

# print(total_time)
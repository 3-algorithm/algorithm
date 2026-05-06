# 바킹독 - 정렬 - 역원소 정렬
# https://www.acmicpc.net/problem/5648
import sys

arr = sys.stdin.read().split()


n= int(arr[0])
nums = arr[1:1+n]
result = []

for num in nums:
    num = int(num[::-1])
    result.append(num)

result.sort()

print('\n'.join(map(str, result)))

    

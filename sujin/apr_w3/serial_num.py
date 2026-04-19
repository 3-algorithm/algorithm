# 바킹독 - 정렬 - 시리얼 번호
# http://acmicpc.net/problem/1431
import sys
from collections import deque

n = int(input())
arr = sys.stdin.read().split()
numbers ='0123456789'

def temp_sum(num):
    temp = 0
    for i in num:
        if i in numbers:
            temp += int(i)
    return temp
    
arr.sort(key=lambda x: (len(x), temp_sum(x), x))

print('\n'.join(arr))
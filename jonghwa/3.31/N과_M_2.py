from itertools import combinations
import sys

input=sys.stdin.readline

N,M=map(int,input().split())

arr= [x for x in range(1,N+1)]

for i in combinations(arr, M):
    print(*i)

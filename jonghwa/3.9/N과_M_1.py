from itertools import permutations
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

for p in permutations(range(1,N+1),M):
    print(*p)


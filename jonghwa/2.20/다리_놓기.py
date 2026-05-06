import math

T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    print(math.comb(M,N))

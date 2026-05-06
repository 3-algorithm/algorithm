import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())

arr=list(map(int,input().split()))

q=deque(range(1,N+1))

cnt=0

for a in arr:
    idx=q.index(a)
    if idx <= len(q)//2:
        q.rotate(-idx)
        cnt += idx
    else:
        moves=len(q) - idx 
        q.rotate(moves)
        cnt += moves

    q.popleft()
print(cnt)

        

import sys
input = sys.stdin.readline

N,K=map(int,input().split())

list1=[]
for _ in range(N):
    list1.append(int(input()))

cnt=0
for a in reversed(list1):
    if K==0:
        break

    if K>=a:
        cnt+=K//a
        K%=a

print(cnt)

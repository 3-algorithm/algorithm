N=int(input())
arr=[]
cnt=[0]*10001
for _ in range(N):
    a=int(input())
    cnt[a]+=1
for i in range(10001):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
#나무의수 N
#가져가려는 나무길이 M

arr=sorted(list(map(int,input().split())))

start = 0
end = arr[-1]
answer = 0

while start<=end:
    mid=(start+end)//2
    sum=0
    for i in range(N):
        if arr[i]>mid:
            sum+=(arr[i]-mid)

    if sum>=M:
        answer = mid
        start=mid+1#더 높여야함
    elif sum<M:
        end = mid-1
        #초과했으므로 닞춰야함
print(answer)

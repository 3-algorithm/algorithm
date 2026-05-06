N=int(input())
arr=[]
for _ in range(N):
    a=int(input())
    if a==0:
        arr.pop()
    else:
        arr.append(a)

print(sum(arr))
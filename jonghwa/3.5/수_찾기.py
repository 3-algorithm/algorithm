n=int(input())
set=set(map(int,input().split()))

m=int(input())
list=list(map(int,input().split()))

for i in list:
    if i in set:
        print(1)
    else:
        print(0)
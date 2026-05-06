N=int(input())
arr=[]
for _ in range(N):
    a=input().split()
    if a[0] =="push":
        arr.append(a[1])
    elif a[0]=="pop":
        if len(arr)==0:
            print(-1)
        else:
            print(arr.pop())
    elif a[0]=="size":
        print(len(arr))
    elif a[0]=="empty":
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif a[0]=="top":
        if len(arr)==0:
            print(-1)
        else:
            print(arr[len(arr)-1])
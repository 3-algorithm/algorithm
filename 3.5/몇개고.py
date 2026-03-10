n,m=map(int,input().split())
if 12<=n and 16>=n and m==0:
    print(320)
elif n<=11 or n>=17 or m==1:
    print(280)
T=int(input())
for tc in range(1,T+1):
    x1,y1,x2,y2 = map(int,input().split())
    n=int(input())
    cnt=0
    for i in range(n):
        cx,cy,r = map(int,input().split())
        if ((x1-cx)**2 +(y1-cy)**2) < r**2 and not ((x2-cx)**2 +(y2-cy)**2) < r**2:
            cnt+=1
        if ((x2-cx)**2 +(y2-cy)**2) < r**2 and not ((x1-cx)**2 +(y1-cy)**2) < r**2:
            cnt+=1
    print (cnt)
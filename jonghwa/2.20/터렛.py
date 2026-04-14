import math

T = int(input())
for tc in range(1,T+1):
    # 조규환 / 백승환 vs 류재명
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    D=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if D==0 and r1==r2:
        print(-1)
    elif D>r1+r2 : 
        print(0)
    elif D<abs(r1-r2):
        print(0)
    elif D==r1+r2:
        print(1)
    elif D==abs(r1-r2):
        print(1)
    elif D<r1+r2 and D>abs(r1-r2):
        print(2)


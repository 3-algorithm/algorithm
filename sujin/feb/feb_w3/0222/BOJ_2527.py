# 직사각형
# https://www.acmicpc.net/problem/2527


# a: 직사각형이 겹침 면적으로
# b: 선으로 겹침
# c: 꼭짓점만 겹침
# d: 안겹침
for i in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    # d: 안겹침
    if p1 < x2 or p2 < x1 or y1>q2 or q1<y2:
        print('d')
        # c:
    elif (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2) or (x1 == p2 and q1 == y2) or (x1 == p2 and y1 == q2):
        print('c')
        #b:
    elif p1 == x2 or x1 == p2 or q1 == y2 or y1 == q2:
        print('b')

    # a:
    else:
        print('a')


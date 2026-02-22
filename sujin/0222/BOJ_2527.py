# 직사각형
# https://www.acmicpc.net/problem/2527


# a: 직사각형이 겹침 면적으로
# b: 선으로 겹침
# c: 꼭짓점만 겹침
# d: 안겹침
final = [['d', 'd', 'd'], ['d', 'c', 'b'], ['d', 'b', 'a']]
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if x2 < x3 or x4<x1:
        x_intersection = 0
    elif x2 == x3 or x4 == x1:
        x_intersection = 1
    else:
        x_intersection = 2

    if y2 < y3 or y4<y1:
        y_intersection = 0
    elif y2 == y3 or y4 == y1:
        y_intersection = 1
    else:
        y_intersection = 2

    print(final[x_intersection][y_intersection])

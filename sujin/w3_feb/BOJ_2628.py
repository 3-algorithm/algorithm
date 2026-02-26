# 문제: 백준 2628 종이자르기
# https://www.acmicpc.net/problem/2628

x, y = map(int, input().split())
height = [0]
width = [0]
height.append(y)
width.append(x)

N = int(input())
#가로/ 세로 변에서 각각 나눠지는 포인트를 저장함
for _ in range(N):
    i, j = map(int, input().split())
    if i == 0:
        height.append(j)
    else:
        width. append(j)

# ascneding 오더로 정리
height.sort()
width.sort()
# 각각 잘라지는 포인트들의 거리를 구함
# 가로 거리, 세로 거리를 곱해서 넓이를 구함
# 넓이 중 최대값을 구함
max_area = 0
for a in range(len(height)-1):
    h_diff = height[a+1] - height[a]
    for b in range(len(width)-1):
        w_diff = width[b+1] - width[b]
        if max_area < w_diff * h_diff:
            max_area = w_diff * h_diff

print(max_area)
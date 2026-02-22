# 문제: 백준 2628 종이 자르기
# https://www.acmicpc.net/problem/2628

# 인풋 받기
width, height = map(int, input().split())
num_cuts = int(input()) # 칼로 잘라야 하는 개수


for _ in range(num_cuts):
    lst = list(map(int, input().split()))

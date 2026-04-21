# https://www.acmicpc.net/problem/10814

import sys

# 입력 속도 향상을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 1. 회원 수 입력 받기
n = int(input())

arr = []
for _ in range(n):
    # 2. 나이와 이름을 문자열로 분리해서 받음
    age, name = input().split()
    # 나이는 숫자로 비교해야 하므로 int형으로 변환하여 리스트에 추가
    arr.append([int(age), name])

# 3. 나이(x[0])를 기준으로만 정렬. 
# 파이썬의 sort는 안정 정렬(Stable sort)이므로 나이가 같으면 입력된 순서가 유지됨.
arr.sort(key=lambda x: x[0])

# 결과 출력
for i in arr:
    print(*i)

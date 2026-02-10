import sys
sys.stdin = open("sequence_in.txt", "r")

# for each test
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
# 리스트 A와 B를 만들음
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
# 부분수열을 표시할 변수 지정
    temp = 0
# 리스트 B를 돌면서,
# B의 각 숫자가 리스트 A에 순서대로 있는지 확인
# => B[i]를 A[j]에서 찾으면
# temp에 표시하고 A[j-1] 다 지움

    for i in range(len(B)):
        if B[i] in A:
            temp += 1
            A_idx = A.index(B[i])
            A = A[A_idx+1:]

# temp = len(B)랑 같으면, B는 A의 부분수열로 들어가 있는 거 => YES 출력
    if temp == len(B):
        print(f'#{test_case+1} YES')
    else:
        print(f'#{test_case+1} NO')


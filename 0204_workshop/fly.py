import sys
sys.stdin = open('fly_input.txt')

T = int(input())
# for each test
# N, M 인풋을 받음
# 아래 숫자들을 한 리스트로 받음
for test_case in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

# sum 임시변수 설정
    max_sum = 0
# matrix를 돌면서, M x M 상자만큼씩 합을 구함
    for n in range(0, N-M+1):
        for m in range(0, N-M+1):
            temp = []
            for i in range(n, n+M):
                for j in range(m,m+M):
                    temp.append(matrix[i][j])
            # 각 MxM 상자 안에 있는 숫자를 다 합친게 max_sum보다 크면, max_sum을 대체
            if max_sum < sum(temp):
                max_sum = sum(temp)
    print(f'#{test_case+1} {max_sum}')
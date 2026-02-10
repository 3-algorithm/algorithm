import sys
sys.stdin = open('word_input.txt')

T = int(input())
# for each test
# N, K를 받음
# matrix를 받음
for test_case in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 단어가 들어가는 칸을 카운트
    count = 0
    # 가로줄 중에서 단어K길이에 딱 맞는 빈칸(=1)을 찾음

    for row in matrix:
        


        for i in range(0, N-K):
            temp = row[i:i+K]
            if K == sum(temp) and K == sum(row):
                count += 1
            print(count)

import sys
sys.stdin = open("sum1_input.txt")


# for each test
for test_case in range(10):
    T = int(input())
# 리스트 받아옴
    arr = [list(map(int, input().split())) for _ in range(100)]

# 변수 sum 어싸인
    # 오른쪽 대각선: sum_1, 왼쪽 대각선: sum_2
    sum_1 = 0
    sum_2 = 0
    # 가로 합을 모아놓을 리스트
    sum_3_max = []
    # 세로 합을 모아놓을 리스트
    sum_4_max = []
# 100x100 matrix
# 한줄씩 돌면서, 대각선 합 구함


    for i in range(100):
        # 오른쪽 방향 대각선 합
        sum_1 += arr[i][i]
        # 왼쪽 방향 대각선 합
        sum_2 += arr[i][99-i]
        # 각 row 합
        sum_3 = 0
        # 각 column 합
        sum_4 = 0
    # rows 합 중 맥시멈:
        for j in range(100):

            sum_3 += arr[i][j]
            sum_4 += arr[j][i]
        sum_3_max.append(sum_3)
        sum_4_max.append(sum_4)
    # sum 출력
    print(f'#{T} {max(sum_1, sum_2, max(sum_3_max), max(sum_4_max))}')

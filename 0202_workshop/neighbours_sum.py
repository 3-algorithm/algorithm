import sys
sys.stdin = open("neighbours_sum_input.txt", "r")

# for each test
T = int(input())
for test_case in range(1, T + 1):

    # N, M
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # numbers[0]부터 오른쪽으로 M개 잘라서 더함 => neighbours_sum
    num_0 = numbers[0:M]
    sum_0 = sum(num_0)
    # Assume max_sum, min_sum = neighbours_sum
    max_sum = 0
    min_sum = 0
    # numbers 리스트를 돌면서
    for i in range(0, N-M+1):
        neighbours = numbers[i:i+M]
        sum_neighbours = sum(neighbours)
    # if neighbours_sum > max_sum => replace
        if max_sum < sum_neighbours:
            max_sum = sum_neighbours
    # if neighbours_sum < min_sum => replace
        if min_sum > sum_neighbours:
            min_sum = sum_neighbours
    # 출력 max_sum - min_sum
    print(f'#{test_case} {max_sum - min_sum}')


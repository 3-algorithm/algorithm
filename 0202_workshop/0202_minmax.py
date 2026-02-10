import sys
sys.stdin = open("minmax_input.txt", "r")

# for each test
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # numbers[0]이 가장 크고, 작은 수라고 가정
    max_num = numbers[0]
    min_num = numbers[0]

    # numbers 리스트를 돌면서 아래를 확인
    for num in numbers:
    # num > max_num => replace
        if max_num < num:
            max_num = num
    # num < min_num => replace
        if min_num > num:
            min_num = num
    # 출력 difference = max_num - min_num
    difference = max_num - min_num
    print(f'#{test_case} {difference}')
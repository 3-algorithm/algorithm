import sys
sys.stdin = open("sum_subsets_input.txt")

T = int(input())
A = list(range(0,13))

# for each test
for test_case in range(T):
    N, K = map(int, input().split())

    # N칸을 가진 임시 subset을 만들음
    subset = [0]*N

    # We want: K = sum(subset)
    # A를 돌면서,
    while != sum(subset):
        for i in range(0,13):
            subset[0] = i
    else:
        count
        # subset리스트에 차례대로 숫자를 넣어보자
        #  K = sum(subset) 이게 나오면 count하나씰 올리기

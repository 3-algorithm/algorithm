# 바킹독 - 백트레킹 - 부분수열의 합
# https://www.acmicpc.net/problem/1182

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

# 모든 subset을 만들면서
# 그 썸이  S인지를 확인
def subseq(idx, subset):
    global count
    if idx == N:
        if subset and sum(subset) == S:
            count += 1
        # print(*subset)
        return

    subseq(idx +1, subset + [num_list[idx]])
    subseq(idx+1, subset)

subseq(0, [])
print(count)
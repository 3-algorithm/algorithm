# 바킹독 - 백트래킹- N&M2
# https://www.acmicpc.net/problem/15650

N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

# 중복이 없이 M개 고르기
final = []

def asc_comb(idx, start):
    # depth: M
    if idx == M:
        print(*final)
        return
    for i in range(start, N):

            final.append(arr[i])

            asc_comb(idx+1, i+1)

            final.pop()
asc_comb(0,0)
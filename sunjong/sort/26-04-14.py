# https://www.acmicpc.net/problem/1431

n = int(input())

arr = [input() for _ in range(n)]


def get_sum(x):
    return sum(int(c) for c in x if c.isdigit())


arr.sort(lambda x: (len(x), get_sum(x), x))

for i in arr:
    print(i)
# https://www.acmicpc.net/problem/1181

n = int(input())

arr = set([input() for _ in range(n)])

l = list(arr)

l.sort(lambda x: (len(x), x))

for i in l:
    print(i)
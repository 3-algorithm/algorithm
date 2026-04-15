# https://www.acmicpc.net/problem/11652

n = int(input())

num_dict = dict()

for i in range(n):
    num = int(input())
    num_dict.setdefault(num, 0)
    num_dict[num] = num_dict[num] + 1


max_cnt = 0
num = 0
for k, v in num_dict.items():
    if max_cnt < v:
        max_cnt = v
        num = k
    elif max_cnt == v:
        num = min(num, k)

print(num)

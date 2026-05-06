# https://www.acmicpc.net/problem/1629

a, b, c = map(int, input().split())

# cal_num = 1
# for i in range(b):
#     cal_num = (cal_num % c) * a % c
#
# print(cal_num)

def func(x, y):
    if y <= 1:
        return x % c
    num = func(x, y // 2) % c
    if y % 2 == 1:
        return (num * num * x) % c
    return num * num % c


print(func(a, b))

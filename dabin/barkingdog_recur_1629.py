def multi(a, b, c):

    if b == 1:
        return a % c

    temp = multi(a, b // 2, c)

    if b % 2 == 0:
        return (temp * temp) % C

    else:
        return (temp * temp * a) % C


A, B, C = map(int, input().split())

print(multi(A, B, C))


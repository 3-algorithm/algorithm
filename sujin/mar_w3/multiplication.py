# 바킹독 - 재귀 - 곱셈
# https://www.acmicpc.net/problem/1629

A, B, C = map(int, input().split())

# 모듈러 연산으로 풀어야 시간초과 안뜸
# (a x b) % C = ((a%C) x (b%C))% C

def multiply(a, b):
    if b == 1:
        return a % C
    temp = multiply(a, b//2)

    if b % 2 == 0: #짝수면
        return(temp * temp) % C
    else:
        return(temp*temp*a)%C

print(multiply(A,B))
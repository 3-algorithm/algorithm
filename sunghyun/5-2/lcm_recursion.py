'''재귀함수를 이용한 최소공배수


70XP

평균 49분

65% 정답률

총 제출 3,507회

n개의 수가 주어졌을 때 이 수들의 최소공배수를 구하는 프로그램을 작성해보세요. 단, 재귀함수를 이용하여 문제를 해결해주세요.'''

n = int(input())
nums = list(map(int, input().split()))


# 최대공약수
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)


# 재귀로 배열 내 숫자들 차례로 lcm검사
def lcm_recursive(arr, n):
    if n == 1:
        return arr[0]
    
    return lcm(lcm_recursive(arr, n - 1), arr[n - 1])

print(lcm_recursive(nums, n))

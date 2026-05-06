# swea 4008
"""
선표는 게임을 통해 사칙 연산을 공부하고 있다.

N개의 숫자가 적혀 있는 게임 판이 있고, +, -, x, / 의 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과 값을 구해보기로 했다.

수식을 계산할 때 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산한다.

예를 들어 1, 2, 3 이 적힌 게임 판에 +와 x를 넣어 1 + 2 * 3을 만들면 1 + 2를 먼저 계산하고 그 뒤에 * 를 계산한다.

즉 1+2*3의 결과는 9이다.
 

주어진 연산자 카드를 사용하여 수식을 계산했을 때 그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력하시오.

 
[입력]

입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,

그 다음 줄부터 T 개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 숫자의 개수 N 이 주어진다.

다음 줄에는 '+', '-', '*', '/' 순서대로 연산자 카드의 개수가 공백을 사이에 두고 주어진다.

다음 줄에는 수식에 들어가는 N 개의 숫자가 순서대로 공백을 사이에 두고 주어진다.

 

[출력]

테스트 케이스 개수만큼 T 개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.

각 줄은 "#t" 로 시작하고 공백을 하나 둔 다음 정답을 출력한다. ( t 는 1 부터 시작하는 테스트 케이스의 번호이다. )

정답은 연산자 카드를 사용하여 만들 수 있는 수식으로 얻은 결과값 중 최댓값과 최솟값의 차이이다.
"""

t = int(input())


def dfs(num1, depth, plus, minus, multi, div):
    global max_end
    global min_end
    if depth == N-1:
        if num1 > max_end:
            max_end = num1
        if num1 < min_end:
            min_end = num1
    if plus > 0:
        dfs(num1 + nums[depth + 1], depth + 1, plus - 1, minus, multi, div)
    if minus > 0:
        dfs(num1 - nums[depth + 1], depth + 1, plus, minus - 1, multi, div)
    if multi > 0:
        dfs(num1 * nums[depth + 1], depth + 1, plus, minus, multi - 1, div)
    if div > 0:
        dfs(int(num1 / nums[depth + 1]), depth + 1, plus, minus, multi, div - 1)



for tes in range(1, t+1):
    N = int(input())
    # [+ - * /] 순서
    #  0 1 2 3

    max_end = -float('inf')
    min_end = float('inf')

    operate_num = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    operaters = []
    for i in range(4):
        operaters.extend([i] * operate_num[i])
    # print(operaters)

    dfs(nums[0], 0, *operate_num)

    # print(max_end, min_end)
    print(f"#{tes}", max_end - min_end)



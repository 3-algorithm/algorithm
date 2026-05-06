#swea 4012
"""
두 명의 손님에게 음식을 제공하려고 한다.

두 명의 손님은 식성이 비슷하기 때문에, 최대한 비슷한 맛의 음식을 만들어 내야 한다.

N개의 식재료가 있다.

식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)

이때, 각각의 음식을 A음식, B음식이라고 하자.

비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분해야 한다.

음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다르게 된다.


[입력]

입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고,

그 다음 줄부터 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 식재료의 수 N이 주어진다.

다음 N개의 줄에는 N * N개의 시너지 Sij값들이 주어진다. i와 j가 서로 같은 경우는 0으로 주어진다.

 

[출력]

테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.

각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t 는 1부터 시작하는 테스트 케이스의 번호이다.)

정답은 두 음식 간의 맛의 차이가 최소가 되도록 A음식과 B음식을 만들었을 때 그 차이 값이다.
"""
import itertools

t = int(input())
for tes in range(1, t+1):
    N = int(input())
    all = set(range(N))
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_diff = float('inf')
    for comb in itertools.combinations(range(N), N//2):
        other_comb = all - set(comb)
        # print(comb)
        # print(other_comb)
        flaver1 = 0
        flaver2 = 0
        # 원래 문제 이해를 잘못해서 최소값을 구했는데 알고보니 모든 재료 조합의
        # 궁합을 구하는 문제였음.
        for menu1 in itertools.combinations(comb, 2):
            flaver1 += arr[menu1[0]][menu1[1]] + arr[menu1[1]][menu1[0]]
        for menu2 in itertools.combinations(other_comb, 2):
            flaver2 += arr[menu2[0]][menu2[1]] + arr[menu2[1]][menu2[0]]
        if abs(flaver1 - flaver2) < min_diff:
            min_diff = abs(flaver1 - flaver2)
    print(f"#{tes}", min_diff)

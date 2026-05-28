'''
악수와 전염병의 상관관계 2


60XP

평균 176분

35% 정답률

총 제출 3,821회

N명의 개발자들이 있으며, T번에 걸쳐 t초에 x개발자가 y개발자와 악수를 나눈 정황이 주어집니다. 1명의 개발자가 처음에 이 전염병을 옮기기 시작한 것이 확실해 졌고, 개발자가 이 병에 감염된 후에는 정확히 K번의 악수 동안만 전염병을 옮기게 되고, 그 이후부터는 전염병에 걸려있지만 새로 옮기지는 않게 됩니다. 개발자들의 악수에 대한 정보와 처음 전염병에 걸려 있는 개발자의 번호 P가 주어졌을 때, 모든 악수를 진행한 이후에 최종적으로 누가 전염병에 걸리게 되었는지를 알아내는 프로그램을 작성해보세요.

단, 전염된 사람끼리 만나도 전염시킨 것으로 간주해야 합니다. 예를 들어 전염된 x 개발자와 전염된 y 개발자끼리 악수를 해도 전염병을 옮기게 되는 횟수에 포함시켜야 합니다. 이때, 감염 횟수에 포함될 뿐, 이미 전염되었던 사람이 재감염이 되는 것은 아님에 유의합니다.
'''

import sys
sys.stdin = open('input.txt', 'r')

N, K, P, T = map(int, input().split())

infected = [0] * (N + 1)
infected[P] = 1
term = [0] * (N + 1)
term[P] = K


lst = []
for _ in range(T):
    lst.append(list(map(int, input().split())))
lst.sort()

for t, x, y in lst:
    if infected[x] and term[x] > 0:
        if infected[y]:
            term[x] -= 1
            term[y] -= 1
            continue
        infected[y] = 1
        term[y] = K
        term[x] -= 1
        
    elif infected[y] and term[y] > 0:
        if infected[x]:
            term[x] -= 1
            term[y] -= 1
            continue
        infected[x] = 1
        term[x] = K
        term[y] -= 1

print(''.join(map(str, infected[1:])))
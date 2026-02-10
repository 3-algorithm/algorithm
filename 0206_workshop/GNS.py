import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
# for each test:
for _ in range(10):
    tc, tc_n = input().split()
    task = list(input().split())
    N = int(tc_n)

    # 각 글자형 숫자의 인덱스를 나타내는 리스트 만들음
    default = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # task에 있는 글자를 오름차순으로 담을 빈 리스트를 만들음
    answer = []
    # task를 돌면서
    for i in task:
    # task[i]가 default 기준 어디 인덱스에 있는지 확인하고 answer 리스트에 담음
        index = default.index((i))
        answer.append(index)
    # answer리스트를 오름차순으로 바꿈
    answer.sort()
    # answer에 있는 숫자를 default의 인덱스로 써서 다시 글자로 바꿈
    # final 리스트에 넣음
    final = []
    for j in answer:
        final.append(default[j])
    print(tc, *final)


# 딕셔너리 쓰는 방법:
    num_dict = {
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,
        'THR' : 3,
        'FOR' : 4,
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9,
    }
    task.sort(key = lambda  num: num_dict[num])


# 카운팅 소트 활용하는 방식
# 각 외계인 숫자를 순회하며
# 각 외계인 숫자가 몇번 나왔는지를 계산

# 0 ~ 9까지 순회하여,
# 외계인 숫자 기준으로 i가 몇번 나왔는지를 바탕으로
# i에 해당하는 외계인 숫자를 반복해서 리스트를에 정리한다.
import sys
sys.stdin = open('num_of_letters_input.txt')

# T = int(input())
# # for each testcase
# for tc in range(T):
#     # 인풋을 받음
#     str1 = list(input())
#     str2 = list(input())
#     # 가장 많은 글자의 갯수를 저장할 변수 설정
#     max_letters = 0
#     # str1과 str2를 차례대로 돌면서
#     for i in str1:
#         count = 0
#         for j in str2:
#             # str2가 각 str1의 요소를 몇개 가지고 있는지 count를 하나씩 늘리면서 센다.
#             if i == j:
#                 count += 1
#
#     # 저장한 max_letters와 count를 비교하여 count가 더 크면 replace
#         if max_letters < count:
#             max_letters = count
#     print(f'#{tc+1} {max_letters}')

############
# dict로 푸는 거
T = int(input())
# for each testcase
# 인풋을 딕셔너리로 받음
for tc in range(T):
    str1 = {}
    for letter1 in input():
        # 갯수를 세기 전 일단 벨류를 0으로 설정
        str1[letter1] = 0
    for letter2 in input():
        # str2에 있는 글자라 str1의 키값에 있으면
        # 그 글자에 해당하는 벨류값을 하나씩 늘림
        if letter2 in str1.keys():
            str1[letter2] += 1
    max_letter = max(str1.values())
    print(f'#{tc+1} {max_letter}')
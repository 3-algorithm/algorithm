import sys
sys.stdin = open("cards_input.txt", "r")

# for each test
T = int(input())
for test_case in range(T):
    N = int(input())
    cards = list(map(int, input())) # 한 글자씩 나눔


# 카드의 숫자를 카운트할 리스트 temp를 만들음 (전체 0으로)
    temp = [0]*10

# cards 리스트를 돌면서
    for card in cards:
# 각 카드(숫자 = i)에 해당하는 빈 리스트 temp[i]에 +1
        temp[card] += 1
# 가장 많은 카드의 장수를 찾음
        num_of_max = max(temp)

# temp 리스트에서 숫자가 가장 큰 인덱스 찾음 = cards 중 가장 많은 카드
# 카드 장수가 같으면 적힌 숫자가 큰 쪽을 출력하므로, temp리스트의 뒤에서부터 가장 많은 카드를 찾음
        temp_1 = temp[::-1]
        max_card = len(temp_1) - temp_1.index(num_of_max) - 1
    print(f'#{test_case+1} {max_card} {num_of_max}')







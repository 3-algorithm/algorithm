import sys
sys.stdin = open("baby_gin_input (1).txt", "r")

# for each test
T = int(input())
for test_case in range(T):
    cards = list(map(int, input().strip()))

    # 인덱스 0~9인 전체 0을 가진 리스트 temp를 만들음 <-cards에 있는 각 카드의 숫자를 담을 리스트임
    temp = [0]*10
    # 전체 run과 triplet의 갯수를 세는 변수
    baby_gin = 0

    for card in cards:
        temp[card] += 1
    # triplet을 찾자. temp에서 숫자가 3이면 triplet임
    # triplet을 찾으면 baby_gin에 1을 더함
    for i in range(len(temp)):
        while temp[i] % 3 == 0 and temp[i] != 0:
            baby_gin += 1
    # triplet을 찾으면, temp 리스트에서 제외시킴
            temp[i] -= 3
    # run을 찾자. temp를 돌면서 i, i+1,i+2 번째 숫자가 모두 1보다 크거나 같으면, run임
        while temp[i] >= 1 and temp[i+1] >= 1 and temp[i+2] >= 1:
            baby_gin += 1
    # run을 찾으면, temp 리스트에서 제외시킴
            temp[i] -= 1
            temp[i+1] -= 1
            temp[i+2] -= 1
    print(f'#{test_case+1} {baby_gin//2}')

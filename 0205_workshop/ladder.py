import sys
sys.stdin = open('ladder_input.txt')


# for each test
for tc in range(10):
    T = int(input())
# 사다리 판을 받음
    game = [list(map(int, input().split())) for _ in range(100)]
    # 사다리 판을 뒤집음
    game.reverse()

    # 첫번째 row에서 도착점(=2)를 찾음
    x = game[0].index(2)
    y = 0

    while y <= 99:
        # 오른쪽에 1이 있으면 현재 있는 숫자를 0으로 바꾸고, 오른쪽으로 한칸 이동
        if x+1 <=99 and game[y][x+1] == 1:
            game[y][x] = 0
            x += 1
        # 왼쪽에 1이 있으면 현재 있는 숫자를 0으로 바꾸고, 왼쪽으로 한칸 이동
        elif x-1 >= 0 and game[y][x-1] == 1:
            game[y][x] = 0
            x -= 1
        # 둘다 아니면, 아래로 한칸 이동
        else:
            y += 1
    print(f'#{tc+1} {x}')


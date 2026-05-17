'''
흰검 칠하기


70XP

평균 180분

43% 정답률

총 제출 4,327회

일직선으로 무한히 나열된 타일이 있습니다. 아무 타일에서 시작하여 N번의 명령에 걸쳐 움직입니다.

명령은 x L, x R 형태로만 주어지며, x L의 경우 왼쪽으로 이동하면서 현재 위치 타일포함 총 x칸의 타일을 흰색으로 연속하게 칠하고, x R의 경우 오른쪽으로 이동하면서 현재 위치 타일포함 총 x칸의 타일을 검은색으로 연속하게 칠함을 뜻합니다.

각 명령 이후에는 마지막으로 칠한 타일 위치에 서있는다고 가정합니다. 타일의 색은 덧칠해지면 마지막으로 칠해진 색으로 바뀌는데, 만약 타일 하나가 순서 상관없이 흰색과 검은색으로 각각 두 번 이상 칠해지면 회색으로 바뀌고 더 이상 바뀌지 않습니다.

모든 명령을 실행한 뒤의 흰색, 검은색, 회색의 타일 수를 각각 출력하는 프로그램을 작성해보세요.
'''

n = int(input())

commands = [tuple(input().split()) for _ in range(n)]

tiles = [0] * 2000001
black = [0] * 2000001
white = [0] * 2000001
s = 100000
for x, c in commands:
    x = int(x)
    # 명령 L 일 때
    if c == 'L':
        for i in range(x):
            if i != 0:
                s -= 1
            black[s] += 1
            # 회색 처리
            if black[s] >= 2 and white[s] >= 2:
                tiles[s] = 3
            # 검은색 처리
            else:
                tiles[s] = -1

    # 명령 R 일 때
    elif c == 'R':
        for i in range(x):
            if i != 0:
                s += 1
            white[s] += 1
            # 회색 처리
            if black[s] >= 2 and white[s] >= 2:
                tiles[s] = 3
            # 흰색 처리
            else:
                tiles[s] = 1

w, b, g = 0, 0, 0
for t in tiles:
    if t == -1:
        w += 1
    elif t == 1:
        b += 1
    elif t == 3:
        g += 1

print(w, b, g)

# 회색 처리 시 L/R 따로 세기 (x가 1일 경우  LLLR로도 지나간 횟수 4가 되기 때문)
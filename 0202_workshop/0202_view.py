import sys
sys.stdin = open("view_input.txt", "r")

for test in range(1, 11):
    # 총 빌딩의 갯수
    N = int(input())
    # 각 빌딩의 높이
    buildings = list(map(int, input().split()))

    view = 0
    # 각 건물(i)별로 아래를 확인하자
    # 맨 왼쪽 두칸/ 맨 오른쪽 두칸은   안쓰니까
    # 2부터 n-2까지만 반복한다 ([2, n-2))
    for i in range(2, N-2, 1):
        # i번째 건물이 i-1, i-2, i+1, i+2보다 크면 계산 시작
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
        # 건물 i - (i-1),  i - (i-2),  i - (i+1),  i - (i+2) 중 가장 작은 값(min) 이 조망권 확보된 세대
        # view = 0 = 조망권 확보된 세대 <- 에 min 값을 다 더함.
            view += min(buildings[i] - buildings[i-1], buildings[i] - buildings[i-2], buildings[i] - buildings[i+1], buildings[i] - buildings[i+2])
    print(f'#{test} {view}')


import sys
sys.stdin = open("colours_input.txt")


T = int(input())
# for each test
for test_case in range(T):

    # Let N = 색칠된 영역 갯수
    N = int(input())

    red = []
    blue = []
    # 각 영역을 리스트로 받은
    for area in range(N):
        area = list(map(int,input().split()))

            # 변수 설정:
            # Let start = 컬러링 시작 포인트, end = 컬러링 끝나는 포인트, colour
        start_i, start_j = area[0], area[1]
        end_i, end_j = area[2], area[3]

        colour = area[4]

            # 각 색깔별로 색칠되어 있는 coordinates 찾기:
            # 빨간색이면 red 리스트에, 파란색이면 blue 리스트에 넣기
        if colour == 1:

            # 시작점에서 돌면서 끝지점까지 리스트에 coordinate넣기
            for i in range(start_i, end_i +1):
                for j in range(start_j, end_j + 1):
                    red.append([i,j])

        elif colour == 2:
            # 시작점에서 돌면서 끝지점까지 리스트에 coordinate넣기
            for k in range(start_i, end_i +1):
                for m in range(start_j, end_j + 1):
                    blue.append([k,m])


        #보라색인 부분 카운트:
    purple = 0
    for coloured in red:
        if coloured in blue:
            purple += 1

    print(f'#{test_case+1} {purple}')


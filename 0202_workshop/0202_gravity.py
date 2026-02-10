import sys
sys.stdin = open("gravity_input.txt", "r")


# for each test
T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    boxes = list(map(int, input().split()))
    # 최대 낙차를 기록할 변수
    max_fall = 0

    # 각 칸에 상자가 쌓인 높이를 확인
    for i in range(N):

# 나보다 높게 쌓인(오른쪽) 상자들의 갯수를 기록할 변수를 만들음
        taller_boxes = 0
    # 나보다 오른쪽 상자들을 살펴봄
        for j in range(i+1, N):
    # 만약 나보다 높거나 같으면
            if boxes[j] >= boxes[i]:
    # 더 컸던 상자들의 갯수를 기록한다
                taller_boxes += 1

    # 내가 낙하할 수 있는 최대 거리는
    # 내가 오른쪽에서 떨어진 만큼 - 나를 방해하는 상자의 갯수
        cur_fall = (N - i - 1) - taller_boxes
    # 나의 최대거리랑 기록된 최대 거리를 비교
        if max_fall < cur_fall:
            max_fall = cur_fall
    print(f'#{test_case} {cur_fall}')
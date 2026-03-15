# swea 스택2-2: 토너먼트 카드게임

import sys
sys.stdin = open("tornament_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 가위바위보 하는 함수
    def scissors_paper_stone(p1, p2):
        if (numbers[p1] == 1 and numbers[p2] !=2) or (numbers[p1] == 2 and numbers[p2] !=3) or (numbers[p1] == 3 and numbers[p2] !=1):
            return p1
        else:
            return p2

    # 토너먼트로 자르는 함수
    def tournament(first, last):
        # 한명 남았으면 부전승
        if first == last:
            return first
        middle = (first + last)// 2
        left = tournament(first, middle)
        right = tournament(middle + 1, last)
        return scissors_paper_stone(left, right)


    print(f'#{tc}', tournament(0, N-1) + 1)
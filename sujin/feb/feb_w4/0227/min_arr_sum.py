#swea 스택2-2: 배열 최소 합

import sys
sys.stdin = open("minarr_input.txt")


def find_min_arr(row, current_sum):
    global min_sum
    # 가지치기 - 현재 합이 최소 합보다 크면 더 볼 필요가 없음
    if current_sum >= min_sum:
        return

    # 마지막 row까지 갔으면 최소 합 갱신
    if row == N:
        min_sum = min(min_sum, current_sum)

    # 현재 행에서 각 열을 하나씩 선택해보기
    for col in range(N):
        if not visited[col]:
            # 아직 선택되지 않은 열이라면
            # 가서 트루로 방문 표시를 하고
            # 다음 행으로 이동동
            visited[col] = True
            find_min_arr(row+1, current_sum + arr[row][col])
            # 여기까지 왔다는건 해당 배율을 모두 탐색한 것
            # 재귀 끝나면 체크한 것을 취소 // 초기화 시켜주는 것
            visited[col] = False

T = int(input())
for tc in range(1, T+1):
    N= int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 열 선택 여부 확인용 # 같은 콜럼에서 숫자 안뽑게
    visited = [False] * N
    min_sum = 10*50
    find_min_arr(0, 0)
    print(f'#{tc}', min_sum)

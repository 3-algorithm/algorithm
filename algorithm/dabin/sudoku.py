import sys
sys.stdin = open("input_sudoku.txt")

T = int(input())
N = 9
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 검사할 때 중복된 게 없어야 하므로 똑같이 set으로 비교하기 위해 set으로 설정
    val_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    flag = True
    # 행 검사
    for i in range(N):
        # 한 행씩 1~9의 수로 이루어져 있는지 확인 후 아닐 경우 flag를 False로 변경
        if set(arr[i]) != val_set:
            flag = False
    # 열 검사
    for j in range(N):
        # j는 0~9까지 돌면서 고정시킨 채 i를 0~9인 돌리면서 열 리스트를 col에 저장 후 똑같이 set으로 비교 후 flag 변경
        col = [arr[i][j] for i in range(N)]
        if set(col) != val_set:
            flag = False
    # 3x3 검사
    # index를 0부터 9까지로 두되 3씩 건너뛰면서 index 조정
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # 하나의 box 값들을 저장할 변수 초기화
            box = []
            # 인덱스 기준 3개씩 돌면서 3x3 값을 box에 저장
            for k in range(i, i+3):
                for m in range(j, j+3):
                    box.append(arr[k][m])
            # box에 저장된 값들을 set으로 변환 후 비교 및 flag 변경
            if set(box) != val_set:
                flag = False
            
    # flag값(t, f)를 정수 형태로 출력        
    print(f"#{tc} {int(flag)}")
    
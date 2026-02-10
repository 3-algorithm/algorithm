import sys
sys.stdin = open("sudoku_input.txt")

T = int(input())

# for each test
for test_case in range(1, 11):
    matrix = [list(map(int, input().split())) for _ in range(9)]

    sudoku = 0
    # 가로줄 겹치는거 없는지 확인
    for row in matrix:
        check = []
        for number in row:
            if number not in check:
                check.append(number)
        if len(check) == 9:
            sudoku += 1

    # 세로줄 겹치는거 없는지 확인
    for i in range(9):
        check_1 = []
        for j in range(9):
            if matrix[j][i] not in check_1:
                check_1.append(matrix[j][i])
        if len(check_1) == 9:
            sudoku += 1
    print(f'{test_case} {sudoku}')

    # 3x3 박스별로 겹치는거 없는지 확인



    for n in range(0, 8, 3):
        for m in range(0, 8, 3):
            box = []
            check_2 = []
            for k in range(n, n+3):
                for j in range(m,m+3):
                    box.append(matrix[i][j])
            for num in box:
                if num not in check_2:
                    check_2.append(num)

        print(f'{test_case} {box}')

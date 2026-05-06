import sys
sys.stdin = open('passcode_scan.txt')

# 16진수 -> 2진수 dictionary
hex_to_bin = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1],
}


# 뒤의 세 연속된 1과 0으로 암호코드를 숫자로 바꾸는 dictionary
passcode_dict = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    # n줄의 입력을 받으면서 각 숫자를 2진수로 바꿔서 저장한다.
    # 16 -> 2: 각 숫자를 키로 갖고 2진수로 바뀐 결과를 값으로 갖는 딕셔너리를 활용
    # n줄 입력받을 준비
    arr = [[] for _ in range(n)]
    # n번 반복해서 각 줄 입력받기
    for i in range(n):
        # 각 줄을 한 글자씩 잘라서 tmp에 저장
        tmp = input().strip()
        # 한 줄씩 돌면서 각 글자를 2진수로 변환(hex_to_bin dictionary에서 키에 맞는 값을 받아오기)하여 arr에 저장
        for hex_num in tmp:
            arr[i].extend(hex_to_bin[hex_num])

    answer = 0
    # 각 줄을 가져와서 확인한다
    for row_idx in range(n):
        # 뒤에서부터 한글자씩 확인하며 0이 아닌 순간을 찾기(마지막 글자는 암호상 0일 수가 없으므로)

        # 뒤에서부터 총 56글자는 확보가 되어야 하므로
        # 시작 지점에서 56글자 떨어진 index == 55 까지(idx가 54이하면 어차피 암호 길이 확보가 안되므로)
        # 2진수 변환 때문에 4배씩 길어졌으므로
        idx = m * 4 - 1  # 각 줄의 마지막 idx
        while idx > 54:
            # 1을 만났는데 만약 윗줄(row_idx-1)의 같은칸(idx)도 1이라면
            # 이전 줄에서 확인한 코드이므로 다음 칸으로 넘어간다.
            if not (arr[row_idx][idx] == 1 and arr[row_idx - 1][idx] == 0):
                idx -= 1
                continue

            # 비밀번호를 만들자
            password = []
            # 비밀번호는 총 8글자
            for _ in range(8):
                # 각각 두번째1, 세번째0, 네번째1의 갯수를 세기 위한 변수들
                c2 = c3 = c4 = 0
                # 이전 숫자의 1번째 0을 스킵한다. (= 처음 마지막이 1인 수를 찾는 것과 동일)
                while arr[row_idx][idx] == 0:
                    idx -= 1
                # 이번 숫자의 4번째 1의 갯수를 센다
                while arr[row_idx][idx] == 1:
                    c4 += 1
                    # 다음 칸으로
                    idx -= 1
                # 이번 숫자의 3번째 0의 갯수를 센다
                while arr[row_idx][idx] == 0:
                    c3 += 1
                    idx -= 1
                # 이번 숫자의 2번째 1의 갯수를 센다
                while arr[row_idx][idx] == 1:
                    c2 += 1
                    idx -= 1
                # 숫자 당 최소 하나의 한칸을 가지고 있으므로
                # c2, c3, c4 중 가장 작은 수가 한칸을 나타낸다.
                ratio = min(c2, c3, c4)
                # 암호에 추가한다.
                password.append(passcode_dict[(c2//ratio, c3//ratio, c4//ratio)])

            # 이번 비밀번호를 검증하고 다음칸으로
            even_sum = password[0] + password[2] + password[4] + password[6]
            odd_sum = password[1] + password[3] + password[5] + password[7]
            if (odd_sum * 3 + even_sum) % 10 == 0:
                answer += odd_sum + even_sum
            idx -= 1

    print(f'#{tc} {answer}')

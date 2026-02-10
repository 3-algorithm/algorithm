import sys
sys.stdin = open('palindrome1_input.txt')

# palindrome function:
def is_palindrome(letters):
    for i in range(N // 2):
        if letters[i] != letters[N - 1 - i]:
            return False
    return True
# for each test

for tc in range(10):
    # input 받기
    N = int(input())
    matrix = [list(input()) for _ in range(8)]

    count = 0
    # 가로 탐색
    for y in range(8):
        for x in range(8-N+1):
            letters_h = matrix[y][x:x+N]
            if is_palindrome(letters_h):
                count += 1
    # 세로 탐색
    for x in range(8):
        for y in range(0, 8-N+1):
            letters_v = []

            while y <=7 and len(letters_v) < N:
                letters_v.append(matrix[y][x])
                y+=1

            if is_palindrome(letters_v):
                count+=1

    print(f'#{tc+1} {count}')
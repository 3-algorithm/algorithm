import sys
sys.stdin = open('beginners_.txt')

T = int(input())


def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[N - 1 - i]:
            return False
    return True

for tc in range(T):
    word = list(input())

    # 단어의 길이를 잼
    N = len(word)

    # 회문인가 ? 맞으면 1
    if is_palindrome(word):
        print(f'#{tc+1} 1')
    # 아니면 0
    else:
        print(f'#{tc+1} 0')
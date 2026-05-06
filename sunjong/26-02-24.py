import sys

def solve():
    # 입력을 읽어옵니다.
    try:
        n = int(sys.stdin.readline())
        f = int(sys.stdin.readline())
    except ValueError:
        return

    # n의 뒤 두 자리를 00으로 만듭니다.
    n -= (n % 100)
    
    ans = -1
    # 00부터 99까지 더해보며 f로 나누어떨어지는지 확인합니다.
    for i in range(100):
        if (n + i) % f == 0:
            ans = i
            break # 가장 작은 수를 찾으면 즉시 종료합니다.
            
    # 결과를 두 자리 숫자로 출력합니다 (예: 7 -> 07)
    # :02d는 최소 2자리를 확보하고 빈칸을 0으로 채우라는 의미입니다.
    print(f"{ans:02d}")

if __name__ == "__main__":
    solve()
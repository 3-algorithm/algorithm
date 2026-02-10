import sys
sys.stdin = open('binary_input.txt')

T = int(input())

for tc in range(T):
    def binary_search(end, target):
        start = 1
        count = 0
        while start <= end:

            mid = (start + end) // 2
            if mid == target:
                return count
            if mid > target:
                end = mid
            elif mid < target:
                start = mid
            count += 1

    P, A, B = map(int, input().split())
    score_A = binary_search(P, A)
    score_B = binary_search(P, B)
    if score_A < score_B:
        print(f"#{tc+1} A")
    elif score_A > score_B:
        print(f"#{tc+1} B")
    elif score_A == score_B:
        print(f"#{tc+1} 0")

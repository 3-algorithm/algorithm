import sys
sys.stdin = open("input_subset.txt")
 
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # 총 부분집합의 개수를 셀 변수 초기화
    cnt = 0
    # 부분 집합의 개수만큼 돌면서
    for i in range(1 << 12):
        # 현재 부분집합의 길이와 원소의 합을 저장할 변수 초기화
        count = 0
        total = 0
        # 원소의 수만큼 비트 비교
        for j in range(12):
            # i의 j번 비트가 1인 경우 (즉, A 리스트에서 j번째 원소가 부분집합의 요소로 있다면)
            if i & (1 << j):
                # 원소의 합에 해당 원소를 더하고
                total += A[j]
                # 원소의 개수 하나 올림
                count += 1
        # 원소의 수만큼 비트 비교를 마친 후 부분집합의 원소의 개수와 원소의 합이 문제 조건과 동일하면
        if count == N and total == K:
            # 총 부분집합의 개수 하나 올리기
            cnt += 1
    print(f"#{tc} {cnt}")
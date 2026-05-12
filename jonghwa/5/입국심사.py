#https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV_XEokaAEcDFAX7&probBoxId=AV_W57U6ACQDFAX7&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%A4%80%EB%B9%84+%EB%AC%B8%EC%A0%9C&problemBoxCnt=4

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,M= map(int,input().split())
    times=[]
    for _ in range(N):
        times.append(int(input()))
     
    left = 1
    right = max(times) * M
    answer = right
 
# 2. 이분 탐색 시작
    while left <= right:
        mid = (left + right) // 2  # 주어진 시간 T (중간값)
         
        # mid 시간 동안 모든 심사대에서 심사할 수 있는 총인원 계산
        total_people = 0
        for t in times:
            total_people += (mid // t)
             
        # 3. 조건 판별 및 범위 축소
        if total_people >= M:
            # M명 이상 심사할 수 있다면, 일단 정답 후보에 저장하고
            answer = mid
            # 더 짧은 시간에도 가능한지 확인하기 위해 right를 줄임
            right = mid - 1
        else:
            # M명을 심사할 수 없다면, 시간이 더 필요하므로 left를 늘림
            left = mid + 1
             
    # 결과 출력
    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////

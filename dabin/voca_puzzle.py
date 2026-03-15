import sys
sys.stdin = open("input_voca.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 단어의 길이와 동일한지 확인 후 개수 저장할 변수 초기화
    fit = 0
    # 행 돌면서 검사
    for i in range(N):
        # 1인 길이를 재기 위해 변수 초기화
        cnt = 0
        for j in range(N):
            # 값이 1이면 cnt를 증가시켜서 길이 재기
            if arr[i][j] == 1:
                cnt += 1
            # 값이 1이 아니라면 여태까지의 1의 길이가 단어의 길이와 일치하는지 확인 후 다시 cnt를 0으로 초기화
            else:
                if cnt == K:
                    fit += 1
                cnt = 0
        # 마지막으로 행을 다 돈 후에도 검사 (배열 마지막 부분이라면 else문을 만나지 못하므로 검사를 건너 뛰게 되므로)
        if cnt == K:
            fit += 1   
            
    # 열도 행과 마찬가지로 검사         
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    fit += 1
                cnt = 0
        if cnt == K:
            fit += 1    
            
    print(f"#{tc} {fit}")
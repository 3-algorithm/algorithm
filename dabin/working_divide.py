import sys
sys.stdin = open("input_working.txt")

def dividing(cnt, per):
    global max_per
    
    # 가지치기(곱할수록 값이 작아지므로 현재 확률값이 작거나 같으면 더 계산하지 않고 종료)
    if per <= max_per:
        return
    
    # N개를 다 뽑았으면 max_per에 현재 확률값 넣고 확률 종료
    if cnt == N:
        max_per = per
        return
    
    # 배열 길이만큼 돌면서
    for i in range(len(arr)):
        # 방문한 적이 없으면
        if visited[i] == 0:
            # 값이 0이면 확률값이 0이므로 굳이 더 계산하지 않음
            if arr[cnt][i] == 0:
                continue
            # 방문 표시 후 
            visited[i] = 1
            # 재귀(현재값으로 확률값 계산한 뒤)
            dividing(cnt + 1, per*(arr[cnt][i]/100))
            # 방문 초기화
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = []
    visited = [0] * N
    max_per = 0
    

    dividing(0, 1.0)

    print(f"#{tc} {max_per*100:.6f}")
import sys
sys.stdin = open("input_fly.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 최종으로 가장 큰 합을 저장할 변수 초기화
    max_sum = 0
    # NxN을 돌되 인덱스에러를 피하기 위해 범위 설정
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 파리채로 잡았을 때 해당되는 값을 저장할 리스트 초기화
            shot = []
            # MxM 만큼 돌면서 파리채로 잡았을 때 해당되는 값을 리스트에 저장
            for k in range(i, i+M):
                for m in range(j, j+M):
                    shot.append(arr[k][m])
            # 최댓값 갱신
            if max_sum < sum(shot):
                max_sum = sum(shot)
    
    print(f"#{tc} {max_sum}")
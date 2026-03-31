import sys
sys.stdin = open("input_magic.txt")

def search(cur_r, cur_w, cur_v):

    global result

    # result와 현재 더해진 가치 중 더 큰 값을 result로 갱신
    result = max(result, cur_v)

    # 현재 방 번호를 키로 갖는 값이 없다면(최하위 노드라면) 함수 종료
    if cur_r not in tree:
        return
    
    # 현재 방 번호를 키로 갖는 값을 돌면서
    for next_r, next_w, next_v in tree[cur_r]:
        # 무게합이 기준값보다 작거나 같다면
        if cur_w + next_w <= K:
            # 이번 방 보물 챙겨서 search 재귀
            search(next_r, cur_w + next_w, cur_v + next_v)
        # 무게합이 기준값보다 크면 이번 방 보물 안 챙기고 search 재귀
        search(next_r, cur_w, cur_v)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 직전방 번호에 따른 현재 방 번호, 무게, 가치를 저장할 딕셔너리 초기화
    tree = {}
    # 최종 가치 저장할 변수 초기화
    result = 0

    # 입력값 돌면서 
    for r, w, v, p in arr:
        # 직전방 번호가 tree키 값으로 없으면 빈 리스트로 새로 생성
        if p not in tree:
            tree[p] = []
        # 직전방 번호를 키로 하는 r, w, v 저장
        tree[p].append([r, w, v])

    # tree의 키값이 0이면 트리의 시작점이므로 무게 확인 후 search 시작
    for start_r, start_w, start_v in tree[0]:
        # 무게가 아직 적다면
        if start_w <= K:
            # 시작점 기준 무게, 가치 넣어서 탐색
            search(start_r, start_w, start_v)
        # 무게가 차 있는 경우 현재 무게, 가치 무시하고 탐색
        search(start_r, 0, 0)

    print(f"#{tc} {result}")
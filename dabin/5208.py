# 전기버스2 (최소로 배터리 교체하는 법)

def backtracking(idx, cur_battery, new_cnt):
    global cnt

    # 여태까지 교환한 수가 초기값보다 크거나 같으면 return
    if new_cnt >= cnt:
        return
    
    # 현재 정류장 위치에서 가능한 배터리를 충전해서 갈 수 있는 위치가 최종 정류장보다 크거나 같으면
    if idx + cur_battery >= n:
        # 현재까지 교환한 수가 초기값보다 작으면 현재까지 교환한 수로 카운트 갱신 후 return
        if new_cnt < cnt:
            cnt = new_cnt
        return 
    
    # 충전하고 다음 스텝으로 옮기는 경우
    backtracking(idx + 1, bus_stop[idx] - 1, new_cnt + 1)

    # 충전하지 않고 다음 스텝으로 옮기는 경우(배터리가 있어야 한다는 조건 추가)
    if cur_battery > 0:
        backtracking(idx + 1, cur_battery - 1, new_cnt)

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    # 처음 배열로 받은 값에서 처음 값이 버스정류장의 길이
    n = arr[0]
    # 버스정류장 배열 만든 후 해당 정류장에 맞는 가능한 배터리 충전 수 저장
    bus_stop = [0] * (n+1)

    for i in range(1, n):
        bus_stop[i] = arr[i]

    # 최소 교체 수를 카운트 해야하므로 초기값을 높게 잡음
    cnt = int(1e9)

    # 두 번째 정류장으로 이동하면서 현재 배터리에서 하나 이동한 값 빼줌, 아직 교환 안 했으므로 new_cnt = 0
    backtracking(2, bus_stop[1] - 1, 0)

    print(f"#{tc} {cnt}")
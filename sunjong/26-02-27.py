import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

def solve():
    # N(도시 크기), M(남길 치킨집 개수) 입력
    n, m = map(int, input().split())
    
    chicken = []
    homes = []

    # 도시 정보 입력 및 위치 저장
    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(n):
            if row[c] == 1:
                homes.append((r, c))
            elif row[c] == 2:
                chicken.append((r, c))

    min_city_dist = float('inf')
    num_chickens = len(chicken)

    # 비트마스킹을 이용한 조합 탐색 (2^치킨집 개수)
    for i in range(1 << num_chickens):
        # 선택된 치킨집의 개수가 M개인 경우만 처리
        if bin(i).count('1') != m:
            continue

        total_sum = 0
        # 각 집마다 가장 가까운 치킨집과의 거리 계산
        for hr, hc in homes:
            temp_dist = float('inf')
            for z in range(num_chickens):
                # i의 z번째 비트가 1이라면 (z번째 치킨집 선택)
                if i & (1 << z):
                    cr, cc = chicken[z]
                    dist = abs(hr - cr) + abs(hc - cc)
                    if dist < temp_dist:
                        temp_dist = dist
            total_sum += temp_dist
            
            # 이미 현재 최소값보다 크다면 계산 중단 (최적화)
            if total_sum >= min_city_dist:
                break
        
        if total_sum < min_city_dist:
            min_city_dist = total_sum

    print(min_city_dist)

if __name__ == "__main__":
    solve()

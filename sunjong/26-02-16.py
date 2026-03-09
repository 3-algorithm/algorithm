import sys
input = sys.stdin.readline
    
n = int(input())
dice_list = []
    
for i in range(n):
    dice = list(map(int, input().split()))
    dice_list.append(dice)
    
top = [0, 1, 2, 3, 4, 5]
bottom = [5, 3, 4, 1, 2, 0]
    
max_sum = 0
    
for i in range(6):
        # 모든 경우의 수 탐색 -> bottom과 같을 때 최대값
    t_top = dice_list[0][top[i]]
    t_bottom = dice_list[0][bottom[i]]
    t_max = 0
        
    for j in range(6):
        if j != top[i] and j != bottom[i]:
            t_max = max(t_max, dice_list[0][j])
        
    for j in range(1, n):
        # 각 면이 bottom과 같은지 확인
        # 확인 후 max 값 확인
        check_max = 0
            
        for z in range(6):
            if t_bottom == dice_list[j][z]:
                for k in range(6):
                    if k != top[z] and k != bottom[z]:
                        check_max = max(check_max, dice_list[j][k])
                    
                t_top = dice_list[j][top[z]]
                t_bottom = dice_list[j][bottom[z]]
                break
            
        t_max += check_max
        
    # print(f"tMax = {t_max}")  # 디버그 출력 (제출 시 주석 처리)
    max_sum = max(max_sum, t_max)
    
print(max_sum)


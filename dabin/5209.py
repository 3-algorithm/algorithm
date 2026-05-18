def backtracking(idx, current_cost):
    global min_cost

    if current_cost >= min_cost:
        return
    
    if idx == N:
        if current_cost < min_cost:
            min_cost = current_cost
        return
    
    for factory_idx in range(N):
        if not visited[factory_idx]:
            visited[factory_idx] = 1

            backtracking(idx + 1, current_cost + matrix[idx][factory_idx])

            visited[factory_idx] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    min_cost = int(1e9)
    
    visited = [0] * N
    matrix = [list(map(int, input().split())) for _ in range(N)]

    backtracking(0, 0)

    print(f"#{tc} {min_cost}")
import sys
from collections import deque

sys.stdin = open("input.txt", "r") 

T = int(input())

for test_case in range(1, T + 1):
    # N: 사람 수, M: 간선 수
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    

    graph = [[] for _ in range(N + 1)]
    
    # 2개씩 짝지어 양방향 간선으로 연결
    for i in range(M):
        u = data[i * 2]
        v = data[i * 2 + 1]
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * (N + 1)
    group_count = 0
    
    # 1번 사람부터 N번 사람까지 순회
    for i in range(1, N + 1):
        # 아직 조가 편성되지 않은 사람(방문하지 않은 노드)을 발견하면
        if not visited[i]:
            # 새로운 조를 하나 결성
            group_count += 1
            
            # BFS 탐색
            queue = deque([i])
            visited[i] = True
            
            while queue:
                curr = queue.popleft()
                
                # 현재 사람과 조가 되고 싶어하는 주변 사람들을 확인
                for neighbor in graph[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        
    # 정답 출력 양식에 맞춰 출력
    print(f"#{test_case} {group_count}")
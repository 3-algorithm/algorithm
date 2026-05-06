# https://www.acmicpc.net/problem/2606

import sys

def search(start, n, graph, visited):
    visited[start] = True
    
    for i in range(1, n + 1):
        # 연결되어 있고 아직 방문하지 않았다면 탐색
        if graph[start][i] == 1 and not visited[i]:
            search(i, n, graph, visited)

def main():
    input = sys.stdin.read().split()
    if not input:
        return
        
    n = int(input[0])  # 노드의 수
    m = int(input[1])  # 간선의 수
    
    # 인접 행렬 초기화 (n + 1 크기)
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    # 간선 정보 입력
    idx = 2
    for _ in range(m):
        u = int(input[idx])
        v = int(input[idx + 1])
        graph[u][v] = 1
        graph[v][u] = 1
        idx += 2
    
    # 1번 노드부터 탐색 시작
    search(1, n, graph, visited)
    
    # 1번 노드를 제외한 연결된 노드 수 계산
    cnt = sum(1 for i in range(1, n + 1) if visited[i])
    print(cnt - 1)

if __name__ == "__main__":
    main()

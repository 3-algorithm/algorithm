import sys

# 재귀 깊이 제한 늘리기 (DFS 사용 시 필수)
sys.setrecursionlimit(10**6)

def solve():
    # 빠른 입력을 위해 stdin 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 정점의 개수
    m = int(input_data[1]) # 간선의 개수
    
    # 인접 리스트로 그래프 구현 (인접 행렬보다 메모리 효율적)
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    # 간선 정보 입력
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        graph[u].append(v)
        graph[v].append(u)
        idx += 2

    # DFS 탐색 함수
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    # 1번 노드부터 탐색 시작
    dfs(1)

    # 방문한 노드 개수 세기 (1번 노드 자신은 제외하므로 -1)
    cnt = sum(1 for v in visited if v)
    print(cnt - 1)

if __name__ == "__main__":
    solve()
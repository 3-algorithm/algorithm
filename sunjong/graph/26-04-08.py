# https://www.acmicpc.net/problem/11403

import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    graph = []
    curr_idx = 1
    for i in range(n):
        graph.append(list(map(int, input_data[curr_idx:curr_idx + n])))
        curr_idx += n

    def dfs(start, target):
        stack = [start]
        vis = [0] * n
        # Java 코드와 마찬가지로 vis[start] = 1을 미리 하지 않음 (사이클 확인용)

        while stack:
            cur_node = stack.pop()

            for next_node in range(n):
                # 연결되어 있고 방문하지 않았다면
                if graph[cur_node][next_node] == 1 and vis[next_node] == 0:
                    if next_node == target:
                        return 1
                    
                    vis[next_node] = 1
                    stack.append(next_node)
        return 0

    # 결과 출력
    for i in range(n):
        row_result = []
        for j in range(n):
            row_result.append(str(dfs(i, j)))
        print(" ".join(row_result))

if __name__ == "__main__":
    solve()

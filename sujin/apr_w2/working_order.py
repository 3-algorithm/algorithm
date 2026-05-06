import sys
sys.stdin = open("work_input.txt")





from collections import deque

# kahn 알고리즘
for tc in range(1, 11):
    nodes, edges = map(int, input().split())

    in_degree = [0]*(nodes+1)
# 인접 리스트
    adj = [[] for _ in range(nodes+1)]
    arr = list(map(int, input().split()))
    for i in range(edges):
        adj[arr[i*2]].append(arr[i*2+1])
        # in_degree: 나한테 들어오는 간선이 몇개인지 기록
        # 0인거를 먼저 시작
        in_degree[arr[i*2+1]] +=1



# 덱 => deque(0,8) => 다음에 방문할 정점을 담아주는 용도
    q = deque()
    for start in range(1, nodes+1):
        if in_degree[start] ==0:
            q.append(start)

# while len(q) != 0:
#     # 앞에서부터 하나씩 뽑아서
#     # now = 4
#     # in_degree(1) - 1 = 0 => 0이 되면 큐에 어팬드
    result = []
    while q:
        # 다음 점을 방문
        now = q.popleft()
        # 순서를 기록
        result.append(now)
        # 현재 방문한 점에서 방문 가능한 점들의 진입 차수를 하나 줄여줌
        for next in adj[now]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)
    print(f'#{tc}', *result)
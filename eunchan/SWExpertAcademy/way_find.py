# swea 24220
"""
경로 1 : 1 -> 3 -> 4
경로 2 : 1 -> 3 -> 2 -> 5 -> 4
경로 3 : 1 -> 2 -> 5 -> 4
경로 4 : 1 -> 2 -> 5 -> 3 -> 4

1 -> 3 -> 2 -> 5 -> 3 -> 4는 ​3번 정점을 두번 방문하므로 경로가 아니다.​​​​​​

방향성 그래프와 출발, 도착 정점이 주어지면, 경로에 포함된 정점을 한 번만 방문해서 이동 가능한 경로가 몇 개인지 찾아보자.

* 모든 정점을 지나야 하는 것은 아니다.
* 사이클이 존재할 수 있다.

[입력]
첫 줄에 테스트케이스개수 T (1<=T<=50), 다음 줄부터 케이스 별로 세 줄에 걸쳐 첫 줄에 마지막 정점번호 N과 간선 수 E, 다음 줄에 E개 간선의 양 끝 정점 번호(출발 도착 순), 마지막 줄에 경로를 찾기 위한 출발 정점 S와 도착정점번호G가 주어진다.
(3<=N<=20, N-1<=E<=N*(N-1)/2)
  
[출력]
테스트케이스 별로 각 줄에 #과 1번부터 시작하는 케이스번호, 빈칸에 이어 답을 출력한다.

"""
tes = int(input())


def bfs(visited, start, goal, path):
    if start == goal:
        path = tuple(path)
        if path not in find:
            find.add(path)
        return
    for i in ways[start]:
        if not visited[i]:
            visited[i] = True
            path.append(i)
            bfs(visited, i, goal, path)
            path.pop()
            visited[i] = False


for t in range(1, tes + 1):
    N, E = map(int, input().split())
    ways = {}
    info = list(map(int, input().split()))
    for i in range(E):
        if ways.setdefault(info[2*i], [info[2*i+1]]) != [info[2*i+1]]:
            ways[info[2*i]].append(info[2*i++1])
    # print(ways)

    start, goal = map(int, input().split())
    find = set()
    visited = [False] * (N + 1)
    visited[start] = True
    bfs(visited, start, goal, [start])
    # print(find)
    print(f"#{t}", len(find))

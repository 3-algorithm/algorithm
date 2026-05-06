# 바킹독 - 백트래킹 - N과 M(1)
# https://www.acmicpc.net/problem/15649

N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

# 방문 체크를 위한 리스트
visited = [False]*len(arr)
final = []
def recur(cnt):
    if cnt == M:
        print(*final)
        return
    for i in range(0, len(arr)): # 항상 0부터 훑음
        # visited가 false면 아직 안 뽑은 숫자인거
        if not visited[i]:
            visited[i] = True # 방문표시
            final.append(arr[i])

            # 다음 숫자 뽑음
            recur(cnt+1)

            final.pop()
            visited[i] = False
recur(0)

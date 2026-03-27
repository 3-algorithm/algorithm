#바킹독 - 연결리스트 - 요세푸스 문제
# https://www.acmicpc.net/problem/1158


from collections import deque
temp = deque()
N, K = map(int, input().split())
for i in range(1, N+1):
    temp.append(i)
final = []

while temp:
    for i in range(K-1):
        temp.append(temp.popleft())
    final.append(temp.popleft())
print("<" + ", ".join(map(str,final))+">")
import sys
import heapq
input = sys.stdin.readline

N=int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort(key=lambda x:(x[0],x[1]))

room_heap = []
heapq.heappush(room_heap,arr[0][1])

for i in range(1,N):
    current_start=arr[i][0]
    current_end=arr[i][1]

    if current_start >= room_heap[0]:
        heapq.heappop(room_heap)
    heapq.heappush(room_heap,current_end)

print(len(room_heap))
import sys

input=sys.stdin.readline
N=int(input())

arr = list(map(int,input().split()))
sorted_arr = sorted(set(arr))

dic={}

for i in range(len(sorted_arr)):
    dic[sorted_arr[i]]=i

for x in arr:
    print(dic[x],end=' ')

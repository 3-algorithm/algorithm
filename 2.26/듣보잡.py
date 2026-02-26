import sys
N,M = map(int,sys.stdin.readline().split())

set1 = set(sys.stdin.readline().rstrip() for _ in range(N))
set2 = set(sys.stdin.readline().rstrip() for _ in range(M))

list1 = sorted(list(set1&set2))
print(len(list1))
for i in range(len(list1)):
    print(list1[i])

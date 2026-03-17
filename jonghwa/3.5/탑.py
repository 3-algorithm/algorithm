import sys
input = sys.stdin.readline

n=int(input())
top=list(map(int,input().split()))

stack=[] #(인덱스 ,높이) 담음
result=[]

for i in range(n):
    current_height = top[i]
    while stack and stack[-1][1]<=current_height:
        stack.pop()
    
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0]+1)

    stack.append((i, current_height))
print (*(result))




n=int(input())

arr_oprator=[]
stack=[]

current=1
flag = True

#타겟으로 for문 돌리기
for _ in range(n):
    target=int(input())
    while current<=target:
        stack.append(current)
        arr_oprator.append("+")
        current+=1

    if stack[-1]==target:
        stack.pop()
        arr_oprator.append("-")
    elif stack[-1]!=target:
        flag = False

if flag :
    for i in arr_oprator:
        print(i)
else:
    print("NO")

    
        
    
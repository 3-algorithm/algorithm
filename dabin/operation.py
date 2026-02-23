import sys
sys.stdin = open("input_operation.txt")

T = 10

operations = '+-*/'

def calculate(idx):
    
    if stack[idx] not in operations:
        return float(stack[idx])
    
    l= calculate(left[idx])
    r = calculate(right[idx])
      
    if stack[idx] == '+':
        return l + r
    elif stack[idx] == '-':
        return l - r
    elif stack[idx] == '*':
        return l * r
    elif stack[idx] == '/':
        return l / r
            
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    stack = [''] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(N):
        idx, item = int(arr[i][0]), arr[i][1]
        stack[idx] = item
        
        if len(arr[i]) == 4:
            left[idx] = int(arr[i][2])
            right[idx] = int(arr[i][3])
    
    print(f"#{tc} {int(calculate(1))}")
        
            
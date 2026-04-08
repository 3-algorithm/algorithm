import sys

def solve():
    # 모든 입력을 한 번에 읽어와서 숫자로 변환
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    sequence = map(int, input_data[1:])
    
    stack = []
    result = []
    current_idx = 1
    possible = True
    
    for num in sequence:
        # 입력된 숫자(num)가 현재 넣어야 할 숫자(current_idx)보다 크거나 같으면 push
        while current_idx <= num:
            stack.append(current_idx)
            result.append("+")
            current_idx += 1
            
        # 스택의 맨 위 숫자가 목표 숫자와 같다면 pop
        if stack and stack[-1] == num:
            stack.pop()
            result.append("-")
        else:
            # 스택의 맨 위가 목표 숫자가 아니라면 수열을 만들 수 없음
            possible = False
            break
            
    if possible:
        print("\n".join(result))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
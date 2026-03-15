import sys
sys.stdin = open("input_inorder.txt")

T = 10

# 중위순회로 값 가져오는 함수
def in_order(idx):
    # 범위 벗어난 경우 종료
    if idx > N:
        return
    
    # 값 없으면 종료
    if stack[idx] == 0:
        return
    
    # 왼쪽 먼저 가져오기
    in_order(idx*2)
    
    # 자기 자신 출력
    print(stack[idx], end = '')
    
    # 오른쪽 방문
    in_order(idx*2+1)
         
# tree 값 인덱스에 맞춰 저장
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    stack = [0]*(N+1)
    for i in range(N):
        idx, item = int(arr[i][0]), arr[i][1]
        stack[idx] = item
    
    print(f"#{tc}", end = ' ')
    in_order(1)
    print()  

       
        
    
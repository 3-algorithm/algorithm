# 전역 변수 설정
n = 0
arr = []
nums = [0] * 6
visited = []

def back(at, depth):
    # 6개를 다 뽑았을 때 출력 (Java의 depth == 6 조건)
    if depth == 6:
        for i in range(6):
            print(nums[i], end=" ")
        print()
        return

    # Java의 for (int i = at; i < n; i++) 부분
    for i in range(at, n):
        if visited[i]:
            continue
            
        nums[depth] = arr[i]
        visited[i] = True
        back(i + 1, depth + 1)
        visited[i] = False

# 메인 루프 (Java의 while(true) 부분)
while True:
    line = input().split()
    n = int(line[0])
    
    if n == 0:
        break
    
    # 두 번째 숫자부터 끝까지가 arr
    arr = [int(x) for x in line[1:]]
    visited = [False] * n
    
    back(0, 0)
    print() # 각 테스트 케이스 사이 줄바꿈

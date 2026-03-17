import sys
sys.stdin = open("암호생성기.txt", "r")
from collections import deque
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    N=int(input())
    arr=deque(map(int,input().split()))

    i=0
    while True : 
        i+=1
        a = arr.popleft()
        if a-i <=0 :
            arr.append(0)
            break
        arr.append(a-i)
        if i ==5 :
            i=0
    
    print(f'#{tc}',*arr)

    # ///////////////////////////////////////////////////////////////////////////////////
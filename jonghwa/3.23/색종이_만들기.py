import sys

white=0
blue=0

#어디서 시작 & 얼마나 커 
def check_paper(x,y,n):
    global white,blue

    color = paper[x][y]
    #현재 영역이 모두 같은 색인지 검사
    for i in range(x , x+n):
        for j in range( y, y+n):
            if paper[i][j]!=color:
                half = n//2
                check_paper(x,y,half)
                check_paper(x+half,y,half)
                check_paper(x,y+half,half)
                check_paper(x+half,y+half,half)
                return

    if color == 0:
        white+=1
    else:
        blue+=1



input=sys.stdin.readline
N=int(input())
paper=[list(map(int,input().split())) for _ in range(N)]

check_paper(0,0,N)

print(white)
print(blue)


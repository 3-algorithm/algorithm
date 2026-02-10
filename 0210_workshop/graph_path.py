import sys
sys.stdin = open('graph_input.txt')

T = int(input())
# for each test
for tc in range(1, T+1):
    V, E = map(int, input().split())
    start = []
    end = []
    # 각 인풋별로 시작점, 도착점으로 나눠서 리스트에 담음
    for _ in range(E):
        s, e = map(int, input().split())
        graph = [list(map(int, input().split())) for _ in range(E)]
        
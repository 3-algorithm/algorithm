import sys
sys.stdin = open("bus_input.txt", "r")

# for each test
T = int(input())
for test_case in range(T):

    # K, N, M 인풋 받음
    # 충전기가 설치된 정류장 리스트 받음
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

   # 정류장을 표시하는 리스트 만들음
    station = [0]*N
    # 버스가 멈춘거를 표시하는 변수
    stop = 0
    bus = 0
    for i in charge:
       station[i] += 1
    print(station)

    # station리스트를 K칸 만큼 잘라서
    for j in range(0, len(station), K):
        chunk = station[bus:j+K+1]
        print(chunk)
        print(chunk[::-1].index(1))
        if 1 in chunk:
            bus = len(chunk) - 1 - chunk[::-1].index(1)
            stop += 1
        print(f'# {test_case+1} {stop}, {bus}')


    # 잘라진 리스트에 가장 멀리있는 정류장에, 버스가 멈춤
    # 버스가 멈췄다는 것을 표시

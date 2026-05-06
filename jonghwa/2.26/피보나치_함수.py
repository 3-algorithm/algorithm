T = int(input())

for _ in range(T):
    n = int(input())
    count0=[0]*41
    count1=[0]*41

    #초기화
    count0[0] = 1
    count1[0] = 0
    count0[1] = 0
    count1[1] = 1  

    for i in range(2,n+1):
        count0[i] = count0[i-1] + count0[i-2]
        count1[i] = count1[i-1] + count1[i-2]

    print(f'{count0[n]} {count1[n]}')
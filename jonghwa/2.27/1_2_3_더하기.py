T=int(input())
for _ in range(T):
    N=int(input())

    if N==1:
        print(1)
    elif N==2:
        print(2)
    elif N==3:
        #111 12 21 3
        print(4)
    else:
        #4-> 1+2+4 = 6
        #5-> 2+3+6 
        dp=[0]*(N+1)
        dp[1]=1
        dp[2]=2
        dp[3]=4

        for i in range(4,N+1):
            dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

        print(dp[N])

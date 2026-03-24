import sys
input=sys.stdin.readline

stair_tries = int(input())
stair=[int(input()) for _ in range(stair_tries)]

#1칸 뛰었으면 2칸 뛰어야함
#2칸 뛰었으면 1 or 2칸 자유

#dp[i]는 i번째 계단까지 올랐을때의 최대 점수(i번째 계단에 도착했음을 가정)
dp=[0]*stair_tries
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0]+stair[2] , stair[1]+stair[2])

#<2칸뛰거나 / 3칸 전에서 2칸뛰고 한칸 뛰거나> 두가지 케이스가 모든 상황을 커버함
if stair_tries ==1 :
    print(dp[0])
elif stair_tries ==2:
    print(dp[1])
elif stair_tries ==3:
    print(dp[2])
else:
    for i in range(3, stair_tries):
        case1 = dp[i-2] + stair[i]
        case2 = dp[i-3] + stair[i-1] + stair[i]

        dp[i] = max(case1,case2)


    print(dp[stair_tries-1])
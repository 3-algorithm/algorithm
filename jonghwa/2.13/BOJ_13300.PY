#N : 참가하는 학생수 K :최대인원수 
#S: 여0남1 Y 학년

N,K = map(int,input().split())
cnt = 0 
arr=[[0]*2 for _ in range(6)]
for i in range(N):
    S,Y = map(int,input().split())
    arr[Y-1][S]+=1
   
for i in range(2):
    for j in range(6):
        if arr[j][i]!=0:
            if arr[j][i]%K!=0:
                cnt+=arr[j][i]//K + 1
            else :
                cnt+=arr[j][i]//K

print(cnt)
            
            
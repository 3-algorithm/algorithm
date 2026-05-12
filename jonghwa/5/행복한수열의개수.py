#https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-number-of-happy-sequence/description?open=true

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer=0
# Please write your code here.
def is_happy_sequence(seq,m):
    if m==1:
        return True
    
    con_cnt =1 

    for i in range(1,len(seq)):
        if seq[i] == seq[i-1]:
            con_cnt+=1
        else :
            con_cnt=1    
        if con_cnt>=m:
            return True
    return False

for i in range(n):
    if is_happy_sequence(grid[i],m):
        answer+=1
    if is_happy_sequence([grid[row][i] for row in range(n)],m):
        answer+=1

print(answer)

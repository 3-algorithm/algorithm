import sys
sys.stdin=open("단순 2진 암호코드.txt","r")

passcode = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

tests = int(input())

for tc in range(1,tests+1):
    n,m = map(int,input().strip().split())
    arr=[input() for _ in range(n)]
#각 줄을 입력받아서 해당 줄에 1이 있는지 확인하고
#1이 존재한다면 암호코드 스캔을 위해 저장한다
#-> 코드가 존재하는 줄 찾기
    target_row = n
    for i in range(n):
        row = arr[i]
        if '1' in row:
            target_row = i 
            break
    line = arr[target_row]

#암호코드의 끝점을 찾기 위해
#뒤에서부터 하나씩 확인해서 처음으로 0이 아닌 index를 찾는다
#=> 암호코드의 끝 찾기 => 암호코드의 시작 찾기

    end_idx = m
    for i in range(m-1,-1,-1):
        if line[i] == '1':
            end_idx = i
            break
    #끝 - 시작 + 1 = 56
    start_idx =  end_idx - 56 + 1
#미리 만들어둔 해독 dict를 이용
# 암호코드를 7글자씩 잘라서 각 숫자를 해독한다
    password = []
    for i in range(start_idx,end_idx,7):
        password.append(passcode.get(line[i:i+7]))
    
    odd_sum = password[0]+password[2]+password[4]+password[6]
    even_sum = password[1]+password[3]+password[5]+password[7]

    if (odd_sum*3+even_sum)%10==0:
        res = odd_sum + even_sum
    else:
        res = 0

    print(f'#{tc} {res}')

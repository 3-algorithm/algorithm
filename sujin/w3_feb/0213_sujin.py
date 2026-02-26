# 문제: 백준 1244 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244


# 인풋 받기
switches = int(input())
lights = list(map(int, input().split()))
num_students = int(input())
students = [list(map(int, input().split())) for _ in range(num_students)]

for student in students:
    # 남자면
    # 받은 숫자의 배수인 스위치 바꾸기
    if student[0] == 1:
        for i in range(1, switches+1):
            if i%student[1] == 0:
                if lights[i-1] == 0:
                    lights[i-1] = 1
                else:
                    lights[i-1] = 0
    # 여자면
    # 받은 숫자 기준으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서
    # 다 on/off를 바꿈
    if student[0] == 2:
        if lights[student[1] - 1] == 1:
            lights[student[1] - 1] = 0
        else:
            lights[student[1] - 1] = 1
        n = 1
        while student[1] - 1 - n >= 0 and student[1] - 1 + n < switches and lights[student[1] - 1 - n] == lights[student[1] - 1 + n]:
            # 더이상 symmetric아니면 와일문 나가기

            # 인덱스 (student[1] - 1) 기준
            # 왼쪽 옆 n개가 오른쪽 옆 n개와 같은지 확인
            # 같으면 온/오프 바꾸기
                # 1이면 영으로 바꿈
                # 0이면 1로 바꿈

            if lights[student[1] - 1 - n] == 1:
                lights[student[1] - 1 - n] = 0
            elif lights[student[1] - 1 - n] == 0:
                lights[student[1] - 1 - n] = 1

            if lights[student[1] - 1 + n] == 1:
                lights[student[1] - 1 + n] = 0
            elif lights[student[1] - 1 + n] == 0:
                lights[student[1] - 1 + n] = 1
            n += 1

# 한줄에 스위치 20개씩 출력
for j in range(len(lights)):
    print(lights[j], end = " ") # 옆으로 출력
    if (j+1)%20 == 0: # 20배수인 곳에서 줄바꿈
        print()

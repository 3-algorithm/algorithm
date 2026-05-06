# 처음에 입력 받을 수
n = int(input())
# 생성된 수열의 길이와 수열을 저장할 dictionary 초기화
max_arr = {}

# 1부터 입력받은 수 까지의 정수를 두 번째 수로 지정 / 어차피 n을 넘어가면 두 수의 차가 음수가 되면서 수열이 끝나므로
for i in range(1, n):
    # 첫 요소를 첫 번째 수로 하는 배열 생성
    arr = [n]
    n_2 = i

    # 두 수의 차가 양수면 배열에 추가
    if n - n_2 > 0:
        arr.append(n_2)
    #  두 수의 차가 양수인 동안만 배열에 추가 후 인덱스 증가
    j = 0
    while arr[j] - arr[j+1] > 0:
        arr.append(arr[j] - arr[j+1])
        j += 1

    # 수열의 길이를 key로 받고 해당 key의 값을 수열로 하는 딕셔너리 추가
    key = len(arr)
    max_arr[key] = arr

    # 키 값들을 모아놓은 리스트 중 최댓값(= 최대 수열의 길이)을 max_num에 저장
    max_num = max(list(max_arr.keys()))
    # 해당 수열을 max_list에 저장
    max_list = max_arr[max_num]

print(max_num)
print(*max_list)




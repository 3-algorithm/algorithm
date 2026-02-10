# 버블 정렬:

nums = [55, 7, 78, 12, 42]
n = len(nums)

# 한번에 패스를 구현해보자
# n개의 데이터에 대해 두개씩 비교하면
# 총 n-1번 비교를 하게 됨
for i in range(n-1):    # i = 0 ~ (n-2)
    # 만약 현재 숫자(i)가 다음 숫자(i+1)보다 큰 경우
    if nums[i] > nums[i+1]:
    # 둘의 위치를 바꿈
        nums[i], nums[i+1] = nums[i+1], nums[i]

# 두번째 패스를 구현해보자
# 이제 nums의 마지막 원소는 무엇일까?
print(nums[-1]) # 78

for i in range(n-2):    # i = 0 ~ (n-2)
    # 만약 현재 숫자(i)가 다음 숫자(i+1)보다 큰 경우
    if nums[i] > nums[i+1]:
    # 둘의 위치를 바꿈
        nums[i], nums[i+1] = nums[i+1], nums[i]

# 이제 nums의 마지막 원소는 무엇일까?
print(nums[-2]) # 55

# arr: 정렬할 숫자들, n: 숫자의 갯수
def bubble_sort(arr, n):
    # 한번의 패스의 범위는
    # n-1부터 0까지 줄어든다
    for i in range(n-1, 0, -1):
        # 한번의 패스를 구현한다
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

nums = [9, 2, 421, 4567, 384, 53]
bubble_sort(nums, len(nums))
print(nums)


# 카운팅 정렬:
N = int(input())

arr = [int(input()) for _ in range(N)]
arr_clone = arr[:]
arr2 = [i for i in range(1, N+1)]
stack = []
result_char = []
result_num = []

while arr:
    a = arr.pop(0)

    i = 0
    while arr2:
        if arr2[i] <= a:
            stack.append(arr2.pop(i))
            result_char.append('+')

        else:
            break

    if stack:
        s = stack.pop()
        if s == a:
            result_char.append('-')
            result_num.append(s)

if result_num == arr_clone:
    for i in range(len(result_char)):
        print(result_char[i])
elif result_num != arr_clone:
    print('NO')
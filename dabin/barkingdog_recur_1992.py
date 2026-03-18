def press(matrix, n):
    global stack
    
    check = matrix[0][0]
    flag = True

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != check:
                flag = False
                break
        if flag == False:
            break

    if flag:

        if check == 1:
            stack.append('1')
        elif check == 0:
            stack.append('0')

        return

    a = n // 2
    stack.append('(')
    for k in range(2):
        for m in range(2):
            sub_matrix = [row[m*a : (m+1)*a] for row in matrix[k*a : (k+1)*a]]
            press(sub_matrix, a)
    stack.append(')')

N = int(input())

arr = [list(map(int, input().strip())) for _ in range(N)]

stack = []


press(arr, N)

print(''.join(stack))
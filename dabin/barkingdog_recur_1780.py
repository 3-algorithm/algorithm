def cutting(matrix, n):
    global first_count, second_count, third_count

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
        if check == -1:
            first_count += 1

        elif check == 0:
            second_count += 1
        
        elif check == 1:
            third_count += 1
            
        return
        
    size = n // 3
    for k in range(3):
        for m in range(3):
            sub_matrix = [row[m*size : (m+1)*size] for row in matrix[k*size : (k+1)*size]]
            cutting(sub_matrix, size)

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
first_count = second_count = third_count = 0

cutting(arr, N)

print(first_count)
print(second_count)
print(third_count)
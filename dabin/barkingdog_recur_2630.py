def cutting(matrix, n):
    global white_count, blue_count

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
        if check == 0:
            white_count += 1
        else:
            blue_count += 1

        return
    
    a = n // 2

    for k in range(2):
        for m in range(2):
            sub_matrix = [row[m*a : (m+1)*a] for row in matrix[k*a : (k+1)*a]]
    
            cutting(sub_matrix, a)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white_count = blue_count = 0

cutting(arr, N)

print(white_count)
print(blue_count)

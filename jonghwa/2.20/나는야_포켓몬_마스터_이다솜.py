import sys

# 입력을 빠르게 받기
input = sys.stdin.read().split()
N = int(input[0])
M = int(input[1])

name_to_id = {}
id_to_name = {}

# 데이터 채우기
for i in range(1, N + 1):
    name = input[i + 1]
    name_to_id[name] = i
    id_to_name[str(i)] = name

# 출력 처리
output = []
for j in range(N + 2, N + M + 2):
    query = input[j]
    if query.isdigit():
        output.append(id_to_name[query])
    else:
        output.append(str(name_to_id[query]))

print('\n'.join(output))
n = int(input())

cnt = 0


def hanoi(num, from_tower, to_tower, path):
    global cnt
    global s
    if num == 0:
        return path

    hanoi(num - 1, from_tower, 6 - (to_tower + from_tower), path)
    path.append(f'{from_tower} {to_tower}')
    cnt += 1
    hanoi(num - 1, 6 - (from_tower + to_tower), to_tower, path)
    return path


path = hanoi(n, 1, 3, [])

print(cnt)
for s in path:
    print(''.join(s))

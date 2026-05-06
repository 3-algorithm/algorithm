# https://www.acmicpc.net/problem/5397

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input()

    l = []
    r = []

    for i in range(len(s) - 1):
        cmd = s[i]

        if cmd == '<':
            if len(l) == 0:
                continue
            r.append(l.pop())
        elif cmd == '>':
            if len(r) == 0:
                continue
            l.append(r.pop())
        elif cmd == '-':
            if len(l) == 0:
                continue
            l.pop()
        else:
            l.append(cmd)

    while r:
        l.append(r.pop())

    print(''.join(l))

import sys
M=int(sys.stdin.readline())
S=set()
for _ in range(M):
    user_input = sys.stdin.readline().split()
    
    string=user_input[0]

    if string == "all":
        S=set(range(1,21))
    elif string == "empty":
        S=set()
    else:
        x=int(user_input[1])
        if string == "add":
            S.add(x)
        elif string == "remove":
            S.discard(x)
        elif string == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif string == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
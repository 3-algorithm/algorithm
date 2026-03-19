def hanoi_top(N, start, end, bypass):
    if N == 1:
        print(start, end)
        return
    
    hanoi_top(N-1, start, bypass, end)

    print(start, end)
    
    hanoi_top(N-1, bypass, end, start)


N = int(input())
hanoi_top(N, 1, 3, 2)
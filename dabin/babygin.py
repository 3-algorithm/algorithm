import sys
sys.stdin = open("input_babygin.txt")

def babygin(card):
    cnt = [0] * 12

    for i in range(len(card)):
        cnt[card[i]] += 1

    j = 0
    while j < 10:
        if cnt[j] >= 3:
            return True

        if cnt[j] >= 1 and cnt[j+1] >= 1 and cnt[j+2] >= 1:
            return True

        j += 1
    return False

    
T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    result = 0

    for i in range(len(cards)):
        if i%2 == 1:
            player2.append(cards[i])
            if len(player2) >= 3:
                if babygin(player2):
                    result = 2
                    break
        else:
            player1.append(cards[i])
            if len(player1) >= 3:
                if babygin(player1):
                    result = 1
                    break
        
        
    print(f"#{tc} {result}")
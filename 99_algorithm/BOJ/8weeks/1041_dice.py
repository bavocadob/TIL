dice_dict = {0: 5, 5: 0, 1: 4, 4: 1, 2: 3, 3: 2}

N = int(input())

dice = list(map(int, input().split()))
dice.pop(dice_dict[dice.index(min(dice))])

dice.sort()
ans = 0
if N > 2:
    ans += ((5 * N ** 2) - (8 * N) + 4) * dice[0]
    ans += (N - 1) * 8 * dice[1]
    ans += 4 * dice[2]
else:
    
print(ans)
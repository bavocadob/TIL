N = int(input())

dice = list(map(int, input().split()))

if N == 1:
    dice.sort()
    print(sum(dice[:5]))
else:

    min_dice = list()

    min_dice.append(min(dice[0], dice[5]))
    min_dice.append(min(dice[4], dice[1]))
    min_dice.append(min(dice[2], dice[3]))
    min_dice.sort()

    ans = 0

    ans += ((5 * N ** 2) - (8 * N) + 4) * min_dice[0]
    ans += (N - 1) * 8 * min_dice[1]
    ans += 4 * min_dice[2]

    print(ans)

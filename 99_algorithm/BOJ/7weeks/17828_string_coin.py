def solution(length, money):
    result = [None] * length

    for i in range(length - 1, -1, -1):
        # print(result)
        # print(money, i)
        if (money - i) == 0:
            result[i] = 'A'
            money -= 1
        else:
            if (money - i) // 26:
                result[i] = 'Z'
                money -= 26
            else:
                result[i] = chr(ord('A') + (money - i) - 1)
                money -= (money - i)

    print(''.join(result))


N, X = map(int, input().split())

if N * 26 < X or N > X:
    print('!')
else:
    solution(N, X)

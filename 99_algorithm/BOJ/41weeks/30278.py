def max_profit(S, A, a, B, b):
    max_profit = 0

    max_x = S // A
    for x in range(max_x + 1):
        remaining_money = S - (x * A)
        max_y = remaining_money // B
        profit = (x * a) + (max_y * b)

        max_profit = max(max_profit, profit)

    return max_profit


S = int(input())
A, a = map(int, input().split())
B, b = map(int, input().split())

print(max_profit(S, A, a, B, b))

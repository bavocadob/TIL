def solve(x, k):
    current_ones = bin(x).count('1')

    if current_ones == k:
        return 0

    y = 0

    if current_ones > k:
        while bin(x + y).count('1') > k:
            lowest_one = (x + y) & -(x + y)
            y += lowest_one

    while bin(x + y).count('1') < k:
        bit_position = 0
        while (x + y) & (1 << bit_position):
            bit_position += 1

        y += (1 << bit_position)

    return y


N = int(input())
K = int(input())
print(solve(N, K))

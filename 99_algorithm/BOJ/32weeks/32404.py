def solve(N):
    p = [0] * N
    half = N // 2

    odd_numbers = list(range(half + 1, N + 1))

    even_numbers = list(range(half, 0, -1))

    odd_idx, even_idx = 0, 0
    for i in range(N):
        if (i + 1) % 2 == 1:
            p[i] = odd_numbers[odd_idx]
            odd_idx += 1
        else:
            p[i] = even_numbers[even_idx]
            even_idx += 1

    return p


n = int(input())
rst = solve(n)
print(*rst)

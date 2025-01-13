def solve(n):
    if n == 0:
        return 1, 1
    if n in {1, 2, 4}:
        return None

    if n % 2 == 1:
        x = (n + 1) // 2
        y = (n - 1) // 2
        return x, y

    if n % 4 == 0:
        half_n = n // 2
        x = (half_n + 2) // 2
        y = (half_n - 2) // 2
        return x, y

    return None


N = int(input())

ans = solve(N)

if ans is None:
    print('No')
else:
    print('Yes')
    print(*ans)
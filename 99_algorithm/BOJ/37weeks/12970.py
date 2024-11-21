def solve():
    if (N // 2) * (N - (N // 2)) < K:
        print(-1)
        return

    for size, a, b in check:
        if size >= K:
            break

    rst = ['B'] * (N - (a + b)) + ['A'] * a + ['B'] * b
    gap = size - K
    last_a = -b - 1

    rst[last_a], rst[last_a + gap] = rst[last_a + gap], rst[last_a]
    print(''.join(rst))


N, K = map(int, input().split())
check = []

for i in range(1, 50):
    check.append((i * i, i, i))
    check.append((i * (i + 1), i + 1, i))

solve()

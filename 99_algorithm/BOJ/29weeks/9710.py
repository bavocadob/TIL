T = int(input())

for t in range(1, T + 1):

    N = int(input())

    X = []
    Y = []

    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    X.sort()
    Y.sort()

    ans = 0
    for i in range(N):
        ans += abs((i + 1) - X[i])
        ans += abs((i + 1) - Y[i])

    print(f'Case #{t}: {ans}')

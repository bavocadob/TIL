def solve():
    if N == 1:
        print(1)
        return

    if N % 2:
        print(-1)
        return

    print(N, end=' ')
    for i in range(1, N):
        if i % 2:
            print(i, end=' ')
        else:
            print(N - i, end=' ')


N = int(input())
solve()
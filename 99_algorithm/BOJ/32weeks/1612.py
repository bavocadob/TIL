def solve(n):
    if not (n % 2 and n % 5):
        print(-1)
        return

    j = 0
    for i in range(1, n + 1):
        j = (10 * j + 1) % n
        if j == 0:
            print(i)
            break


N = int(input())
solve(N)

def solve():
    n, x = map(int, input().split())

    cnt = bin(n).count('1')
    if x > cnt:
        print(-1)
        return

    if x == 1:
        print(0)
        return

    ans = []
    for i in range(60, -1, -1):
        if n & (1 << i):
            n ^= (1 << i)
            ans.append(n)
            x -= 1
            if x <= 1:
                break

    print(*ans, 0)


solve()

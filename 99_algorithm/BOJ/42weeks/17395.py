def solve():
    n, x = map(int, input().split())
    ans = []
    for i in range(60, -1, -1):
        if n & (1 << i):
            n ^= (1 << i)
            ans.append(n)
            x -= 1
            if x == 1:
                print(*ans, 0)
                return
    print(-1)


solve()

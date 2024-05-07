import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    loc = [0] + list(map(int, input().split()))
    fan = [0] + list(map(int, input().split()))

    pre = [0] * (N + 1)
    for i in range(1, N + 1):
        pre[i] = fan[i] + pre[i - 1]

    s = sum((loc[i] - loc[1]) * fan[i] for i in range(1, N + 1))
    ans = loc[1]
    for i in range(2, N + 1):
        cur = s + (pre[i - 1] * 2 - pre[N]) * (loc[i] - loc[i - 1])
        if s > cur:
            s = cur
            ans = loc[i]

    print(ans)

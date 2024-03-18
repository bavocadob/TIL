import sys

input = sys.stdin.readline

T = int(input())

dp = [False] * 1_000_001

for i in range(1, 1000001):
    for j in range(1, 1001):
        if j ** 2 > i:
            break

        if not dp[i - j ** 2]:
            dp[i] = True
            break

for _ in range(T):
    N = int(input())

    if dp[N]:
        print('koosaga')
    else:
        print('cubelover')

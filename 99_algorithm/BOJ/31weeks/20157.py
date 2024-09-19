import math
import sys
from collections import defaultdict

input = sys.stdin.readline


def normalize_slope(dy, dx):
    if dx == 0:
        return (1, 0) if dy > 0 else (-1, 0)
    if dy == 0:
        return (0, 1) if dx > 0 else (0, -1)

    g = math.gcd(dy, dx)
    dy //= g
    dx //= g

    return dy, dx


N = int(input())

dp = defaultdict(int)
ans = 0
for _ in range(N):
    x, y = map(int, input().split())

    slope = normalize_slope(y, x)

    dp[slope] += 1
    ans = max(ans, dp[slope])

print(ans)

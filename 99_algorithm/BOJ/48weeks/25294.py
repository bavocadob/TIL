import sys


def solve(n, a, b, c, d):
    ans = int(1e18)

    if b * c > d * a:
        a, c = c, a
        b, d = d, b

    for i in range(a):
        left = n - i * c
        cnt = (left - 1) // a + 1 if left > 0 else 0
        ans = min(ans, cnt * b + i * d)

    return ans


input = sys.stdin.readline
N, A, B, C, D = map(int, input().split())
print(solve(N, A, B, C, D))

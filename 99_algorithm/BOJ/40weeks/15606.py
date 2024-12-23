import sys

input = sys.stdin.readline


def solve(a, b, c, d):
    a, b = max(a, b), min(a, b)
    a, c = max(a, c), min(a, c)
    b, c = max(b, c), min(b, c)

    ans = a * a + b * b + c * c

    for i in range(c, c + min(d + 1, 4)):

        x = max(0, i - a) + max(0, i - b) + max(0, i - c)

        if x > d:
            break

        ans = max(
            ans,
            7 * i + (max(a, i) + d - x) ** 2 + max(b, i) ** 2 + max(c, i) ** 2
        )

    return ans


N = int(input())

for _ in range(N):
    a1, b1, c1, d1 = map(int, input().split())
    print(solve(a1, b1, c1, d1))

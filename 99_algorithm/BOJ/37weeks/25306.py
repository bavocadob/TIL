import sys


def solve(n):
    m = n % 4
    if m == 0:
        return n
    elif m == 1:
        return 1
    elif m == 2:
        return n + 1
    else:
        return 0


input = sys.stdin.readline

A, B = map(int, input().split())
ans = solve(A - 1) ^ solve(B)
print(ans)

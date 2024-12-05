import sys

input = sys.stdin.readline
MOD = 1000000007


def solve(x, y):
    if y <= 0:
        return 1
    elif y % 2 == 0:
        tmp = solve(x, y // 2)
        return (tmp * tmp) % MOD
    else:
        tmp = solve(x, y // 2)
        return (tmp * tmp * x) % MOD


T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(2, N - 2))

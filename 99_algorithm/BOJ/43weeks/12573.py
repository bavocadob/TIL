import math


def solve(l, p, c):
    ans = 0
    while True:
        if l * math.pow(c, math.pow(2, ans)) >= p:
            return ans
        ans += 1


T = int(input())

for t in range(1, T + 1):
    L, P, C = map(int, input().split())
    rst = solve(L, P, C)
    print(f"Case #{t}: {rst}")

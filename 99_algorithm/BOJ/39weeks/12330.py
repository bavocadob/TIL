import sys

input = sys.stdin.readline


def check(r, t, x):
    return t >= (x + 1) * (2 * r + 2 * x + 1)


def solve(r, t):
    low, high = 0, t
    while low < high:
        mid = (low + high + 1) // 2
        if check(r, t, mid):
            low = mid
        else:
            high = mid - 1
    return low + 1


T = int(input())
for cnt in range(1, T + 1):
    R, T = map(int, input().split())
    result = solve(R, T)
    print(f"Case #{cnt}: {result}")

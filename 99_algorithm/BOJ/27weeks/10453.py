import sys

input = sys.stdin.readline


def solve(a, b):
    len_a, len_b = len(a), len(b)

    if len_a != len_b:
        print("-1")
        return

    ans = 0
    idx_a = 0
    idx_b = 0

    while True:
        while idx_a < len_a and a[idx_a] == 'a':
            idx_a += 1
        while idx_b < len_b and b[idx_b] == 'a':
            idx_b += 1
        if idx_a >= len_a or idx_b >= len_b:
            break
        ans += abs(idx_a - idx_b)
        idx_a += 1
        idx_b += 1

    print(ans)


T = int(input())
for _ in range(T):
    A, B = input().rstrip().split()
    solve(A, B)

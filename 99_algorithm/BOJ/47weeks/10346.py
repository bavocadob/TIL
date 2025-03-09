import sys

input = sys.stdin.readline


def solve(t, p, q):
    if q == 1:
        print(t, f"1/{p + 1}")
    else:
        cnt = p // q
        p = p % q
        q -= p
        p += q
        q += p * cnt

        print(t, f"{p}/{q}")


P = int(input())
for i in range(1, P + 1):
    _, temp = input().split()

    solve(i, *tuple(map(int, temp.split('/'))))

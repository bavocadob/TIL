import sys

input = sys.stdin.readline


def solve(n):
    candidate = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i != 0:
            continue
        diff = i
        total = n // i
        if (total + diff) % 2 != 0:
            continue
        r = (total + diff) // 2
        l = r - diff
        candidate.append((l, r))

    if not candidate:
        return None

    candidate.sort()

    return candidate[0]


T = int(input())

for _ in range(T):
    N = int(input())
    ans = solve(N)
    if ans is None:
        print("IMPOSSIBLE")
    else:
        print(*ans)

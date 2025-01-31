import sys

input = sys.stdin.readline


def solve():
    R, C = map(int, input().split())
    odd = 0
    even = 0

    for i in range(R):
        row = list(map(int, input().split()))
        for j in range(C):
            if (i + j) % 2 == 0:
                even += row[j]
            else:
                odd += row[j]

    return "YES" if odd == even else "NO"


T = int(input())

for t in range(1, T + 1):
    print(f'Case #{t}: {solve()}\n')

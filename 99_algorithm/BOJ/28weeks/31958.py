import sys

input = sys.stdin.readline


def solve():
    curr = 0
    for i in range(1, N + 1):
        size = int(input())

        if curr + i * (size - 1) >= P:
            return i - 1

        curr += size
    return N


N, P = map(int, input().split())

print(solve())

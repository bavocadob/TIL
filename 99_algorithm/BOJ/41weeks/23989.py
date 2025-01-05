import sys

input = sys.stdin.readline
T = int(input())
MOD = 1_000_000_007

for x in range(1, T + 1):
    R, C = map(int, input().split())
    low, high = min(R, C), max(R, C)
    total_squares = (low * (low - 1) * (low + 1) * (2 * high - low) // 12)
    print(f"Case #{x}: {total_squares % MOD}")

import math
import sys

input = sys.stdin.readline


def solve(l1, l2):
    H = math.sqrt(l1 ** 2 + l2 ** 2)
    R = (l1 + l2 - H) / 2
    S_triangle = (l1 * l2) / 2
    sum_circle_areas = math.pi * R ** 2 / (1 - (1 - 2 * R / (R + math.sqrt(R ** 2 + (l2 - R) ** 2))) ** 2)

    return sum_circle_areas / S_triangle


N = int(input())
for T in range(1, N + 1):
    L1, L2 = map(int, input().split())
    result = solve(L1, L2)
    print(f"Case #{T}: {result:.4f}\n")

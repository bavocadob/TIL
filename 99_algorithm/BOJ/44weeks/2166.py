import sys

input = sys.stdin.readline


def solve():
    n = len(points)
    area = 0

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += (x1 * y2) - (y1 * x2)

    return round(abs(area) / 2, 1)


N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

print(solve())

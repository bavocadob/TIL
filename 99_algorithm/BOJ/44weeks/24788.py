import math
import sys

input = sys.stdin.readline


def get_area(p):
    n = len(p)
    area = 0

    for i in range(n):
        x1, y1 = p[i]
        x2, y2 = p[(i + 1) % n]
        area += (x1 * y2) - (y1 * x2)

    return round(abs(area) / 2, 1)


N = int(input())
points = [tuple(map(float, input().split())) for _ in range(N)]

min_x, min_y = float('inf'), float('inf')
for x, y in points:
    min_x = min(x, min_x)
    min_y = min(y, min_y)

for i in range(N):
    points[i] = (points[i][0] - min_x, points[i][1] - min_y)

original_area = get_area(points)

A = int(input())

scale_factor = math.sqrt(A / original_area)

scaled_points = [(x * scale_factor, y * scale_factor) for x, y in points]

for x, y in scaled_points:
    print(x, y)

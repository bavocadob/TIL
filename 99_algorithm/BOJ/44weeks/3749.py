import sys

input = sys.stdin.readline


def solve(points):
    n = len(points)
    area = 0

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += (x1 * y2) - (y1 * x2)

    return round(abs(area) / 2, 1)


while True:
    line = input().strip()

    p = []
    try:
        K = int(line)
        while len(p) != K:
            temp = list(map(float, input().split()))

            for i in range(len(temp) // 2):
                x, y = temp[i * 2], temp[i * 2 + 1]
                p.append((x, y))
    except ValueError:
        K, *dots = map(float, line.split())

        K = int(K)

        for i in range(K):
            x, y = dots[i * 2], dots[i * 2 + 1]
            p.append((x, y))

        while len(p) != K:
            temp = list(map(float, input().split()))

            for i in range(len(temp) // 2):
                x, y = temp[i * 2], temp[i * 2 + 1]
                p.append((x, y))

    if K == 0:
        break

    print(round(solve(p)))

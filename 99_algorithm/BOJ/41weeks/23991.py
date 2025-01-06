import sys

input = sys.stdin.readline


def check_corner(x, y, z, r, edge, x_min, y_min, z_min, x_max, y_max, z_max, corner_type):
    for k in range(len(x)):
        if corner_type == "left_bottom":
            if ((x[k] + r[k] > x_min + edge or y[k] + r[k] > y_min + edge or z[k] + r[k] > z_min + edge) and
                    (x[k] - r[k] < x_max - edge or y[k] - r[k] < y_max - edge or z[k] - r[k] < z_max - edge)):
                return False
        elif corner_type == "right_bottom":
            if ((x[k] - r[k] < x_max - edge or y[k] + r[k] > y_min + edge or z[k] + r[k] > z_min + edge) and
                    (x[k] + r[k] > x_min + edge or y[k] - r[k] < y_max - edge or z[k] - r[k] < z_max - edge)):
                return False
        elif corner_type == "left_top":
            if ((x[k] + r[k] > x_min + edge or y[k] - r[k] < y_max - edge or z[k] + r[k] > z_min + edge) and
                    (x[k] - r[k] < x_max - edge or y[k] + r[k] > y_min + edge or z[k] - r[k] < z_max - edge)):
                return False
        elif corner_type == "right_top":
            if ((x[k] - r[k] < x_max - edge or y[k] - r[k] < y_max - edge or z[k] + r[k] > z_min + edge) and
                    (x[k] + r[k] > x_min + edge or y[k] + r[k] > y_min + edge or z[k] - r[k] < z_max - edge)):
                return False
    return True


def solve():
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]
    x, y, z, r = zip(*coordinates)

    x_min = min(x[i] - r[i] for i in range(N))
    x_max = max(x[i] + r[i] for i in range(N))
    y_min = min(y[i] - r[i] for i in range(N))
    y_max = max(y[i] + r[i] for i in range(N))
    z_min = min(z[i] - r[i] for i in range(N))
    z_max = max(z[i] + r[i] for i in range(N))

    left, right = 0, max(x_max - x_min, y_max - y_min, z_max - z_min)

    while right - left > 1:
        mid = (right + left) // 2
        if (check_corner(x, y, z, r, mid, x_min, y_min, z_min, x_max, y_max, z_max, "left_bottom") or
                check_corner(x, y, z, r, mid, x_min, y_min, z_min, x_max, y_max, z_max, "left_top") or
                check_corner(x, y, z, r, mid, x_min, y_min, z_min, x_max, y_max, z_max, "right_bottom") or
                check_corner(x, y, z, r, mid, x_min, y_min, z_min, x_max, y_max, z_max, "right_top")):
            right = mid
        else:
            left = mid

    return right


T = int(input())
for t in range(1, T + 1):
    ans = solve()
    print(f'Case #{t}: {ans}')

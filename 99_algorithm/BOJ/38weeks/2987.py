import sys

input = sys.stdin.readline


def get_ccw(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
            - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1]))


A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

n = int(input())

additional_points = [tuple(map(int, input().split())) for _ in range(n)]

area = get_ccw(A, B, C)
total_area = abs(area) / 2
ans = 0

for point in additional_points:
    if area < 0:
        if (abs(get_ccw(A, point, B)) > -area or get_ccw(A, point, B) < 0 or
                abs(get_ccw(B, point, C)) > -area or get_ccw(B, point, C) < 0 or
                abs(get_ccw(C, point, A)) > -area or get_ccw(C, point, A) < 0):
            continue
    else:
        if (abs(get_ccw(A, point, B)) > area or get_ccw(A, point, B) > 0 or
                abs(get_ccw(B, point, C)) > area or get_ccw(B, point, C) > 0 or
                abs(get_ccw(C, point, A)) > area or get_ccw(C, point, A) > 0):
            continue
    ans += 1

print(f"{total_area:.1f}")
print(ans)

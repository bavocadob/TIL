import math
import sys


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


input = sys.stdin.readline
temp = list(map(int, input().split()))

a = temp[:3]
b = temp[3:6]
c = temp[6:9]

s = a
e = b
cnt = 0

while not math.isclose(s[0], e[0], rel_tol=1e-9) or \
        not math.isclose(s[1], e[1], rel_tol=1e-9) or \
        not math.isclose(s[2], e[2], rel_tol=1e-9):
    cnt += 1
    if cnt == 100_000:
        break

    mid = [(s[i] + e[i]) / 2 for i in range(3)]

    if distance(s, c) < distance(e, c):
        e = mid
    else:
        s = mid

result = round(distance(s, c), 10)
print(f"{result:.10f}")

import sys

input = sys.stdin.readline


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


p = 25
circles = []

n = int(input())

for i in range(n):
    x, y, r = map(int, input().split())
    x *= p
    y *= p
    r *= p
    circles.append(Circle(x, y, r))

ans = 0
for i in range(-10 * p, 21 * p):
    for j in range(-10 * p, 21 * p):
        for circle in circles:
            dis = (i - circle.x) ** 2 + (j - circle.y) ** 2
            if dis <= circle.r * circle.r:
                ans += 1
                break

print(ans / (p * p))

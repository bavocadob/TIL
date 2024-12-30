import math
import sys

input = sys.stdin.readline

R = int(input().strip())
y = R - 1
x = int(math.sqrt(2 * R - 1))
print(x - 1 if x * x + y * y == R * R else x, y)

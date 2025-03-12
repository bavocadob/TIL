import math


N = int(input())
cylinders = list(map(float, input().split()))

positions = [0.0] * N

positions[0] = cylinders[0]
width = cylinders[0] * 2.0

for i in range(1, N):
    max_x = cylinders[i]
    for j in range(i):
        max_x = max(max_x, positions[j] + math.sqrt(4 * cylinders[i] * cylinders[j]))
    positions[i] = max_x
    width = max(width, positions[i] + cylinders[i])

print(f"{width:.9f}")

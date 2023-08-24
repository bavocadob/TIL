N, M = map(int, input().split())

heights = list(map(int, input().split()))

rain = 0

for i in range(1, M - 1):
    left = 0
    right = 0
    for j in range(i - 1, -1, -1):
        left = max(left, heights[j])
    for j in range(i + 1, M):
        right = max(right, heights[j])
    target = min(left, right)
    if target > heights[i]:
        rain += target - heights[i]

print(rain)


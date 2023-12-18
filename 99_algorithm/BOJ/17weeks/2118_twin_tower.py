import sys

input = sys.stdin.readline

N = int(input())

towers = []

distance = 0
for _ in range(N):
    dist = int(input())

    distance += dist
    towers.append(dist)

left = 0
right = 0

left_dist = 0
ans = 0

while True:
    right_dist = distance - left_dist
    if right_dist > left_dist:
        if right == N:
            break
        left_dist += towers[right]
        right += 1
    elif left_dist > right_dist:
        if left == N:
            break
        left_dist -= towers[left]
        left += 1
    elif left_dist == right_dist:
        ans = left_dist
        break

    right_dist = distance - left_dist
    ans = max(ans, min(left_dist, right_dist))

print(ans)

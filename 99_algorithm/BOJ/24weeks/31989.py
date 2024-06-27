import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pos = [0] + list(map(int, input().split()))

box = []

for _ in range(M):
    target, weight = map(int, input().split())
    box.append((target, weight))

box.sort()

ans = 0
start_pos = pos[N + 1]

if box[0][0] < N + 1:
    ans += (start_pos - pos[box[0][0]]) * 2

if box[-1][0] > N + 1:
    ans += (pos[box[-1][0]] - start_pos) * 2

for target, weight in box:
    ans += weight * abs(start_pos - pos[target])

print(ans)

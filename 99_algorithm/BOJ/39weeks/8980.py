import sys

input = sys.stdin.readline
N, C = map(int, input().split())
M = int(input())

boxes = []

for _ in range(M):
    s, e, v = map(int, input().split())
    boxes.append((s, e, v))

boxes.sort(key=lambda x: (x[1]))
# print(boxes)

ans = 0
weights = [C] * N
for s, e, v in boxes:
    temp = v
    for i in range(s, e):
        temp = min(temp, weights[i])

    for i in range(s, e):
        weights[i] -= temp

    ans += temp

print(ans)

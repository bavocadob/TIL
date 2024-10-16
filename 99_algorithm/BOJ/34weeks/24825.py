import heapq
import sys

input = sys.stdin.readline
H, C = map(int, input().split())

coworkers = []

queue = []
ans = 0
for _ in range(C):
    a, d = map(int, input().split())
    ans = max(a, ans)
    heapq.heappush(queue, (a + d, d))

cnt = 0
while cnt < H:
    cnt += 1

    curr, gap = heapq.heappop(queue)
    ans = max(ans, curr)
    heapq.heappush(queue, (curr + gap, gap))

print(ans)

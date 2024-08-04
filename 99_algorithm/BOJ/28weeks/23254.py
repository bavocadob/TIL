import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

time = N * 24

score = list(map(int, input().split()))

increase = list(map(int, input().split()))

queue = []

ans = 0

for i in range(M):
    s = score[i]
    incr = increase[i]
    temp = incr if s + incr <= 100 else 100 - s

    heapq.heappush(queue, (-temp, i))
    ans += s

while queue and time > 0:
    incr, idx = heapq.heappop(queue)

    incr = -incr

    if incr == 0:
        break

    max_time = (100 - score[idx]) // incr
    mod = (100 - score[idx]) % incr

    spend_time = min(max_time, time)

    time -= spend_time
    ans += spend_time * incr
    score[idx] += spend_time * incr

    if time == 0:
        break

    heapq.heappush(queue, (-mod, idx))

print(ans)
import heapq
import sys

input = sys.stdin.readline

N = int(input())
T = []
D = []

for _ in range(N):
    code, val = input().split()
    val = float(val)

    if code == 'T':
        heapq.heappush(T, val)
    else:
        heapq.heappush(D, val)

speed = 1
curr = 0
ans = 0

while T or D:
    if not T:
        d = heapq.heappop(D)
        ans += (d - curr) * speed
        curr = d
    elif not D:
        t = heapq.heappop(T)
        curr += (t - ans) * (1 / speed)
        ans = t
    else:
        d = D[0]
        t = T[0]
        if ans + (d - curr) * speed <= t:
            ans += (d - curr) * speed
            curr = d
            heapq.heappop(D)
        else:
            curr += (t - ans) * (1 / speed)
            ans = t
            heapq.heappop(T)

    speed += 1

ans += (1000 - curr) * speed
print(round(ans))

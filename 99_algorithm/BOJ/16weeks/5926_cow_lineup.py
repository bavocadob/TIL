import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

cows = []
cow_set = set()

for _ in range(N):
    x, idx = map(int, input().split())
    cows.append((x, idx))
    cow_set.add(idx)

cows.sort()
K = len(cow_set)
del cow_set

cow_dict = defaultdict(int)

left = 0
right = 0
cnt = 0

ans = cows[-1][0] - cows[0][0]

while left < N and right < N:
    while cnt < K and right < N:
        if not cow_dict[cows[right][1]]:
            cnt += 1
        cow_dict[cows[right][1]] += 1
        right += 1

    while cnt >= K:
        ans = min(ans, cows[right - 1][0] - cows[left][0])
        cow_dict[cows[left][1]] -= 1
        if not cow_dict[cows[left][1]]:
            cnt -= 1
        left += 1
print(ans)

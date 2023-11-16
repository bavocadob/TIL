import sys

input = sys.stdin.readline

N, K = map(int, input().split())

cnt = [0] * 1_000_001

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(a, b):
        cnt[i] += 1

left = right = 0
curr = 0
while right < 1_000_001:
    if curr > K:
        curr -= cnt[left]
        left += 1
    elif curr < K:
        curr += cnt[right]
        right += 1
    else:
        print(left, right)
        break
else:
    print(0, 0)

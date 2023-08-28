import sys
input = sys.stdin.readline

N, L = map(int, input().split())

pools = [list(map(int, input().split())) for _ in range(N)]

pools.sort()

curr = 0
ans = 0

for left, right in pools:
    if curr > left:
        log = (right - curr) // L

        if (right - curr) % L:
            log += 1
        ans += log
        curr += log * L
    else:
        log = (right - left) // L
        if (right - left) % L:
            log += 1
        ans += log
        curr = left + log * L

print(ans)

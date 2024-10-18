import sys
from collections import deque

input = sys.stdin.readline


def solve():
    P, N = map(int, input().split())

    friends = list(map(int, input().split()))
    rst = [0] * N
    gap = []

    s = 0
    base = P // N
    for i in range(N):
        pay = min(base, friends[i])
        rst[i] = pay
        s += pay
        if friends[i] > base:
            gap.append(((friends[i] - base), i))

    if P > sum(friends):
        print('IMPOSSIBLE')
        return
    elif P == s:
        print(*rst)
        return

    gap.sort(key=lambda x: (-x[0], x[1]))
    queue = deque(gap)
    while queue and s < P:
        target = (P - s) // len(queue)
        for g, _ in queue:
            target = min(target, g)
        if target:
            temp_queue = deque()
            while queue:
                gg, idx = queue.popleft()
                s += target
                rst[idx] += target
                if gg > target:
                    temp_queue.append(((gg - target), idx))
            queue = temp_queue
            continue

        s += 1
        idx = queue.popleft()[1]
        rst[idx] += 1
        if rst[idx] < friends[idx]:
            queue.append((friends[idx] - rst[idx], idx))
    print(*rst)


T = int(input())

for _ in range(T):
    solve()

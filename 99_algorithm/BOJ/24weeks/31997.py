import heapq
import sys

input = sys.stdin.readline

N, M, T = map(int, input().split())

joined = [False] * (N + 1)
queue = []
member = []
adj = [list() for _ in range(N + 1)]

for i in range(1, N + 1):
    start, end = map(int, input().split())
    queue.append((start, end, i))

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

queue.sort()

queue_idx = 0

ans = 0

for time in range(T):
    while queue_idx < N and queue[queue_idx][0] <= time:
        start, end, people_idx = queue[queue_idx]
        queue_idx += 1

        heapq.heappush(member, (end, people_idx))
        joined[people_idx] = True
        for friend in adj[people_idx]:
            if joined[friend]:
                ans += 1

    print(ans)

    while member and member[0][0] <= time + 1:
        _, people_idx = heapq.heappop(member)
        joined[people_idx] = False

        for friend in adj[people_idx]:
            if joined[friend]:
                ans -= 1

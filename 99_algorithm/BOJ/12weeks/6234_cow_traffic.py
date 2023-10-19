import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dp = [0] * (N + 1)
reverse_dp = [0] * (N + 1)
adj = [list() for _ in range(N + 1)]
reverse_adj = [list() for _ in range(N + 1)]

parents = [0] * (N + 1)
reverse_parents = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    parents[b] += 1
    reverse_parents[a] += 1

    adj[a].append(b)
    reverse_adj[b].append(a)

queue = deque()

for i in range(1, N):
    if parents[i] == 0:
        queue.append(i)
        dp[i] = 1

while queue:
    curr_node = queue.popleft()

    for next_node in adj[curr_node]:
        dp[next_node] += dp[curr_node]
        parents[next_node] -= 1

        if not parents[next_node]:
            queue.append(next_node)

queue.append(N)
reverse_dp[N] = 1

while queue:
    curr_node = queue.popleft()

    for next_node in reverse_adj[curr_node]:
        reverse_dp[next_node] += reverse_dp[curr_node]
        reverse_parents[next_node] -= 1

        if not reverse_parents[next_node]:
            queue.append(next_node)

ans = 0

for i in range(1, N + 1):
    for j in adj[i]:
        ans = max(ans, dp[i] * reverse_dp[j])

# print(dp)
# print(reverse_dp)
print(ans)

# print(dp)

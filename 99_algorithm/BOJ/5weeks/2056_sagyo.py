import sys

from collections import deque

input = sys.stdin.readline

N = int(input())

dp = [0] * N

connection = [list() for _ in range(N)]

cost = [0] * N
parent_cnt = [0] * N

for i in range(N):
    c, n, *parent = map(int, input().split())
    cost[i] = c
    parent_cnt[i] = n
    for p in parent:
        connection[p - 1].append(i)

queue = deque()

for i in range(N):
    if parent_cnt[i] == 0:
        queue.append(i)
        dp[i] = cost[i]

# print('부모개수', parent_cnt)
cnt = 1
while queue:
    node = queue.popleft()
    # print('현재노드', node,'방문순서', cnt)
    cnt += 1
    for next_node in connection[node]:
        parent_cnt[next_node] -= 1
        dp[next_node] = max(dp[next_node], dp[node] + cost[next_node])
        if parent_cnt[next_node] == 0:
            queue.append(next_node)
# print('부모개수', parent_cnt)
print(max(dp))

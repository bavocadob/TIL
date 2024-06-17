import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, D = map(int, input().split())

parents = dict()

for _ in range(N):
    name, cnt = input().split()
    cnt = int(cnt)
    parents[name] = cnt

adj = defaultdict(list)

for _ in range(M):
    a, b = input().split()

    adj[a].append(b)
    adj[b].append(a)

visited = defaultdict(int)

start = input().rstrip()

queue = deque([start])
visited[start] = 0

ans = set()
while queue:
    node = queue.popleft()
    if visited[node] == D:
        continue

    for next_node in adj[node]:

        ans.add(next_node)
        parents[next_node] -= 1
        if parents[next_node] == 0:
            visited[next_node] = visited[node] + 1
            queue.append(next_node)

if start in ans:
    ans.remove(start)

print(len(ans))

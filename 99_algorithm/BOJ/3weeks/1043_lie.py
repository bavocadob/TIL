from collections import deque


def build_graph(edges):
    for edge in edges:
        u, v = edge
        graph[u].add(v)
        graph[v].add(u)


N, M = map(int, input().split())

graph = {i: set() for i in range(1, N + 1)}

num, *truth = list(map(int, input().split()))

parties = []

for i in range(M):
    num, *member = list(map(int, input().split()))
    edges = [(member[i], member[i + 1]) for i in range(len(member) - 1)]
    build_graph(edges)
    parties.append(member)

visited = [False] * (N + 1)

for t in truth:
    visited[t] = True
    queue = deque([t])
    while queue:
        curr = queue.popleft()
        for tt in graph[curr]:
            if not visited[tt]:
                visited[tt] = True
                queue.append(tt)

cnt = 0
for party in parties:
    can_lie = True
    for party_member in party:
        if visited[party_member]:
            can_lie = False
            break
    cnt += int(can_lie)

print(cnt)

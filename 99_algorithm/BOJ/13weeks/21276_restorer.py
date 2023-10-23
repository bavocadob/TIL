import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())

villagers = input().split()
villagers.sort()
adj = defaultdict(list)
parents = defaultdict(int)

M = int(input())

for _ in range(M):
    a, b = input().split()

    adj[b].append(a)
    parents[a] += 1

roots = []
queue = deque()

child_dict = dict()

for villager in villagers:
    if villager not in parents:
        queue.append(villager)
        roots.append(villager)
    child_dict[villager] = list()

while queue:
    now = queue.popleft()

    for next_node in adj[now]:
        parents[next_node] -= 1
        if not parents[next_node]:
            queue.append(next_node)
            child_dict[now].append(next_node)

print(len(roots))
print(*sorted(roots))

for key, value in child_dict.items():
    print(key, len(value), *sorted(value))

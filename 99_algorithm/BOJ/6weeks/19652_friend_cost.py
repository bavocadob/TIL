import sys

input = sys.stdin.readline


def find(node):
    if parent_dict[node] == node:
        return node

    parent_dict[node] = find(parent_dict[node])
    return parent_dict[node]


def union(a, b):
    a_parent, b_parent = find(a), find(b)

    if a_parent == b_parent:
        return

    if cost[a_parent] < cost[b_parent]:
        parent_dict[b_parent] = parent_dict[a_parent]
    elif cost[a_parent] == cost[b_parent]:
        a_parent, b_parent = min(a_parent, b_parent), max(a_parent, b_parent)
        parent_dict[b_parent] = parent_dict[a_parent]
    else:
        parent_dict[a_parent] = parent_dict[b_parent]


N, M, k = map(int, input().split())

cost = [0] + list(map(int, input().split()))

parent_dict = {i: i for i in range(1, N + 1)}

for _ in range(M):
    x, y = map(int, input().split())

    union(x, y)

visited = set()

result = 0
for i in range(1, N + 1):
    if find(i) not in visited:
        visited.add(parent_dict[i])
        result += cost[parent_dict[i]]

if result <= k:
    print(result)
else:
    print('Oh no')

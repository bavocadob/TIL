from collections import defaultdict

import sys

input = sys.stdin.readline


def dfs(node, val):
    global max_distance, max_index
    if val > max_distance:
        max_distance = val
        max_index = node

    for next_node, distance in connection[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, val + distance)


connection = defaultdict(list)
head = 0
while True:
    try:
        x, y, d = map(int, input().split())
        connection[x].append((y, d))
        connection[y].append((x, d))
        if len(connection[x]) > len(connection[head]):
            head = x

        if len(connection[y]) > len(connection[head]):
            head = y

    except:
        break

max_distance = 0
max_index = -1
visited = [False] * (10001)
visited[head] = True
dfs(head, 0)

max_distance = 0
visited = [False] * (10001)
visited[max_index] = True
dfs(max_index, 0)
print(max_distance)

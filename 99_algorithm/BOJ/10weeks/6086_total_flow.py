import sys
from collections import deque

input = sys.stdin.readline


def a_to_i(alphabet):
    if ord(alphabet) <= ord('Z'):
        return ord(alphabet) - ord('A')
    else:
        return ord(alphabet) - ord('a') + 26


max_size = 52

N = int(input())

c = [[0] * max_size for _ in range(max_size)]
f = [[0] * max_size for _ in range(max_size)]
adj = [list() for _ in range(max_size)]

for _ in range(N):
    v, e, w = input().split()
    v = a_to_i(v)
    e = a_to_i(e)
    w = int(w)
    adj[v].append(e)
    adj[e].append(v)
    c[v][e] += w
    c[e][v] += w

ans = 0
S = a_to_i('A')
T = a_to_i('Z')

while True:
    parent = [-1] * max_size
    queue = deque([S])
    while queue and parent[T] == -1:
        curr = queue.popleft()
        for next_node in adj[curr]:
            if c[curr][next_node] - f[curr][next_node] > 0 and parent[next_node] == -1:
                queue.append(next_node)
                parent[next_node] = curr
                if next_node == T:
                    break

    if parent[T] == -1:
        break

    flow = int(1e9)
    node = T
    while node != S:
        flow = min(flow, c[parent[node]][node] - f[parent[node]][node])
        node = parent[node]

    node = T
    while node != S:
        f[parent[node]][node] += flow
        node = parent[node]

    ans += flow

print(ans)

import sys
from collections import deque

input = sys.stdin.readline


def solve(idx):
    queue = deque()
    queue.append(idx)
    check[idx] = 0

    while queue:
        node = queue.popleft()

        for next_node in adj[node]:
            if check[next_node] == -1:
                queue.append(next_node)
                check[next_node] = (check[node] + 1) % 2
            else:
                if check[node] == check[next_node]:
                    return False

    return True


N, M = map(int, input().split())

adj = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
check = [-1] * (N + 1)

flag = True
for i in range(1, N + 1):
    if check[i] == -1:

        if not solve(i):
            flag = False
            break

print(int(flag))

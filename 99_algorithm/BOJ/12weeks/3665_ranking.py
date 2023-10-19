from collections import deque
import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    base_order = list(map(int, input().split()))
    M = int(input())

    parents = [0] * (N + 1)
    adj = [set() for _ in range(N + 1)]

    for i in range(N):
        parents[base_order[i]] = i
        for j in range(i + 1, N):
            adj[base_order[i]].add(base_order[j])

    for _ in range(M):
        a, b = map(int, input().split())
        if a in adj[b]:
            a, b = b, a

        # b는 a의 후순위 노드인 상태.
        # a -> b인 상태에서 b -> a로 바꿔줌
        adj[a].remove(b)
        adj[b].add(a)
        parents[a] += 1
        parents[b] -= 1

    queue = deque()
    for i in range(1, N + 1):
        if not parents[i]:
            queue.append(i)
            break

    result = []
    while queue:
        curr_node = queue.popleft()
        result.append(curr_node)
        for next_node in adj[curr_node]:
            parents[next_node] -= 1
            if not parents[next_node]:
                queue.append(next_node)

    if len(result) == N:
        print(*result)
    else:
        print('IMPOSSIBLE')


T = int(input())

for tc in range(T):
    solution()

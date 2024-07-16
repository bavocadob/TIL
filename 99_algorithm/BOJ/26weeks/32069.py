import sys
from collections import deque, defaultdict

input = sys.stdin.readline

L, N, K = map(int, input().split())

A = list(map(int, input().split()))

queue = deque()
rst = []

visited = defaultdict(int)

for pos in A:
    queue.append((pos, 1))
    visited[pos] = 1

cnt = min(N, K)

for _ in range(cnt):
    print(0)

while cnt < K:
    node, node_cnt = queue.popleft()

    for gap in range(-1, 2, 2):
        next_node = node + gap

        if 0 <= next_node <= L and visited[next_node] == 0:
            visited[next_node] = node_cnt + 1
            queue.append((next_node, node_cnt + 1))

            print(node_cnt)
            cnt += 1

        if cnt == K:
            break

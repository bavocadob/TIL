import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

roads = [list() for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    roads[x].append(y)

result = []

queue = deque()
visitied = [-1] * (N + 1)
visitied[X] = 0
queue.append(X)

while queue:
    current = queue.popleft()
    if visitied[current] == K:
        result.append(current)

    for next in roads[current]:
        if visitied[next] == -1:
            visitied[next] = visitied[current] + 1
            queue.append(next)

if result:
    result.sort()
    print('\n'.join(map(str,result)))
else:
    print(-1)
import sys

input = sys.stdin.readline

from collections import deque

N = int(input())

graph = [list() for _ in range(N + 1)]

while True:
    x, y = map(int, input().split())
    if (x, y) == (-1, -1):
        break

    graph[x].append(y)
    graph[y].append(x)

result = []
min_score = 100

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    visited[i] = 1

    queue = deque([i])
    while queue:
        member = queue.popleft()

        for next_member in graph[member]:
            if visited[next_member] == 0:
                visited[next_member] = visited[member] + 1
                queue.append(next_member)

    if visited.count(0) == 1:
        temp_score = max(visited)
        if temp_score < min_score:
            result.clear()
            result.append(i)
            min_score = temp_score
        elif temp_score == min_score:
            result.append(i)

print(min_score - 1, len(result))
print(*result)

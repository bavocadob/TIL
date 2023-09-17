import sys

input = sys.stdin.readline

from collections import deque

N, M, Q, K = map(int, input().split())

meeting = list(map(int, input().split()))

connection = [list() for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    connection[x].append(y)
    connection[y].append(x)

visited = [-1] * (N + 1)

queue = deque()
queue2 = deque()
for i in range(Q):
    visited[meeting[i]] = 0
    queue.append(meeting[i])

day = 1
while queue:

    for _ in range(day * K):
        while queue:
            house = queue.popleft()
            for next_house in connection[house]:
                if visited[next_house] == -1:
                    visited[next_house] = day
                    queue2.append(next_house)
        queue = queue2
        queue2 = deque()
        if not queue:
            break
    day += 1
print(' '.join(list(map(str, visited[1:]))))

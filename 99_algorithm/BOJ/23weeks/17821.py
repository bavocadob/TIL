import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()

    queue.append((x, y))
    division[x][y] = div_cnt
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and zoo[x][y] == zoo[nx][ny] and division[nx][ny] == -1:
                division[nx][ny] = div_cnt
                queue.append((nx, ny))


N, M = map(int, input().split())

zoo = [list(input().rstrip()) for _ in range(N)]

division = [[-1] * M for _ in range(N)]

div_cnt = 0

for i in range(N):
    for j in range(M):
        if zoo[i][j] != '*' and division[i][j] == -1:
            bfs(i, j)
            div_cnt += 1

adj = [list() for _ in range(div_cnt)]

adj_set = set()

for i in range(N):
    for j in range(M):
        if division[i][j] == -1:
            continue

        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]

            if 0 <= ni < N and 0 <= nj < M and division[ni][nj] != -1 and division[i][j] != division[ni][nj]:
                if (division[i][j], division[ni][nj]) not in adj_set:
                    left, right = division[i][j], division[ni][nj]

                    adj_set.add((left, right))
                    adj_set.add((right, left))
                    adj[left].append(right)
                    adj[right].append(left)

visited = [False] * div_cnt
visited[0] = True

ans = 1

div_queue = deque([(0, 1)])

while div_queue:
    node, size = div_queue.popleft()
    ans = max(ans, size)

    for next_node in adj[node]:
        if not visited[next_node]:
            visited[next_node] = True
            div_queue.append((next_node, size + 1))

print(ans)

import sys
from collections import deque

input = sys.stdin.readline


def check(cur_x, cur_y, prv_x, prv_y):
    if cur_x > prv_x:
        return 'S'
    elif prv_x > cur_x:
        return 'N'
    elif cur_y > prv_y:
        return 'E'
    else:
        return 'W'


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

A = [list(input().rstrip()) for _ in range(N * 2 - 1)]

adj = [[list() for _ in range(M)] for _ in range(N)]

queue = deque()

end_x, end_y = -1, -1
for i in range(0, N * 2 - 1, 2):
    for j in range(0, M * 2 - 1, 2):

        if A[i][j] == 'S':
            queue.append((i // 2, j // 2))
        elif A[i][j] == 'E':
            end_x, end_y = i // 2, j // 2
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]

            if 0 <= ni < (N * 2 - 1) and 0 <= nj < (M * 2 - 1) and (A[ni][nj] == '-' or A[ni][nj] == '|'):
                ni += dx[k]
                nj += dy[k]

                adj[i // 2][j // 2].append((ni // 2, nj // 2))

visited = [[-1] * M for _ in range(N)]

visited[queue[0][0]][queue[0][1]] = (-1, -1)

while queue:
    x, y = queue.popleft()

    if (x, y) == (end_x, end_y):
        break

    for nx, ny in adj[x][y]:
        if visited[nx][ny] == -1:
            visited[nx][ny] = (x, y)
            queue.append((nx, ny))

curr_x, curr_y = end_x, end_y

rst = []
while (curr_x, curr_y) != (-1, -1):
    next_x, next_y = visited[curr_x][curr_y]

    if (next_x, next_y) == (-1, -1):
        break

    rst.append(check(curr_x, curr_y, next_x, next_y))
    curr_x, curr_y = next_x, next_y

rst.reverse()
cur_idx = 1

cur_direction = rst[0]
cur_cnt = 1
while cur_idx < len(rst):
    if rst[cur_idx] != cur_direction:
        print(cur_direction, cur_cnt)

        cur_direction = rst[cur_idx]
        cur_cnt = 1

    else:
        cur_cnt += 1

    cur_idx += 1
else:
    print(cur_direction, cur_cnt)

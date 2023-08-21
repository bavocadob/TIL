from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def valid_range(x, y):
    return 0 <= x < 10 and 0 <= y < 9


def solution(x, y):
    queue = deque([(x, y)])
    queue2 = deque()

    day = 0

    while queue:
        while queue:
            i, j = queue.popleft()
            if (i, j) == end:
                print(day)
                return
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if valid_range(ni, nj) and (ni, nj) != end:
                    nni, nnj = ni + dx[k] + dy[k], nj + dx[k] + dy[k]
                    if valid_range(nni, nnj) and (nni, nnj) != end:
                        nnii, nnjj = nni + dx[k] + dy[k], nnj + dx[k] + dy[k]
                        if valid_range(nnii, nnjj) and not visited[nnii][nnjj]:
                            queue2.append((nnii, nnjj))
                            visited[nnii][nnjj] = True

                    if dx[k] == 0:
                        nni2, nnj2 = ni + (dx[k] + dy[k]) * -1, nj + (dx[k] + dy[k])
                        if valid_range(nni2, nnj2) and (nni2, nnj2) != end:
                            nni3, nnj3 = nni2 + (dx[k] + dy[k]) * -1, nnj2 + (dx[k] + dy[k])
                            if valid_range(nni3, nnj3) and not visited[nni3][nnj3]:
                                queue2.append((nni3, nnj3))
                                visited[nni3][nnj3] = True
                    else:
                        nni2, nnj2 = ni + (dx[k] + dy[k]), nj + (dx[k] + dy[k]) * -1
                        if valid_range(nni2, nnj2) and (nni2, nnj2) != end:
                            nni3, nnj3 = nni2 + (dx[k] + dy[k]), nnj2 + (dx[k] + dy[k]) * -1
                            if valid_range(nni3, nnj3) and not visited[nni3][nnj3]:
                                queue2.append((nni3, nnj3))
                                visited[nni3][nnj3] = True
        if queue2:
            queue = queue2
            queue2 = deque()

        day += 1


if __name__ == '__main__':
    x_index, y_index = map(int, input().split())
    end = tuple(map(int, input().split()))
    visited = [[False] * 9 for _ in range(10)]
    solution(x_index, y_index)

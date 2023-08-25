import sys
#
input = sys.stdin.readline
# sys.setrecursionlimit(1000000)
#
#
# def dfs(idx, connection, visited):
#     visited[idx] = True
#     if idx != 1 and len(connection[idx]) == 1:
#         return 1
#
#     cnt = 0
#
#     for next_node in connection[idx]:
#         if next_node != idx and not visited[next_node]:
#             cnt += dfs(next_node, connection, visited)
#
#     return cnt


def solution():
    N, W = map(int, input().split())

    # connection = [list() for _ in range(N + 1)]
    connection = [0] * (N + 1)

    visited = [False] * (N + 1)
    for _ in range(N - 1):
        x, y = map(int, input().split())
        # connection[x].append(y)
        # connection[y].append(x)
        connection[x] += 1
        connection[y] += 1
    # num_of_leaf = dfs(1, connection, visited)
    num_of_leaf = 0
    for i in range(2, N + 1):
        if connection[i] == 1:
            num_of_leaf += 1

    print(W / num_of_leaf)


if __name__ == '__main__':
    solution()

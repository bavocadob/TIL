import sys

sys.setrecursionlimit(999999)
input = sys.stdin.readline


def dfs(idx, group, group_idx):
    if visited[A[idx]]:
        if A[idx] in group:
            return group[A[idx]]
        else:
            return group_idx
    else:
        visited[A[idx]] = True
        group[A[idx]] = group_idx
        return dfs(A[idx], group, group_idx + 1)


T = int(input())

for tc in range(T):
    N = int(input())
    A = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    result = 0
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result += dfs(i, {i: 0}, 1)

    print(result)

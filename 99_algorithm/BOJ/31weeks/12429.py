import sys

input = sys.stdin.readline


def dfs(day):
    global ans

    ans = max(ans, day)
    for i in range(N):
        if visited[i] or day > foods[i][0]:
            continue

        visited[i] = True
        dfs(day + foods[i][1])
        visited[i] = False


for t in range(int(input())):
    N = int(input())

    ans = 0
    foods = [tuple(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    dfs(0)
    print(f'Case #{t + 1}: {ans}')

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

visited = [False] * (K + 1)

ans = 0
cnt = 0
for _ in range(N):

    i = int(input())

    if not visited[i]:
        cnt += 1
        visited[i] = True

    if cnt == K:
        cnt = 0
        ans += 1
        visited = [False] * (K + 1)

print(ans + 1)

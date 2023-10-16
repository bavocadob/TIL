import sys

input = sys.stdin.readline

from collections import deque


def solution():
    def init_capacity(m):
        for tg in targets:
            C[tg + N][T] = m

    def can_flow(tg):
        f = [[0] * (T + 1) for _ in range(T + 1)]

        result = 0

        while True:
            prev = [-1] * (T + 1)
            prev[S] = S
            queue = deque([S])

            while queue:
                now = queue.popleft()
                if now == T:
                    break

                for next_node in adj[now]:
                    if prev[next_node] == -1 and C[now][next_node] - f[now][next_node] > 0:
                        prev[next_node] = now
                        queue.append(next_node)

            if prev[T] == -1:
                break

            min_flow = INF
            now = T
            while now != S:
                min_flow = min(min_flow, C[prev[now]][now] - f[prev[now]][now])
                now = prev[now]

            now = T

            while now != S:
                f[prev[now]][now] += min_flow
                f[now][prev[now]] -= min_flow
                now = prev[now]

            result += min_flow

        return result == tg * R

    ans = 0

    left = 0
    right = sum(base_hero) // R

    while left <= right:
        mid = (left + right) // 2
        init_capacity(mid)

        if can_flow(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


INF = int(1e9)
N, M = map(int, input().split())

S = 0
T = N + N + 1

adj = [list() for _ in range(T + 1)]
C = [[0] * (T + 1) for _ in range(T + 1)]

base_hero = list(map(int, input().split()))

for i in range(N):
    C[S][i + 1] = base_hero[i]
    adj[S].append(i + 1)
    adj[i + 1].append(S)

for _ in range(M):
    u, v = map(int, input().split())
    v += N
    C[u][v] = INF
    adj[u].append(v)
    adj[v].append(u)

R = int(input())
targets = list(map(int, input().split()))
for target in targets:
    adj[target].append(target + N)
    adj[target + N].append(target)
    C[target][target + N] = INF

    adj[target + N].append(T)
    adj[T].append(target + N)

rst = solution()
print(rst)

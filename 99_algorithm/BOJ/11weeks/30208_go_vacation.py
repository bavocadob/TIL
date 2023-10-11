import sys

input = sys.stdin.readline


def solution(idx, target, c, r):
    if target >= len(dp) or c > target or dp[target - c] == INF:
        return

    # 현재 과제를 처리하는 게 이득일 때 -> 자식은 따로 본다.
    if dp[target] < dp[target - c] + r:
        dp[target] = dp[target - c] + r
        if adj[idx] == -1:
            return
        solution(adj[idx], target + cost[adj[idx]], cost[adj[idx]], importance[adj[idx]])
    else:  # 현재 과제를 처리하는 게 이득이 아닐 때 -> 자식이랑 합쳐서 다시 본다.
        if adj[idx] == -1:
            return
        solution(adj[idx], target + cost[adj[idx]], c + cost[adj[idx]], r + importance[adj[idx]])


INF = -int(1e9)

N, S = map(int, input().split())

importance = list(map(int, input().split()))

cost = list(map(int, input().split()))

parents = list(map(int, input().split()))

if sum(importance) < S:
    print(-1)
else:
    adj = [-1] * N
    for i in range(N):
        if parents[i]:
            adj[parents[i] - 1] = i
    dp = [INF] * (sum(cost) + 1)
    dp[0] = 0
    for i in range(N):
        if parents[i]:
            continue
        for j in range(len(dp) - 1, cost[i] - 1, -1):
            solution(i, j, cost[i], importance[i])
    for i in range(len(dp)):
        if dp[i] >= S:
            print(i)
            break

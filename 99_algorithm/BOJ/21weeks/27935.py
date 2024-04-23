from collections import deque, defaultdict

INF = int(1e9)
N, L = map(int, input().split())

queue = defaultdict(deque)

train = input().rstrip()

pre = [0] * (N + 1)

dp = [INF] * (N + 1)
dp[0] = 0
for i in range(N):
    if train[i] == 'K':
        pre[i + 1] = pre[i] + 1
    else:
        pre[i + 1] = pre[i] - 1

for i in range(N + 1):
    for j in range(pre[i] - 1, pre[i] + 2):
        while queue[j] and queue[j][0] < i - L:
            queue[j].popleft()

        if queue[j]:
            dp[i] = min(dp[i], dp[queue[j][0]] + 1)

    queue[pre[i]].append(i)

print(dp[N])

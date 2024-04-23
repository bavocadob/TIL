import heapq

N, D = map(int, input().split())

dp = [0] * N

A = list(map(int, input().split()))

queue = []

for i in range(N - 1, -1, -1):

    dp[i] += A[i]

    while queue and queue[0][1] > i + D:
        heapq.heappop(queue)

    if queue:
        dp[i] -= queue[0][0]

    if dp[i] >= 0:
        heapq.heappush(queue, (-dp[i], i))

print(max(dp))

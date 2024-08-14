def reduce_size(x):
    return x * 4 // 5


n, t, k = map(int, input().split())
cheeses = []

for _ in range(n):
    w, h = map(int, input().split())
    cheeses.append((h, w))

cheeses.sort()

dp = [0] * 1005
ans = 0

i = 0
while i < n and cheeses[i][0] < k:
    for j in range(cheeses[i][0], t + 1):
        dp[j] = max(dp[j], dp[j - cheeses[i][0]] + cheeses[i][1])
    i += 1

nn = i
ans = dp[t]

dp = [0] * 1005

for i in range(n):
    for j in range(reduce_size(cheeses[i][0]), t + 1):
        dp[j] = max(dp[j], dp[j - reduce_size(cheeses[i][0])] + cheeses[i][1])

for i in range(nn, n):
    ans = max(ans, dp[t - cheeses[i][0]] + cheeses[i][1])

print(ans)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[(0, 0)] * 2 for _ in range(N + 1)]

# 0이 안먹었을 때 1이 먹었을 때
# 왼쪽 최대값, 오른쪽 먹었을 때 학생 번호
for i in range(1, M + 1):
    l, *data = map(int, input().split())

    for j in range(l):
        food, val = data[j * 2], data[j * 2 + 1]
        if dp[food][1][1] == i - 1:
            temp_val, temp_idx = dp[food][1]

            dp[food][1] = (dp[food][0][0] + val, i)
            dp[food][0] = (max(temp_val, dp[food][0][0]), temp_idx)
        else:
            temp_val, temp_idx = dp[food][1]
            dp[food][1] = (max(temp_val, dp[food][0][0]) + val, i)
            dp[food][0] = (max(dp[food][0][0], temp_val), temp_idx)

ans = 0

for i in range(1, N + 1):
    ans += max(dp[i][0][0], dp[i][1][0])

print(ans)

a_string = input()
b_string = input()

a_len = len(a_string)
b_len = len(b_string)

dp = [[0] * (b_len + 1) for _ in range(a_len + 1)]

for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if a_string[i-1] == b_string[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[a_len][b_len])


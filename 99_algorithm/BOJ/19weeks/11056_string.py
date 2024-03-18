A = input().rstrip()
B = input().rstrip()

len_A = len(A)
len_B = len(B)

dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]
gap = 0


for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        char_A = A[i - 1]
        char_B = B[j - 1]

        if char_A == char_B:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        gap = max(dp[i][j], gap)


print(len_A + len_B - gap)
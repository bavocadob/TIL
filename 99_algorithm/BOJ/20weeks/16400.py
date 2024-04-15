def get_prime(n):
    n += 1
    rst = [2]
    is_prime = [True] * (n // 2)

    for i in range(3, int(n ** 0.5) + 1, 2):
        if is_prime[i // 2]:
            rst.append(i)
            is_prime[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    for i in range((int(n ** 0.5) + 1) // 2, n // 2):
        if is_prime[i]:
            rst.append(2 * i + 1)

    return rst


P = get_prime(40000)
MOD = 123_456_789
N = int(input())

dp = [0] * (N + 1)
dp[0] = 1

for p in P:
    for i in range(p, N + 1):
        dp[i] = (dp[i] + dp[i - p]) % MOD

print(dp[N])

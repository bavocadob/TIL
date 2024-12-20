import math

N = int(input())

divisors = []
for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i:
            divisors.append(N // i)

divisors.sort()
divisors.append(N)

dp = [1] * len(divisors)
for i in range(len(divisors)):
    for j in range(i):
        if divisors[i] % divisors[j] == 0:
            dp[i] += dp[j]

print(dp[-1])

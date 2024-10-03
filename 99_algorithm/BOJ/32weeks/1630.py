def get_primes(limit):
    prime = [False] * (limit + 1)

    for i in range(2, limit + 1):
        if not prime[i]:
            for j in range(i * 2, limit + 1, i):
                prime[j] = True

    return list(filter(lambda x: not prime[x], range(2, limit + 1)))


N = int(input())
MOD = 987654321


primes = get_primes(N)

ans = 1
for p in primes:
    k = p
    while k * p <= N:
        k *= p
    ans *= k
    ans %= MOD

print(ans)

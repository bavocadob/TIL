def sieve_eratosthenes(limit):
    if limit < 2:
        return []

    primes = [2]
    sieve = [True] * ((limit - 1) // 2)

    for i in range(len(sieve)):
        if sieve[i]:
            current = 2 * i + 3
            primes.append(current)
            for multiple in range((current**2 - 3) // 2, len(sieve), current):
                sieve[multiple] = False

    return primes


N = int(input())
if N > 1:
    prime_numbers = sieve_eratosthenes(N)

    ans = 0

    left = right = 0
    curr = prime_numbers[0]

    while True:
        try:
            if curr == N:
                ans += 1
            if curr < N:
                right += 1
                curr += prime_numbers[right]
            else:
                curr -= prime_numbers[left]
                left += 1
        except:
            break
    print(ans)
else:
    print(0)

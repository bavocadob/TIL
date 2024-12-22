import sys
import math

input = sys.stdin.readline


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [x for x in range(limit + 1) if is_prime[x]]


def count_prime_powers(n, primes):
    prime_powers = {1}

    for p in primes:
        power = p
        while power <= n:
            prime_powers.add(power)
            power *= p

    return len(prime_powers)


def solve(n):
    if n == 1:
        return 0
    primes = sieve_of_eratosthenes(int(math.sqrt(n)) + 1)

    P = len([p for p in primes if p <= n])

    P_prime = count_prime_powers(n, primes)

    spread = P_prime - P

    return spread


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    result = solve(N)
    print(f"Case #{t}: {result}")

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
INF = int(1e9)


def find_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime


primes = find_primes(1_000_000)

for _ in range(T):
    x, a, b = map(int, input().split())
    flag = False

    for i in range(a, b + 1):
        if primes[i]:
            flag = True
            break

    if not flag:
        print(-1)
        continue
    queue = deque([(x, 0)])

    dp = [INF] * 1_000_001
    dp[x] = 0

    while queue:
        val, dist = queue.popleft()

        if dp[val] != dist:
            continue

        if a <= val <= b and primes[val]:
            print(dist)
            break

        if dp[val // 2] > dist:
            dp[val // 2] = dist + 1
            queue.append((val // 2, dist + 1))

        if dp[val // 3] > dist:
            dp[val // 3] = dist + 1
            queue.append((val // 3, dist + 1))

        if val - 1 >= a and dp[val - 1] > dist:
            dp[val - 1] = dist + 1
            queue.append((val - 1, dist + 1))

        if val + 1 <= b and dp[val + 1] > dist:
            dp[val + 1] = dist + 1
            queue.append((val + 1, dist + 1))

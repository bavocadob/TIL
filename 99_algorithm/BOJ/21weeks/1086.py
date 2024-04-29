import math
import sys

input = sys.stdin.readline


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N = int(input())

numbers = []
powers = []

for _ in range(N):
    temp = input().rstrip()
    temp_num = int(temp)
    numbers.append(temp_num)
    powers.append(10 ** len(temp))
remain = []
K = int(input())
for num in numbers:
    remain.append(num % K)

dp = [[0] * (K + 1) for _ in range(1 << N)]
dp[0][0] = 1

for bit in range(1 << N):
    for k in range(K + 1):
        for i in range(N):
            if bit & (1 << i):
                continue
            num = (k * powers[i]) + remain[i]
            mod = num % K

            dp[bit | (1 << i)][mod] += dp[bit][k]

mole = dp[(1 << N) - 1][0]
denom = math.perm(N, N)

gcd = get_gcd(denom, mole)

if mole == 0:
    print('0/1')
else:
    print(f'{mole // gcd}/{denom // gcd}')

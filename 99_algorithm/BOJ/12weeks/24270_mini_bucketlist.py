N, K = map(int, input().split())
MOD = 1_000_000_007

times = list(map(int, input().split()))

sum_times = sum(times)

R = K - sum_times

ans = 1

for i in range(1, N + 1):
    ans *= (R + i)
    ans %= MOD

print(ans)
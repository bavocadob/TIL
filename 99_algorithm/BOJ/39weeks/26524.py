MOD = 1_000_000_007

N = int(input())

ans = 1

for i in range(1, N + 1):
    ans = (ans * i) % MOD
print(ans + 1)

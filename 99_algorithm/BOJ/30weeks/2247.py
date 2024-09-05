N = int(input().strip())

ans = 0
MOD = 1000000

for i in range(2, N):
    quotient = N // i - 1
    if quotient <= 0:
        break
    ans = (ans + i * quotient) % MOD

print(ans)

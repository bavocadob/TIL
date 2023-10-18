N = int(input())
MOD = 1_000_000_007

scovilles = list(map(int, input().split()))
a = [1, 2]

for _ in range(N):
    a.append((a[-1] * 2) % MOD)

ans = 0
# print(a)
scovilles.sort()
# 제일 작은 경우는 N - i승
# 제일 큰 경우는 i - 1승
for i in range(1, N + 1):
    x = scovilles[i - 1]
    y = a[i - 1]
    z = a[N - i]

    ans = (ans + (x * (y - z))) % MOD

print(ans)

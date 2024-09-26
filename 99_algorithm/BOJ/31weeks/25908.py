L, R = map(int, input().split())
L -= 1
ans = 0

for i in range(1, R + 1):
    if i % 2:
        ans -= (R // i) - (L // i)
    else:
        ans += (R // i) - (L // i)

print(ans)

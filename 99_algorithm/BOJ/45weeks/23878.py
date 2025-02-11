N = int(input().strip())
s = input().strip()

ans = 0
for i in range(N):
    l = 0
    if i > 0 and s[i - 1] != s[i]:
        l = 1
        k = i - 2
        while k >= 0 and s[k] == s[i - 1]:
            l += 1
            k -= 1

    r = 0
    if i + 1 < N and s[i + 1] != s[i]:
        r = 1
        k = i + 2
        while k < N and s[k] == s[i + 1]:
            r += 1
            k += 1

    ans += l * r + max(l - 1, 0) + max(r - 1, 0)

print(ans)

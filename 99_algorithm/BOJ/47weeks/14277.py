a, b, c, d, u = map(int, input().split())
ans = 0

if a <= u:
    ans = (u - a) // b + 1

if d == 1 and c <= u:
    if not (a == c or (a < c and (c - a) % b == 0)):
        ans += 1
else:
    while c <= u:
        ans += 1
        if c >= a and (c - a) % b == 0:
            ans -= 1
        c *= d

print(ans)

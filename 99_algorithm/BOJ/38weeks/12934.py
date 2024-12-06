X, Y = map(int, input().split())

A = X + Y

# 윤호가 X

idx = 1
cur = 0

while cur < A:
    cur += idx
    idx += 1

if cur != A:
    print(-1)


else:
    ans = 0
    idx -= 1
    while idx > 0 and X > 0:
        if idx < X:
            X -= idx
            ans += 1
            idx -= 1
        else:
            ans += 1
            idx = 0

    print(ans)

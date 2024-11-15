def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def sect(pos, target):
    if pos == 1:
        return (target - 1) // n
    else:
        return (target - 1) // m


n, m, q = map(int, input().split())
g = gcd(n, m)
n //= g
m //= g

for _ in range(q):
    a, b, c, d = map(int, input().split())
    inner = sect(a, b)
    outer = sect(c, d)
    if inner == outer:
        print("YES")
    else:
        print("NO")

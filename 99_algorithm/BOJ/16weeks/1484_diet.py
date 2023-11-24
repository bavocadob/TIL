G = int(input())

l = r = 1
result = []

while True:
    d = r ** 2 - l ** 2
    if r - l == 1 and d > G:
        break

    if d > G:
        l += 1
    elif d < G:
        r += 1
    else:
        result.append(r)
        r += 1

if result:
    for r in result:
        print(r)
else:
    print(-1)

l, r = map(int, input().split())

size = r - l + 1

A = [False] * size

for i in range(2, int(r ** 0.5 + 1) + 1):
    S = i ** 2

    start = l // S + 1 if l % S else l // S

    for j in range(start * S, r + 1, S):
        temp = j - l
        if not A[temp]:
            A[temp] = True
            size -= 1

print(size)

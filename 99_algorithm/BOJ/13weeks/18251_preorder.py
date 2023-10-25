from math import log2

N = int(input())

numbers = [-float('inf')] + list(map(int, input().split()))

h = int(log2(N)) + 1

nodes = []


def preorder(idx, height):
    if idx * 2 <= N:
        preorder(idx * 2, height + 1)
    nodes.append((numbers[idx], height))
    if idx * 2 + 1 <= N:
        preorder(idx * 2 + 1, height + 1)


preorder(1, 0)
# print(nodes)

ans = max(numbers)
for i in range(h):
    for j in range(i, h):
        temp = 0
        for w, hh in nodes:
            if i > hh or j < hh:
                continue

            if temp + w < 0:
                temp = 0

            else:
                temp += w
                ans = max(ans, temp)

print(ans)

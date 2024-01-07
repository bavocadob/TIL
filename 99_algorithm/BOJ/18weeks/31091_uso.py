N = int(input())

A = list(map(int, input().split()))

under = [0] * (N + 2)
over = [0] * (N + 2)

for a in A:
    if a > 0:
        over[a - 1] += 1
    else:
        under[-a + 1] += 1

for i in range(N, -1, -1):
    over[i] += over[i + 1]

for i in range(1, N + 2):
    under[i] += under[i - 1]

rst = []

for i in range(N + 1):
    if over[i] + under[i] == i:
        rst.append(i)

print(len(rst))
print(*rst)

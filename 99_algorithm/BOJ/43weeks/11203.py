temp = input().split()

N = int(temp[0])
S = ""

if len(temp) > 1:
    S = temp[1]

r = 0
for char in S:
    r *= 2

    if char == 'R':
        r += 1

print(2 ** (N + 1) - 2 ** len(S) - r)
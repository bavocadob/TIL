N = int(input())

rst = [0] * (N + 1)

rst[1] = 1
curr = 1

for i in range(2, N + 1):
    if rst[i] == 0:
        curr += 1
        rst[i] = curr

        for j in range(i * 2, N + 1, i):
            if rst[j] != 0:
                continue
            rst[j] = curr

print(curr)

print(*rst[1:])

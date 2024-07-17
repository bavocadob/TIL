N, M = map(int, input().split())

A = input().rstrip()
B = input().rstrip()

a = []
b = []

for i in range(N + M):
    if A[i] == '1':
        a.append(i)

    if B[i] == '1':
        b.append(i)

ans = 0

for i in range(M):
    ans += abs(a[i] - b[i])

left = ans // 2
right = ans // 2 + ans % 2

print(left ** 2 + right ** 2)

N = int(input())

A = [0] * (N + 1)
B = [0] * (N + 1)
honey = list(map(int, input().split()))

for i in range(1, N + 1):
    A[i] = A[i - 1] + honey[i - 1]
    B[N - i] = B[N - i + 1] + honey[N - i]

ans = 0
for i in range(2, N):
    temp = A[i] - A[1] + B[i - 1] - B[N - 1]
    ans = max(ans, temp)

for i in range(2, N):
    temp = A[N] - honey[0] - honey[i - 1] + A[N] - A[i]

    temp2 = A[N] - honey[N - 1] - honey[i - 1] + B[0] - B[i - 1]
    ans = max(ans, temp, temp2)

print(ans)

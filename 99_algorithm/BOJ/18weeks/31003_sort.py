def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_co_prime(x, y):
    return gcd(x, y) == 1


N = int(input())

A = list(map(int, input().split()))

B = [0] * N

for i in range(1, N):
    for j in range(i):
        if not is_co_prime(A[i], A[j]):
            B[i] += 1

for k in range(N):
    temp = A[k]
    temp_idx = k
    for i in range(k + 1, N):
        if B[i] == 0 and temp > A[i]:
            temp_idx = i
            temp = A[i]

    for i in range(temp_idx + 1, N):
        if not is_co_prime(A[temp_idx], A[i]):
            B[i] -= 1

    for i in range(temp_idx, k, -1):
        A[i], A[i - 1] = A[i - 1], A[i]
        B[i], B[i - 1] = B[i - 1], B[i]

print(*A)

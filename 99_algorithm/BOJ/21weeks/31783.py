def binary_search(l, r, t):
    while l < r:
        mid = (l + r) // 2
        if H[mid] >= t:
            l = mid + 1
        else:
            r = mid - 1

    if H[l] < target:
        return l - 1

    return l


N = int(input())

H = list(map(int, input().split()))

A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

dp = [0] * N

for i in range(1, N):
    dp[i] = dp[i - 1]

    target = H[i] + B[i]
    if H[0] < target:
        continue

    left = 0
    right = i - 1

    idx = binary_search(left, right, target)

    dp[i] = max(dp[i], dp[idx] + A[i])

print(dp[N - 1])

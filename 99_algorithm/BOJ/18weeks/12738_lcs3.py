def binary_search(target):
    # lower bound 구현
    left = 0
    right = N

    while left <= right:
        mid = (left + right) // 2
        if minimal[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return right


INF = int(2e9)
N = int(input())

numbers = list(map(int, input().split()))

dp = [0] * (N + 1)
minimal = [INF] * (N + 1)
minimal[0] = -INF

for i in range(N):
    number = numbers[i]
    idx = binary_search(number) + 1
    dp[i + 1] = idx
    minimal[idx] = number

print(max(dp))

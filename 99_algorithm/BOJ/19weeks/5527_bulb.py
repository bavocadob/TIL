def solve(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] + arr[1]

    ans = 0

    for i in range(N - 2):
        ans = max(ans, sum(arr[i:i + 3]))
    return ans


N = int(input())

A = list(map(int, input().split()))

dp = []

consecutive = 1

for i in range(1, N):
    if A[i] != A[i - 1]:
        consecutive += 1
    else:
        dp.append(consecutive)
        consecutive = 1
dp.append(consecutive)
print(solve(dp))

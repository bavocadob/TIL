def binary_search(target):
    left = 0
    right = len(dp) - 1

    while left <= right:
        mid = (left + right) // 2

        if dp[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left


N = int(input())

nums = list(map(int, input().split()))

pos = [0] * N

dp = [nums[0]]

for i in range(1, N):
    num = nums[i]
    idx = binary_search(num)
    pos[i] = idx
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

rst = [0] * len(dp)
idx = len(dp) - 1
for i in range(N - 1, -1, -1):
    if pos[i] == idx:
        rst[idx] = nums[i]
        idx -= 1

    if idx == -1:
        break

print(len(dp))
print(*rst)

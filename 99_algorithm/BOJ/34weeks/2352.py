def binary_search(target):
    left = 0
    right = len(dp) - 1

    while left <= right:
        mid = (left + right) // 2

        if dp[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return left


N = int(input())

nums = list(map(int, input().split()))

dp = [nums[0]]

for i in range(1, N):
    num = nums[i]
    pos = binary_search(num)
    # print(f'{i + 1}번째 값 {num}의 위치 찾기')
    # print(pos)

    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num


print(len(dp))

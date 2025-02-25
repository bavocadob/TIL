import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    d, n = map(int, input().split())
    nums = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    mod = [0] * d

    ans = 0

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        ans += mod[prefix_sum[i + 1] % d]
        mod[prefix_sum[i + 1] % d] += 1

    ans += mod[0]
    print(ans)

def dp_solution(N):
    max_coupon = 100
    dp = [[float('inf')] * (max_coupon + 1) for _ in range(N + 6)]
    dp[0][0] = 0

    for day in range(N):
        for coupon in range(50):
            if dp[day][coupon] != float('inf'):
                curr = dp[day][coupon]
                if day + 1 in yasumi:
                    dp[day + 1][coupon] = curr
                    continue

                if coupon >= 3:
                    dp[day + 1][coupon - 3] = min(dp[day + 1][coupon - 3], curr)

                dp[day + 1][coupon] = min(curr + 10000, dp[day + 1][coupon])

                for i in range(day + 1, day + 4):
                    dp[i][coupon + 1] = min(dp[i][coupon + 1], curr + 25000)

                for i in range(day + 1, day + 6):
                    dp[i][coupon + 2] = min(dp[i][coupon + 2], curr + 37000)

    # for d input.txt dp:
    #     print(d)
    result = min(dp[N])
    return result


n, m = map(int, input().split())
yasumi = []

if m > 0:
    yasumi = list(map(int, input().split()))

print(dp_solution(n))

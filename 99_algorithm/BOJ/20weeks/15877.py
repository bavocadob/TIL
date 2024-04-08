import sys

sys.setrecursionlimit(int(1e6))


def solve(apple, banana, is_alice):
    if dp[apple][banana] != -1:
        return dp[apple][banana]

    if not apple:
        r1 = not is_alice
    else:
        r1 = solve(apple - 1, banana, not is_alice)

    if not banana:
        r2 = not is_alice
    else:
        r2 = solve(apple, banana - 1, not is_alice)

    if apple < 3 or banana < 1:
        r3 = not is_alice
    else:
        r3 = solve(apple - 3, banana - 1, not is_alice)

    if apple < 1 or banana < 3:
        r4 = not is_alice
    else:
        r4 = solve(apple - 1, banana - 3, not is_alice)

    if is_alice:  # 엘리스인 경우 r1,r2,r3,r4중 하나라도 트루라면 이길 수 있는거
        dp[apple][banana] = r1 or r2 or r3 or r4
        return dp[apple][banana]
    else:  # is_alice가 false경우 즉 밥인 경우 r1, r2 ,r3 ,r4중 하나라도 false가 있는 경우 승리 즉 false
        dp[apple][banana] = r1 and r2 and r3 and r4
        return dp[apple][banana]


a, b = map(int, input().split())

dp = [[-1] * (b + 1) for _ in range(a + 1)]

if not a and not b:
    print('Bob')
else:
    print('Alice' if solve(a, b, True) else 'Bob')

print(dp)
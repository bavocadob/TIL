def solve(x, y, z):
    if x == 1 or x == y:
        return 1
    if dp[x][y][z]:
        return dp[x][y][z]
    dp[x][y][z] = sum(solve(x-1, y-i, i) for i in range(z, y//x + 1))
    return dp[x][y][z]


n = int(input())
k = int(input())
dp = [[[0]*305 for _ in range(305)] for _ in range(305)]
print(solve(k, n, 1))

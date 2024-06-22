import sys

sys.setrecursionlimit(9999999)

N = int(input())
input_str = input()

dp = [[-1 for _ in range(3 * N)] for _ in range(3 * N)]


def solve(l, r, prev):
    if l > r:
        return 0
    if dp[l][r] != -1:
        return dp[l][r]

    ret = 0
    if (input_str[l] == 'B' and prev == ' ') or (input_str[l] == 'B' and prev == 'D') or (
            input_str[l] == 'L' and prev == 'B') or (
            input_str[l] == 'D' and prev == 'L'):
        ret = max(ret, solve(l + 1, r, input_str[l]) + 1)
    if (input_str[r] == 'B' and prev == ' ') or (input_str[r] == 'B' and prev == 'D') or (
            input_str[r] == 'L' and prev == 'B') or (
            input_str[r] == 'D' and prev == 'L'):
        ret = max(ret, solve(l, r - 1, input_str[r]) + 1)

    dp[l][r] = ret
    return ret


result = solve(0, 3 * N - 1, ' ')
print(result)

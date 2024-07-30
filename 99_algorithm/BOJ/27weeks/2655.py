import sys

input = sys.stdin.readline


class Result:

    def __init__(self, ans, arr):
        self.ans = ans
        self.arr = arr


N = int(input())

blocks = [(10001, 10001, 0, 0)]

for i in range(1, N + 1):
    base, height, weight = map(int, input().split())

    blocks.append((base, weight, height, i))

blocks.sort(reverse=True)

dp = [Result(-1, list()) for _ in range(N + 1)]

dp[0] = Result(0, list())

for i in range(1, N + 1):
    temp = -1
    for j in range(i):

        if blocks[j][1] > blocks[i][1] and dp[j].ans + blocks[i][2] > temp:
            temp = dp[j].ans + blocks[i][2]
            dp[i] = Result(temp, dp[j].arr + [blocks[i][3]])

ans = -1
ans_arr = []

for i in range(1, N + 1):
    if dp[i].ans > ans:
        ans = dp[i].ans
        ans_arr = dp[i].arr

print(len(ans_arr))

for i in reversed(ans_arr):
    print(i)

import sys

input = sys.stdin.readline


def get_distance(a, b):
    x1, y1 = a
    x2, y2 = b

    return abs(x2 - x1) + abs(y2 - y1)


INF = int(1e9)
N = int(input())

W = int(input())

A = [(0, 0)]
for _ in range(W):
    x, y = map(int, input().split())
    A.append((x, y))

dp = [[INF] * (W + 1) for _ in range(W + 1)]

dp[1][0] = get_distance((1, 1), A[1])
dp[0][1] = get_distance(A[1], (N, N))

for i in range(W):
    for j in range(W):

        if i == j:
            continue

        if i == 0:
            A[0] = (1, 1)
        elif j == 0:
            A[0] = (N, N)

        next_case = max(i, j) + 1

        # i번째에 있던 차량이 next_case번 사건에 가는 경우
        first = dp[i][j] + get_distance(A[i], A[next_case])
        if first < dp[next_case][j]:
            dp[next_case][j] = first

        second = dp[i][j] + get_distance(A[j], A[next_case])
        if second < dp[i][next_case]:
            dp[i][next_case] = second

ans = INF

print(dp)

left = -1
right = -1
for i in range(W):
    if ans > dp[i][W]:
        ans = dp[i][W]
        left, right = i, W

    if ans > dp[W][i]:
        ans = dp[W][i]
        left, right = W, i


print(ans)

ans_list = []
while left != 0 and left != 1 and right != 0  and right != 1:
    if right > left and right - left > 1:
        ans_list += (right - left - 1) * [2]
        right = left + 1
        continue

    if left > right and left - right > 1:
        ans_list += (left - right - 1) * [1]
        left = right + 1
        continue

    if left > right:
        ans_list.append(2)
        ans_list.append(1)
    else:
        ans_list.append(1)
        ans_list.append(2)

    curr = dp[left][right]
    next_case = min(left, right - 1)

    for i in range(next_case):

        if dp[i][next_case] == dp[left][right] - 





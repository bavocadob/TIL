import sys

input = sys.stdin.readline


def binary_search_lower(dp, target):
    l = 0
    r = len(dp) - 1

    while l <= r:
        mid = (l + r) // 2

        if dp[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1

    return l


N = int(input())

left = list(map(int, input().split()))
right = list(map(int, input().split()))

right_dict = dict()

for i in range(N):
    right_dict[right[i]] = i

line = []

for i in range(N):
    line.append(right_dict[left[i]])

dp_plus = [line[0]]
plus_pos = [0] * N

for i in range(1, N):
    num = line[i]

    idx = binary_search_lower(dp_plus, num)

    if idx == len(dp_plus):
        dp_plus.append(num)
    else:
        dp_plus[idx] = num

    plus_pos[i] = idx

curr = len(dp_plus) - 1

rst = []
for i in range(N - 1, -1, -1):
    if plus_pos[i] == curr:
        rst.append(left[i])
        curr -= 1

    if curr == -1:
        break

rst.sort()
print(len(dp_plus))
print(*rst)

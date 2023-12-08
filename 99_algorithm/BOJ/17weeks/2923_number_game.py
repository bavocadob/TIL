import sys

input = sys.stdin.readline

N = int(input())

A = [0] * 101
B = [0] * 101

for i in range(N):
    a, b = map(int, input().split())
    A[a] += 1
    B[b] += 1

    left = 0
    right = 101
    cnt = 0
    left_cnt = 0
    right_cnt = 0

    ans = 0
    while cnt <= i:
        if left_cnt == 0:
            left += 1
            left_cnt = A[left]
            continue
        if right_cnt == 0:
            right -= 1
            right_cnt = B[right]
            continue

        card = min(left_cnt, right_cnt)
        left_cnt -= card
        right_cnt -= card
        cnt += card
        ans = max(ans, left + right)

    print(ans)

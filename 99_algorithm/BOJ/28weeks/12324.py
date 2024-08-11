import sys

input = sys.stdin.readline


def solve(left, right, curr_size, cnt):
    global ans

    if cnt >= ans:
        return

    while left <= right and motes[left] < curr_size:
        curr_size += motes[left]
        left += 1

    if left > right:
        ans = cnt
        return

    if curr_size > 1:
        solve(left, right, curr_size * 2 - 1, cnt + 1)
        solve(left, right - 1, curr_size, cnt + 1)

    else:
        solve(left, right - 1, curr_size, cnt + 1)


T = int(input())

for t in range(1, T + 1):
    A, N = map(int, input().split())

    motes = list(map(int, input().split()))
    motes.sort()

    ans = float('inf')
    solve(0, N - 1, A, 0)
    print(f'Case #{t}: {ans}')

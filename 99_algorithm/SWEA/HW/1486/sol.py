import sys

sys.stdin = open('input.txt')


def backtrack(depth, val):
    global gap
    if val > target_gap:
        return

    if depth == N:
        gap = max(gap, val)
        return

    backtrack(depth + 1, val + heights[depth])
    backtrack(depth + 1, val)


T = int(input())
for tc in range(T):
    N, B = map(int, input().split())

    heights = list(map(int, input().split()))
    max_heights = sum(heights)
    # 얘가 기준
    target_gap = max_heights - B

    gap = 0
    backtrack(0, 0)
    # print(target_gap, gap)
    print(f'#{tc + 1} {target_gap - gap}')

from collections import defaultdict


def solution(target):
    cnt = 0
    window_set = set()
    window_dict = defaultdict(int)
    window_len = 0
    curr_idx = target

    while curr_idx < N:
        window_set.add(cards[curr_idx])
        window_dict[cards[curr_idx]] += 1

        if window_len < target:
            window_len += 1
        else:
            window_dict[cards[curr_idx - target]] -= 1
            if not window_dict[cards[curr_idx - target]]:
                window_set.remove(cards[curr_idx - target])

        if window_len == target and len(window_set) == target:
            window_set = set()
            window_dict = defaultdict(int)
            window_len = 0

    return cnt >= M


N, M = map(int, input().split())

cards = list(map(int, input().split()))

left = 1
right = N // M

ans = 0
while left <= right:
    mid = (left + right) // 2

    if solution(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)

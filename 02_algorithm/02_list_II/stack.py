import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(range(1, 13))
    result = 0

    stack = [(0, [])]
    while stack:
        idx, arr = stack.pop()

        if idx == 12:
            if len(arr) == N and sum(arr) == K:
                print(arr)
                result += 1
            continue

        stack.append((idx+1, arr + [nums[idx]]))
        stack.append((idx+1, arr))

    print(result)
T = int(input())

def backtracking(idx, arr, current_sum):
    global result

    if len(arr) > N or current_sum > K:
        print(arr)
        return

    if idx == 12:
        if len(arr) == N and current_sum == K:
            print(arr)
            result += 1
        return

    backtracking(idx + 1, arr + [nums[idx]], current_sum + nums[idx])
    backtracking(idx + 1, arr, current_sum)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(range(1, 13))
    result = 0
    backtracking(0, [], 0)
    print(result)
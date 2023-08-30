import sys

sys.setrecursionlimit(9999999)

sys.stdin = open('input.txt')


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False

    return True


def check_duplicate(arr):
    target = arr[:]
    for i in range(len(target) - 1):
        if target[i] == target[i + 1]:
            return True

    return False


def dfs(idx, change_cnt):
    global result, end
    if end:
        return

    if change_cnt == K:
        if result < ''.join(numbers):
            result = ''.join(numbers)

        return

    if is_sorted(numbers):
        if (K - change_cnt) % 2 and not duplicate:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
            result = ''.join(numbers)
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        else:
            result = ''.join(numbers)
            end = True
        return

    change = False
    for i in range(idx + 1, N):
        if numbers[i] > numbers[idx]:
            numbers[i], numbers[idx] = numbers[idx], numbers[i]
            dfs(idx + 1, change_cnt + 1)
            numbers[i], numbers[idx] = numbers[idx], numbers[i]
            change = True

    if not change and idx < len(numbers):
        dfs(idx + 1, change_cnt)


T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    numbers = list(str(N))
    result = str(N)
    N = len(numbers)

    duplicate = check_duplicate(numbers)

    end = False

    for i in range(N):
        dfs(i, 0)

    print(f'#{tc + 1} {result}')

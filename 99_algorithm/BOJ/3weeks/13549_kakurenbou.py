N, K = map(int, input().split())


def solution(left, right):
    if left >= right:
        return left - right
    if left == 0 and right == 1:
        return 1
    if right % 2:
        return min(solution(left, right - 1), solution(left, right + 1)) + 1
    else:
        return min(right - left, solution(left, right // 2))


print(solution(N, K))

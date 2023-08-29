def solution(s):
    left = 0
    right = N - 1

    min_gap = float('inf')
    result = None

    while left < right:
        gap = s[right] + s[left]
        if abs(gap) < min_gap:
            result = (left, right)
            min_gap = abs(gap)
        if gap == 0:
            break
        elif gap > 0:
            right -= 1
        else:
            left += 1

    return result


N = int(input())

solutions = list(map(int, input().split()))
solutions.sort()
l, r = solution(solutions)
print(solutions[l], solutions[r])

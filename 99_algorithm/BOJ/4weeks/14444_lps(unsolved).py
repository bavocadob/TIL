def solution(s: str):
    def expand(left, right) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        # return s[left + 1:right - 1]
        return right - left - 2

    if len(s) == 1 or s == s[::-1]:
        return len(s)

    # result = ''
    result = 0
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2))
    return result


if __name__ == '__main__':
    print(solution(input()))

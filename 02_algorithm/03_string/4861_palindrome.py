def is_palindrome(arr, left, right):
    while left <= right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True


def solution(words):
    for word in words:
        for i in range(N - M + 1):
            if is_palindrome(word, i, i + M - 1):
                return word[i:i + M]
    trans_words = list(map(''.join, list(zip(*words))))

    for word in trans_words:
        for i in range(N - M + 1):
            if is_palindrome(word, i, i + M - 1):
                return word[i:i + M]


for T in range(int(input())):
    N, M = map(int, input().split())

    input_words = [input() for _ in range(N)]

    print(f'#{T + 1} {solution(input_words)}')

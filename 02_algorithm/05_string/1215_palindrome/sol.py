import sys

sys.stdin = open('input.txt')


def is_palindrome(arr, left, right):
    while left <= right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True


def solution(words, length):
    cnt = 0
    for word in words:
        for i in range(8 - length + 1):
            if is_palindrome(word, i, i + length - 1):
                cnt += 1

    trans_words = list(map(''.join, list(zip(*words))))

    for word in trans_words:
        for i in range(8 - length + 1):
            if is_palindrome(word, i, i + length - 1):
                cnt += 1

    return cnt


for T in range(1, 11):
    n = int(input())

    input_words = [input() for _ in range(8)]

    print(f'#{T} {solution(input_words, n)}')

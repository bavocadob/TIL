import sys

input = sys.stdin.readline

N = int(input())


def check(word, l, r):
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            left_delete = check(word, left + 1, right)
            right_delete = check(word, left, right - 1)
            if left_delete or right_delete:
                return 1
            else:
                return 2
    return 0


for _ in range(N):
    text = input().rstrip()

    print(is_palindrome(text))

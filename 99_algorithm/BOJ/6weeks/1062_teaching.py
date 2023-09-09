import sys

input = sys.stdin.readline

from itertools import combinations


def solution(n, k):
    base_alphabet = {'a', 'n', 't', 'i', 'c'}
    candidate_alphabet = set()
    alphabet_set = [set() for _ in range(N)]

    for i in range(n):
        word = input().rstrip()

        for char in word:
            if char not in base_alphabet:
                candidate_alphabet.add(char)
                alphabet_set[i].add(char)

    # print(candidate_alphabet)
    ans = 0
    for c in combinations(candidate_alphabet, min(k - 5, len(candidate_alphabet))):
        temp = 0
        cc = set(c)
        for a in alphabet_set:
            if cc >= a:
                temp += 1

        ans = max(temp, ans)

    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    if 26 > K >= 5:
        solution(N, K)
    elif K == 26:
        print(N)
    else:
        print(0)

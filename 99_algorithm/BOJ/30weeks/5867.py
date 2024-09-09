import sys

input = sys.stdin.readline


def check(w, target_arr: list, gap):
    left = 0
    right = N - 1

    while left <= right:

        mid = (left + right) // 2

        if target_arr[mid][0] == w:
            return mid + 1
        elif target_arr[mid][0] > w:
            right = mid - 1
        else:
            left = mid + 1

    return left + gap + 1


N = int(input())

S = []
R = []

for i in range(N):
    S.append((''.join(sorted(list(input().rstrip()))), i))
    R.append((S[-1][0][::-1], i))

S.sort()
R.sort()

ans_S = [-1] * N
ans_R = [-1] * N

for word, idx in S:
    ans_S[idx] = check(word, R, 0)

for word, idx in R:
    ans_R[idx] = check(word, S, -1)

for i in range(N):
    print(ans_S[i], ans_R[i])

import sys

from collections import defaultdict

input = sys.stdin.readline

R, C = map(int, input().split())

A = [input().rstrip() for _ in range(R)]

left, right = 0, R - 1

A = list(zip(*A))

for i in range(len(A)):
    A[i] = ''.join(A[i])

ans = 0

while left <= right:
    mid = (left + right) // 2

    word_dict = defaultdict(bool)
    flag = False
    for i in range(C):
        temp = A[i][mid:]
        if word_dict[temp]:
            flag = True
            break
        else:
            word_dict[temp] = True

    if not flag:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)

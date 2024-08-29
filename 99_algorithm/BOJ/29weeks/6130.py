import sys

input = sys.stdin.readline
N = int(input())
A = [int(input()) - 1 for _ in range(N)]
count = [0, 0, 0]

for i in range(N):
    count[A[i]] += 1

ans = 0

for i in range(count[0]):
    if A[i] == 0:
        continue
    if A[i] == 2:
        changed = False
        for j in range(count[0] + count[1], N):
            if A[j] != 0:
                continue
            A[i], A[j] = A[j], A[i]
            ans += 1
            changed = True
            break
        if changed:
            continue
    for j in range(count[0], N):
        if A[j] != 0:
            continue
        A[i], A[j] = A[j], A[i]
        ans += 1
        break
# 끝나면 0은 정렬되어 있음


for i in range(count[0], count[0] + count[1]):
    if A[i] == 1:
        continue
    for j in range(count[0] + count[1], N):
        if A[j] != 1:
            continue
        A[i], A[j] = A[j], A[i]
        ans += 1
        break

print(ans)

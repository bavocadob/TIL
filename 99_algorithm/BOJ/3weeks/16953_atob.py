import sys


# def solution(target, curr):
#     if target == curr:
#         return 1
#     if curr % 2 == 0:
#         return solution(target, curr // 2) + 1
#     elif curr % 10 == 1 and (curr - 1) // 10 > target:
#         return solution(target, (curr - 1) // 10) + 1

N, M = map(int, input().split())

cnt = 1
valid = True
while True:
    if M == N:
        break

    if M < N:
        valid = False
        break

    if M % 2 == 0:
        M //= 2
    elif (M % 10) == 1:
        M = (M - 1) // 10
    else:
        valid = False
        break
    cnt += 1

if valid:
    print(cnt)
else:
    print(-1)


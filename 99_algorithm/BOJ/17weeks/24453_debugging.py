import sys

input = sys.stdin.readline

N, M = map(int, input().split())
errors = list(map(int, input().split()))
X, Y = map(int, input().split())

error_list = [False] * (N + 1)
for error in errors:
    error_list[error] = True

error_cnt = 0

for i in range(1, X + 1):
    if error_list[i]:
        error_cnt += 1

min_error = error_cnt

for i in range(X + 1, N + 1):
    if error_list[i]:
        error_cnt += 1

    if error_list[i - X]:
        error_cnt -= 1

    min_error = min(min_error, error_cnt)

if min_error <= Y:
    print(M - Y)
else:
    print(M - min_error)

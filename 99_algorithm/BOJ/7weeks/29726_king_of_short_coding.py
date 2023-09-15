# import sys
#
# sys.stdin = open('input.txt')

N, M = map(int, input().split())

gap = [0] * (N - 1)

numbers = list(map(int, input().split()))

prefix_max = [0] * (M + 1)
prefix_max[M] = numbers[-1]

for i in range(M):
    prefix_max[M - 1 - i] = max(prefix_max[M - i], numbers[N - 2 - i])

ans = -float('inf')
# print(prefix_max)
for i in range(M + 1):
    ans = max(ans, prefix_max[i] - numbers[i])

print(ans)

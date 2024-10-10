import sys

input = sys.stdin.readline
N = int(input())

A = [int(input()) for _ in range(N)]

cnt = [0] * 1_000_001

for a in A:
    cnt[a] += 1

rst = [0] * 1_000_001

for i in range(1, 1_000_000):
    if cnt[i]:
        rst[i] += cnt[i] - 1
        for j in range(i + i, 1_000_001, i):
            rst[j] += cnt[i]

for a in A:
    print(rst[a])

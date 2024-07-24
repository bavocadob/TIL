import sys

input = sys.stdin.readline
N, M = map(int, input().split())

visited = [True] * (N + 1)

A = []
for i in range(M):
    temp = int(input())

    A.append(temp)
    visited[temp] = False

B = []

for i in range(1, N + 1):
    if visited[i]:
        B.append(i)

cur_idx = 0

for cur in A:
    while cur_idx < len(B) and B[cur_idx] < cur:
        print(B[cur_idx])
        cur_idx += 1

    print(cur)

while cur_idx < len(B):
    print(B[cur_idx])
    cur_idx += 1

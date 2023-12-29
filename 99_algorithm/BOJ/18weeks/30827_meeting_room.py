import sys

input = sys.stdin.readline

N, K = map(int, input().split())

room = [0] * K

meetings = []

for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: x[1])

ans = 0
for s, e in meetings:
    r_num = -1
    r_end = -1

    for i in range(K):
        if s > room[i] > r_end:
            r_num = i
            r_end = room[i]

    if r_num == -1:
        continue
    ans += 1
    room[r_num] = e

print(ans)

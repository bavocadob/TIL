import sys

input = sys.stdin.readline

N = int(input())

node_count = [0] * (N + 1)
connection = []

for _ in range(N - 1):
    x, y = map(int, input().split())
    node_count[x] += 1
    node_count[y] += 1
    connection.append((x, y))

g_cnt = 0
d_cnt = 0

for n in node_count:
    if n >= 3:
        g_cnt += (n * (n - 1) * (n - 2)) // 6

for c in connection:
    x, y = c
    d_cnt += (node_count[x] - 1) * (node_count[y] - 1)

if d_cnt > g_cnt * 3:
    print('D')
elif d_cnt < g_cnt * 3:
    print('G')
else:
    print('DUDUDUNGA')

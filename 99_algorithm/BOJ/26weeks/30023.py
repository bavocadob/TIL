import sys

input = sys.stdin.readline


N, X = map(int, input().split())

temp = 0

gap = []
for i in range(N):
    a, b = map(int, input().split())
    temp += b

    gap.append(a - b)

gap.sort(reverse=True)

use_money = N * 1000

idx = 0

while use_money + 4000 <= X and gap[idx] > 0 and idx < N:
    temp += gap[idx]
    idx += 1
    use_money += 4000

print(temp)

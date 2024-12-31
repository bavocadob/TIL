import sys

input = sys.stdin.readline
L, U = map(int, input().split())

MOD = 1000000007
sum_value = 0
multi = 1

if L == 1:
    sum_value += 1
    L += 1
if U != 1 and L == 2:
    sum_value += 1
    L += 1

print("H" if sum_value & 1 else "A")

for i in range(3, U + 1):
    if i & 1:
        multi = (multi * 26) % MOD
    if i >= L:
        sum_value = (sum_value + multi) % MOD

print(sum_value)

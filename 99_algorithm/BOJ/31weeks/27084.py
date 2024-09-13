from collections import defaultdict

MOD = 1_000_000_007
N = int(input())

num_dict = defaultdict(int)

for num in list(map(int, input().split())):
    num_dict[num] += 1

ans = 1
for i in num_dict.values():
    ans *= i + 1

print((ans - 1) % MOD)

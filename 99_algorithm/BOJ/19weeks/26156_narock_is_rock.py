from collections import defaultdict

MOD = 1_000_000_007
N = int(input())

S = input().rstrip()

pow = [1]
cnt = [0] * 4
rock_dict = defaultdict(int)
alphabet_dict = {'O': 'R', 'C': 'O', 'K': 'C'}

for i in range(N):
    pow.append((pow[i] * 2) % MOD)

for i in range(N):
    char = S[i]
    if char == 'R':
        rock_dict[char] += pow[i]
    elif char in alphabet_dict:
        rock_dict[char] += rock_dict[alphabet_dict[char]]

    rock_dict[char] %= MOD

print(rock_dict['K'])

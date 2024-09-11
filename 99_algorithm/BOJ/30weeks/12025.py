import sys

input = sys.stdin.readline

pos = {'1': '6', '6': '6', '2': '7', '7': '7'}
neg = {'1': '1', '6': '1', '2': '2', '7': '2'}
N = list(input().rstrip())

K = int(input())
bin_k = str(bin(K - 1)[2:])

cnt = 0

for i in range(len(N)):
    char = N[i]
    if char in {'1', '2', '6', '7'}:
        cnt += 1
        N[i] = neg[N[i]]

if len(bin_k) > cnt:
    print(-1)
else:
    idx = len(bin_k) - 1
    char_idx = len(N) - 1
    while idx >= 0:
        if N[char_idx] in {'1', '2', '6', '7'}:
            if bin_k[idx] == '1':
                N[char_idx] = pos[N[char_idx]]
            else:
                N[char_idx] = neg[N[char_idx]]
            idx -= 1

        char_idx -= 1
    print(''.join(N))

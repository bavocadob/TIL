import sys

input = sys.stdin.readline

string = input().rstrip()

prefix_sum = [[0] * (len(string) + 1) for _ in range(26)]

for i in range(1, len(string) + 1):
    char = string[i - 1]
    prefix_sum[ord(char) - 97][i] += 1
    for k in range(26):
        prefix_sum[k][i] += prefix_sum[k][i - 1]

N = int(input())

for _ in range(N):
    alphabet, left, right = input().split()
    left = int(left)
    right = int(right)
    idx = ord(alphabet) - 97
    print(prefix_sum[idx][right + 1] - prefix_sum[idx][left])

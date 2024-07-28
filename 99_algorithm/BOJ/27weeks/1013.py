import re
import sys

input = sys.stdin.readline

N = int(input())
reg = re.compile('(100+1+|01)+')

for _ in range(N):
    s = input().strip()
    print('YES' if reg.fullmatch(s) else 'No')

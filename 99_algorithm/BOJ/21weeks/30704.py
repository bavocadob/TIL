import math
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    root = int(math.sqrt(N))

    square = root * root
    if N == square:
        print(root * 4)
    elif N <= square + root:
        print(root * 4 + 2)
    else:
        print(root * 4 + 4)
